"""Apply the version-locked Chinese translation without redistributing original mods."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CET = 'bin/x64/plugins/cyber_engine_tweaks'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def inside(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()) or path == root.resolve():
        raise ValueError('Unsafe relative path in manifest')
    return path

def build_changes(game, skip_cet=False):
    changes = []
    for entry in load(ROOT / 'patches/mod-texts.json'):
        path = inside(game, entry['path'])
        original = path.read_bytes()
        if digest(original) == entry['localized_sha256']:
            continue
        if digest(original) != entry['original_sha256']:
            raise ValueError('Original version/hash mismatch: ' + entry['path'])
        text = original.decode('utf-8-sig')
        if entry.get('output_newline') == 'crlf':
            text = text.replace('\r\n', '\n').replace('\r', '\n')
        for edit in entry['replacements']:
            if text.count(edit['old']) != edit['count']:
                raise ValueError('Unexpected source text: ' + entry['path'])
            text = text.replace(edit['old'], edit['new'])
        if entry.get('output_newline') == 'crlf':
            text = text.replace('\n', '\r\n')
        translated = text.encode('utf-8')
        if digest(translated) != entry['localized_sha256']:
            raise ValueError('Translation hash mismatch: ' + entry['path'])
        changes.append((entry['path'], original, translated))
    for entry in load(ROOT / 'patches/payloads.json'):
        if skip_cet and entry['path'].endswith('.asi'):
            continue
        path = inside(game, entry['path'])
        original = path.read_bytes() if path.exists() else None
        old_hash = digest(original) if original is not None else None
        if old_hash == entry['sha256']:
            continue
        if old_hash not in entry['accepted_original_sha256']:
            raise ValueError('Original version/hash mismatch: ' + entry['path'])
        translated = inside(ROOT / 'payload', entry['path']).read_bytes()
        if digest(translated) != entry['sha256']:
            raise ValueError('Payload hash mismatch: ' + entry['path'])
        changes.append((entry['path'], original, translated))
    font = inside(game, CET + '/fonts/NotoSansSC-Regular.otf')
    if not font.is_file():
        raise ValueError('Install the official CET Chinese font first: NotoSansSC-Regular.otf')
    rel = CET + '/config.json'
    path = inside(game, rel)
    original = path.read_bytes()
    config = json.loads(original.decode('utf-8-sig'))
    settings = config.setdefault('font', {})
    if settings.get('path') != 'NotoSansSC-Regular.otf' or settings.get('language') != 'ChineseFull':
        settings.update(path='NotoSansSC-Regular.otf', language='ChineseFull')
        translated = (json.dumps(config, ensure_ascii=False, indent=4) + '\n').encode('utf-8')
        changes.append((rel, original, translated))
    return changes

def ensure_game_closed():
    if os.name == 'nt':
        result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq Cyberpunk2077.exe', '/FO', 'CSV', '/NH'], capture_output=True, text=True, errors='replace', check=True)
        if '"cyberpunk2077.exe"' in result.stdout.lower():
            raise ValueError('Save and close Cyberpunk 2077 before installing or restoring.')

def apply_changes(game, changes, backup_parent=None):
    if not changes:
        return None
    backup_parent = backup_parent or ROOT / '.backups'
    backup = backup_parent / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup.mkdir(parents=True, exist_ok=False)
    manifest = {'game_root': str(game.resolve()), 'files': []}
    for rel, old, new in changes:
        target = inside(game, rel)
        current = target.read_bytes() if target.exists() else None
        if current != old:
            raise ValueError('File changed after preflight: ' + rel)
        if old is not None:
            saved = inside(backup / 'files', rel)
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_bytes(old)
        manifest['files'].append({'path': rel, 'existed': old is not None, 'original_sha256': digest(old) if old is not None else None, 'installed_sha256': digest(new)})
    (backup / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    written = []
    try:
        for rel, old, new in changes:
            target = inside(game, rel)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(new)
            written.append((target, old))
            if digest(target.read_bytes()) != digest(new):
                raise ValueError('Installed hash mismatch: ' + rel)
    except Exception:
        for target, old in reversed(written):
            if old is None:
                target.unlink(missing_ok=True)
            else:
                target.write_bytes(old)
        raise
    return backup

def rollback(game, backup):
    manifest = load(backup / 'manifest.json')
    if Path(manifest['game_root']).resolve() != game.resolve():
        raise ValueError('Backup belongs to a different game directory.')
    changes = []
    for entry in manifest['files']:
        path = inside(game, entry['path'])
        if not path.exists() or digest(path.read_bytes()) != entry['installed_sha256']:
            raise ValueError('Installed file was changed; restore cancelled: ' + entry['path'])
        original = None
        if entry['existed']:
            original = inside(backup / 'files', entry['path']).read_bytes()
            if digest(original) != entry['original_sha256']:
                raise ValueError('Backup hash mismatch: ' + entry['path'])
        changes.append((path, original))
    for path, original in changes:
        if original is None:
            path.unlink()
        else:
            path.write_bytes(original)

def main():
    parser = argparse.ArgumentParser(description='Version-locked Chinese localization for Cyberpunk 2077 QoL mods and CET')
    parser.add_argument('--game-root', required=True, type=Path)
    parser.add_argument('--check', action='store_true', help='Validate all inputs without writing game files')
    parser.add_argument('--skip-cet', action='store_true', help='Keep your existing CET binary; still configure its Chinese font')
    parser.add_argument('--rollback', type=Path, metavar='BACKUP_DIRECTORY')
    args = parser.parse_args()
    game = args.game_root.resolve()
    if not (game / 'bin/x64/Cyberpunk2077.exe').is_file():
        raise ValueError('Game executable not found under --game-root')
    if args.rollback:
        if args.check:
            raise ValueError('--check and --rollback cannot be combined')
        ensure_game_closed()
        rollback(game, args.rollback.resolve())
        print('Backup restored. Save files were not touched.')
        return
    changes = build_changes(game, args.skip_cet)
    print('Validated changes: ' + str(len(changes)))
    if args.check:
        return
    ensure_game_closed()
    backup = apply_changes(game, changes)
    print('Already localized.' if backup is None else 'Installed. Backup: ' + str(backup))

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print('Error: ' + str(exc), file=sys.stderr)
        sys.exit(1)
