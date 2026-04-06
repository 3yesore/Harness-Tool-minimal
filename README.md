# Harness Tool Minimal v1.0.1 beta

[![Validate](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml/badge.svg)](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.1-beta-blue.svg)](docs/VERSION_ROADMAP.md)

这是仓库的默认主页，也是当前默认展示的 beta 基线版本。  
`v1.0.1 beta` 不是厚平台，而是一个围绕 minimal 基线做收口和加固的历史版本主页：核心更薄、合同更硬、扩展入口更清楚，同时保留足够大的项目级自定义空间。

## 你会得到什么

- 一套最小闭环：初始化、接入、验证、记录
- 一套可执行验证：`validate_module.py` 会实际运行 `tests/smoke.py`
- 一套轻量扩展面：`profiles/`、`templates/`、`.openclaw_skill/`
- 一套可交接结构：`INDEX.md`、`SPEC.md`、`CHANGELOG.md`
- 一套发布资源：中文主页、英文镜像、展示页、升级清单

## 这版适合什么场景

- 小项目
- 小模块
- 开发初期
- 需要 AI 参与维护但又希望上下文可恢复的项目

## 快速上手

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

## 仓库内容

- `tools/init_module.py`：初始化模块骨架
- `tools/apply_harness.py`：为现有模块补 Harness
- `tools/validate_module.py`：校验文档、配置和冒烟测试
- `templates/`：文档模板
- `profiles/`：规则预设
- `examples/`：参考示例
- `.openclaw_skill/`：OpenClaw / Codex skill 包

## 示例

- `examples/hello_world`
- `examples/user_service`
- `examples/local_extension`

## 安装 Skill

### OpenClaw

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.openclaw\skills" | Out-Null
Copy-Item -Recurse -Force ".openclaw_skill" "$env:USERPROFILE\.openclaw\skills\harness"
```

### Codex / VS Code

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".openclaw_skill" "$env:USERPROFILE\.codex\skills\harness"
```

## 文档入口

- [docs/README.md](docs/README.md)
- [README.en.md](README.en.md)
- [docs/VERSION_ROADMAP.md](docs/VERSION_ROADMAP.md)

## 历史版本

- `v1.0.0`：初始 minimal 版本，作为历史锚点保留

## 当前状态

`v1.0.1 beta`，当前默认展示的主页版本。后续如果继续推进新扩展，会在保持 minimal 基线的前提下逐步回流到主线。
