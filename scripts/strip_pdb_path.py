"""Remove local directories from unsigned PE32+ diagnostic path strings."""
import argparse
from pathlib import Path
import struct
import re

def strip(data):
    data = bytearray(data)
    pe = struct.unpack_from('<I', data, 0x3c)[0]
    if data[pe:pe+4] != b'PE\0\0':
        raise ValueError('Expected a PE binary')
    sections = struct.unpack_from('<H', data, pe+6)[0]
    optional_size = struct.unpack_from('<H', data, pe+20)[0]
    optional = pe+24
    if struct.unpack_from('<H', data, optional)[0] != 0x20b:
        raise ValueError('Expected PE32+')
    directory = optional+112
    if struct.unpack_from('<II', data, directory+4*8) != (0, 0):
        raise ValueError('Refusing to alter a signed binary')
    debug_rva, debug_size = struct.unpack_from('<II', data, directory+6*8)
    debug_offset = None
    for i in range(sections):
        record = optional+optional_size+i*40
        virtual_size, virtual_address, raw_size, raw_offset = struct.unpack_from('<IIII', data, record+8)
        if virtual_address <= debug_rva < virtual_address+max(virtual_size, raw_size):
            debug_offset = raw_offset+debug_rva-virtual_address
            break
    if debug_offset is None:
        raise ValueError('Debug directory not found')
    count = 0
    for off in range(debug_offset, debug_offset+debug_size, 28):
        kind, size, _, pointer = struct.unpack_from('<IIII', data, off+12)
        if kind != 2 or data[pointer:pointer+4] != b'RSDS':
            continue
        start = pointer+24
        end = data.index(0, start, pointer+size)
        old = bytes(data[start:end])
        basename = old.replace(b'\\', b'/').split(b'/')[-1]
        data[start:end] = basename+b'\0'*(end-start-len(basename))
        count += 1
    if not count:
        raise ValueError('CodeView PDB record not found')
    # MSVC embeds wide source filenames used by assertion diagnostics.
    # Keep each basename; do not alter executable code, layout or runtime resource paths.
    for match in list(re.finditer(rb'(?:[\x20-\x7e]\x00){8,}', data)):
        text = match.group().decode('utf-16-le')
        if not re.fullmatch(r'[A-Za-z]:[\\/].*\.(?:h|hpp|cpp|c)', text):
            continue
        basename = text.replace('\\', '/').split('/')[-1].encode('utf-16-le')
        data[match.start():match.end()] = basename+b'\0'*(len(match.group())-len(basename))
    return bytes(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('Use a separate output file')
    args.output.write_bytes(strip(args.input.read_bytes()))
