# 赛博朋克 2077：六项便利模组及 CET 简体中文补丁

针对 Windows PC 游戏 **2.5** 整理的独立汉化。翻译菜单、设置项、说明、按键显示名称和确认提示，并提供基于官方 **CET v1.38.1** 的中文构建。

原模组功能由各自作者开发。本仓库提供汉化与安装工具，作者、固定版本、原始下载出处和许可证见 **[SOURCES.md](SOURCES.md)**。其他社区汉化仅用于版本调研，未下载、复制或套用。

| 模组 / 工具 | 适配版本 | 汉化内容 |
| --- | --- | --- |
| Simple Flashlight 内置手电筒 | 2.5 | 设置、说明、颜色、按键显示名称 |
| In-World Navigation 全息导航 | 0.1.24 | 标题、12 项设置、说明及显示模式 |
| Reset Attributes Always Available 无限重置属性 | 1.0.0.5 | 属性重置确认提示 |
| Better Loot Markers 战利品标记 | 1.4.0 | CET 设置窗口及选项 |
| Smarter Scrapper 自动拆解 | 2.3.6 | 标题；分类、品质沿用游戏中文 |
| Hacking Gets Tedious 自动入侵 | 1.1 | 原模组未新增文案，沿用游戏中文，无需补丁 |
| Native Settings UI | 1.97 | “模组”入口和空列表提示 |
| Mod Settings | 0.2.25 | 入口、恢复默认及放弃更改提示 |
| Cyber Engine Tweaks | 1.38.1 | 控制台、按键、设置、游戏日志、TweakDB 编辑器等常用界面 |

## 安装

1. 先从原作者处安装上表对应版本和所需前置：CET、RED4ext、ArchiveXL、TweakXL、redscript、Input Loader、Native Settings UI、Mod Settings。出处表优先列 GitHub 和 CurseForge。
2. 安装 Python **3.10+**，下载本仓库的 ZIP 并完整解压。保存并退出游戏。
3. 在仓库目录打开终端，先检查，再安装；把示例路径替换成你的游戏目录：

```powershell
python scripts/install.py --game-root 'C:\Games\Cyberpunk 2077' --check
python scripts/install.py --game-root 'C:\Games\Cyberpunk 2077'
```

安装器按 SHA256 校验原文件，版本不匹配会在写入前停止。它只修改对应文本、CET 中文构建和字体配置；保留其他配置和快捷键，不读写存档，不自动下载原模组。

若想保留自己的 CET 二进制，可以两次命令均加 `--skip-cet`；这样 CET 常用界面本身不会获得本仓库的中文翻译。

CET 官方包附带的 `NotoSansSC-Regular.otf` 必须位于 CET 的 `fonts` 目录。安装器仅把 `font.path` 设为该文件名、`font.language` 设为 `ChineseFull`，其他设置保留。字体配置依据 [CET 官方说明](https://wiki.redmodding.org/cyber-engine-tweaks/console/settings/config-file/change-font-and-font-size)。

备份在 `.backups/<时间>/`，安装成功后终端会显示具体目录。退出游戏后可撤回：

```powershell
python scripts/install.py --game-root 'C:\Games\Cyberpunk 2077' --rollback '.backups/<时间>'
```

若文件安装后又被其他工具修改，撤回会停止，避免覆盖新改动。

## 仓库内容

- `patches/mod-texts.json`：原文件摘要与文字替换表，不含完整原模组。
- `patches/cet-v1.38.1-zh-cn.patch`：CET 官方固定提交上的源码差异。
- `payload/`：自制中文本地化归档，以及 CET 中文 ASI；相关许可证保留在 `licenses/`。
- `translations/`、`resources/`：翻译字典及 WolvenKit 可编辑资源。
- `scripts/install.py`：版本校验、安装、独立备份及撤回。
- [BUILD.md](BUILD.md)：源码版本与构建说明。
- [docs/PRIVACY.md](docs/PRIVACY.md)：公开上传前的隐私检查范围。

## 验证与范围

LuaJIT 2.1 语法检查、redscript 离线与游戏启动编译均已通过；CET v1.38.1 已运行，手电筒归档检测为真，10 项设置成功初始化，导航和模组标题已在运行时读回中文。脱敏后的结果见 [验证记录](docs/runtime-verification.json)。

原先 CET v1.38.0 的 SDK 对游戏 2.5 的 Mod 归档类型处理有误。此处采用官方 [v1.38.1](https://github.com/maximegmd/CyberEngineTweaks/releases/tag/v1.38.1) 基线及其 [上游修复](https://github.com/maximegmd/CyberEngineTweaks/pull/1074)，没有自行改写手电筒玩法逻辑。

脚本 API、数据库类型/记录/字段标识符、原始日志及 ImGui 底层诊断内容保留原文。本次未进入存档实测导航路线、拾取拆解、洗点和入侵奖励。补丁适配表中的固定版本，后续版本需要重新核对。

## 许可

本仓库新增的翻译、安装工具和文档采用 [MIT](LICENSE)。各原模组及 CET、依赖的权利仍属于原作者，以 [出处说明](SOURCES.md) 和 `licenses/` 中的原始条款为准。未明确允许重新分发的原模组仅提供文字替换表，需要使用者自行安装原件。
