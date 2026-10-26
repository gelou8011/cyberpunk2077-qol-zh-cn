# 构建与复核

## CET 中文构建

- 上游：https://github.com/maximegmd/CyberEngineTweaks
- 标签：`v1.38.1`
- 固定提交：`213151fa22c79182922a08a44e4a44d44739d1cd`
- RED4ext.SDK：`5246e659d783e5834cc08a90e56c8932c9ed3449`
- 本次工具：Visual Studio 2022 Build Tools（C++）、xmake 3.1.2。

在本仓库根目录执行：

```powershell
git clone --recursive --branch v1.38.1 https://github.com/maximegmd/CyberEngineTweaks.git work/CET
git -C work/CET rev-parse HEAD
git -C work/CET apply --check ../../patches/cet-v1.38.1-zh-cn.patch
git -C work/CET apply ../../patches/cet-v1.38.1-zh-cn.patch
Set-Location work/CET
xmake f -y -m release -p windows -a x64
xmake -y -j 4
```

输出：`build/windows/x64/release/cyber_engine_tweaks.asi`。依赖安装和构建前提也请参照上游 README。

源码差异仅涉及静态界面文字、手电筒按键组显示名称和 MSVC UTF-8 编译参数。绑定 ID、Lua API、游戏数据库标识符保持原值。

公开 ASI 的 PE CodeView 调试记录及 6 处断言用宽字符源码路径仅保留文件名，清除了本机构建目录；程序代码、导入表和节布局未改动。处理工具为 `scripts/strip_pdb_path.py`，用法：`python scripts/strip_pdb_path.py <输入ASI> <另存输出ASI>`。公开二进制与本机验证构建的 SHA256 因这项诊断信息处理而不同。所有安装摘要见 `patches/payloads.json`。

## 模组文字补丁

`patches/mod-texts.json` 记录每个原文件和目标文件 SHA256、精确替换文本及次数。安装器在内存中生成全部结果并检查摘要，全部通过后才备份、写入。版本不匹配时请重新核对原作者版本，不要绕过校验。

## 本地化归档

源文件：`resources/codex_qol_zh/onscreens.json.json`。本次使用 WolvenKit Console 9.1.0 的 `cr2w --deserialize` 生成 CR2W，然后以保留 depot 路径的目录执行 `pack`：

```powershell
WolvenKit.CLI.exe cr2w --deserialize -i resources/codex_qol_zh/onscreens.json.json -o work/archive/codex_qol_zh
WolvenKit.CLI.exe pack -p work/archive -o work/packed
```

打包输入必须包含 `codex_qol_zh/onscreens.json`，不能把文件放平到归档根目录。复制配套 `.archive.xl`，`en-us`、`zh-cn` 均映射到该资源，确保英文后备文本不会覆盖中文标题。Mod Settings 的映射调整也包含在文字补丁中。

运行时探测只读取版本、归档状态、设置数量和本地化文本，探测脚本已经从游戏中移除。仓库不包含该临时脚本、完整运行日志或存档。
