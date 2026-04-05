# Harness Tool Minimal

[![Validate](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml/badge.svg)](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.1-beta-blue.svg)](docs/VERSION_ROADMAP.md)

面向模块维护的 Harness Engineering 最小工具集。

它把模块入口、规范、冒烟测试和变更记录收拢成一套可验证、可交接的流程，适合测试仓库整理后继续发布，也适合拿来做轻量模块接管。

## 你会得到什么

- 一套最小闭环：初始化、接入、验证、记录
- 一套可执行验证：`validate_module.py` 会实际运行 `tests/smoke.py`
- 一套可扩展结构：`profiles/`、`.openclaw_skill/`、`templates/`
- 一套发布入口：中文主文档 + 英文镜像 + GitHub Actions 校验

## 快速上手

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

## 适合谁

- 想把一个模块整理成“可交接、可验证”结构的人
- 想给现有项目补上 `INDEX.md`、`SPEC.md`、`CHANGELOG.md` 的人
- 想把同一套流程同时交给 OpenClaw 和 Codex 使用的人

## 仓库包含什么

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

## 安装 Skill

### 在线下载

- [下载 skill ZIP](https://github.com/3yesore/Harness-Tool-minimal/archive/refs/heads/main.zip)
- 或在 GitHub 页面点击 `Code` -> `Download ZIP`

下载后解压，将 `.openclaw_skill` 目录复制到你的本地 skill 目录即可。
如果你的 skill 管理器支持按名字安装，也可以把这个包发布到对应的 skill 目录或仓库后再用名字安装。

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

## 当前状态

v1.0.1 beta，当前以基线加固和标准化扩展入口为主，仍建议在小项目、小模块和开发初期使用。欢迎反馈。
