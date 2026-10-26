# 原作者、来源与版本

汉化整理日期：2026-10-26。以下作者开发了原模组和工具；本仓库的贡献是独立中文翻译、汉化源码差异和安装工具。中文补丁不代表原作者官方版本。

## 原模组与工具

| 项目 | 原作者 / 上游维护者 | 本次版本 / 固定提交 | 原始出处 | 仓库处理 |
| --- | --- | --- | --- | --- |
| Cyber Engine Tweaks | yamashi、CET 项目贡献者 | v1.38.1 / `213151fa22c79182922a08a44e4a44d44739d1cd` | [官方源码](https://github.com/maximegmd/CyberEngineTweaks)、[对应发布](https://github.com/maximegmd/CyberEngineTweaks/releases/tag/v1.38.1) | MIT；提供源码差异和中文构建，保留许可证 |
| Simple Flashlight | keanuWheeze；Nexus 上传账号 NexusGuy999 | 2.5 | [作者页面](https://www.nexusmods.com/cyberpunk2077/mods/2913) | 仅文字替换表，不重传原脚本和资源 |
| In-World Navigation | Jack Humbert / jackhumbert | 0.1.24 | [官方源码](https://github.com/jackhumbert/in_world_navigation)、[对应发布](https://github.com/jackhumbert/in_world_navigation/releases/tag/v0.1.24) | 自制本地化键值，不重传原插件；原包含 MIT |
| Reset Attributes Always Available | yakuzadeso；创意及 REDmod 原作 FarisFaux | 1.0.0.5 | [作者 CurseForge 页面](https://www.curseforge.com/cyberpunk-2077/mods/reset-attributes-always-available-redscript)、[对应文件](https://www.curseforge.com/cyberpunk-2077/mods/reset-attributes-always-available-redscript/files/8744608)、[Nexus](https://www.nexusmods.com/cyberpunk2077/mods/9240) | 仅确认提示替换表，不重传原脚本 |
| Better Loot Markers | rodikh | 1.4.0 / `64b2487caa683de2d4e46dd71a90d9088669abbf` | [作者 GitHub](https://github.com/rodikh/BetterLootMarkers-Cyberpunk-mod) | 固定源码未见许可证；仅文字替换表 |
| Smarter Scrapper | djkovrik | 2.3.6 / `eb3ba46b25eb69e879a7ee8c370f2b0f813e9b02` | [作者 CP77Mods](https://github.com/djkovrik/CP77Mods)、[作者页面](https://www.nexusmods.com/cyberpunk2077/mods/2687) | 仅自制标题本地化，不重传原脚本 |
| Hacking Gets Tedious | shiide | 1.1 | [作者页面](https://www.nexusmods.com/cyberpunk2077/mods/6956) | 没有新增文案，无修改文件，不包含原模组 |
| Native Settings UI | keanuWheeze / justarandomguyintheinternet | 1.97 / `4065b51456f5e3df8f29e1dc3c07edcc294e68e9` | [作者 GitHub](https://github.com/justarandomguyintheinternet/CP77_nativeSettings)、[作者页面](https://www.nexusmods.com/cyberpunk2077/mods/3518) | 固定源码未见许可证；仅文字替换表 |
| Mod Settings | Jack Humbert / jackhumbert | 0.2.25 | [官方源码](https://github.com/jackhumbert/mod_settings)、[对应发布](https://github.com/jackhumbert/mod_settings/releases/tag/v0.2.25) | 原包 MIT；提供文字和本地化映射替换表 |

Simple Flashlight 原作者另注明 psiberx 提供了 GameUI.lua、Cron.lua；本仓库未分发这两份文件。CET 的第三方代码权利属于相应作者，保留于 `licenses/CET-ThirdParty-LICENSES.txt` 和 SDK 许可证文件中。

## 本次本地安装的下载来源

优先使用作者 GitHub、CurseForge。Simple Flashlight 和 Hacking Gets Tedious 当时使用了 DLCfun 镜像；镜像不是原作者页面，也不视为转载许可，本仓库不重传镜像原包。

| 下载内容 | 当时使用的来源 | 原包 SHA256 |
| --- | --- | --- |
| 全息导航 0.1.24 | [作者 GitHub Release](https://github.com/jackhumbert/in_world_navigation/releases/tag/v0.1.24) | `2c0e256b86f0e24dac39133ec245d9d302738b9cc9d6d1025fb61bd9da940b13` |
| Mod Settings 0.2.25 | [作者 GitHub Release](https://github.com/jackhumbert/mod_settings/releases/tag/v0.2.25) | `f724b3e07d1a83ef07ad96d67c95ae211ae5a17c9f041f7684dac5e6b20d4280` |
| 无限重置属性 1.0.0.5 | [作者 CurseForge 文件](https://www.curseforge.com/cyberpunk-2077/mods/reset-attributes-always-available-redscript/files/8744608) | `239ed2692e0221ec9bcda2bfee19ac87c0933354ee0da0ff12dd703ca293f618` |
| 手电筒 2.5 | [DLCfun 镜像](https://dlcfun.com/en/cyberpunk-2077/prostoi-fonarik) | `a530806a9558eff809c112656afa9ee836607401e7e68df1b69b6bd1ec7924ab` |
| 自动入侵 1.1 | [DLCfun 镜像](https://dlcfun.com/en/cyberpunk-2077/vzlom-stanovitsia-utomitelnym) | `a54b1f5d305a021bb9394064d3fca3557bf08906aaaded80a60cf3074e62e502` |

镜像包仅按文件名、版本和内容检查；没有取得 Nexus 原包独立摘要，不宣称与 Nexus 包逐字节一致。使用者应优先从作者页面取得原模组。

## 现成汉化的调研记录

只核对页面与版本，未使用下列译文或文件。它们的翻译权利属于各自作者，本仓库不声称继承其成果。

- 手电筒：[10048](https://www.nexusmods.com/cyberpunk2077/mods/10048)，声明适配 2.5。
- 战利品标记：[28942](https://www.nexusmods.com/cyberpunk2077/mods/28942)，对应 1.4.0。
- 无限洗点：[32033](https://www.nexusmods.com/cyberpunk2077/mods/32033) 对应 1.0.0.5；[31115](https://www.nexusmods.com/cyberpunk2077/mods/31115) 对应 1.0.0.4。
- 全息导航：[22835](https://www.nexusmods.com/cyberpunk2077/mods/22835)，对应较旧 0.1.20。
- Mod Settings：[23293](https://www.nexusmods.com/cyberpunk2077/mods/23293)，对应较旧 0.2.21。
- Native Settings UI：[23591](https://www.nexusmods.com/cyberpunk2077/mods/23591)，未明确声明适配 1.97。
- CET：[3DMXM 中文分支](https://github.com/3DMXM/CyberEngineTweaks_cn)，最后更新于 2023 年，不替代本次官方 1.38.1 基线。

需求参考来自 [小黑盒原帖](https://www.xiaoheihe.cn/app/bbs/link/d7a972ac0b57)。仅保留干净的帖子链接，已删除原分享链接中的会话和追踪参数。

## 制作与验证工具

- [WolvenKit](https://github.com/WolvenKit/WolvenKit) Console 9.1.0：本地化资源转换、打包与解包复核。
- [xmake](https://github.com/xmake-io/xmake) 3.1.2、Visual Studio 2022 Build Tools：CET 构建。
- [redscript](https://github.com/jac3km4/redscript) 0.5.32、LuaJIT 2.1：脚本编译及语法验证。
- [RED4ext.SDK](https://github.com/WopsS/RED4ext.SDK) 固定提交 `5246e659d783e5834cc08a90e56c8932c9ed3449`：CET 的上游 SDK。

不包含上述工具本体、游戏本体文件或中文字体包。
