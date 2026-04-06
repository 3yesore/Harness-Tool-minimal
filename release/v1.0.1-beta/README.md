# Harness Tool Minimal v1.0.1 beta

[![Validate](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml/badge.svg)](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](../../LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.1-beta-blue.svg)](../VERSION_ROADMAP.md)

这是一个围绕 minimal 基线做收口和加固的 beta 发布包。  
它保留了最小但完整的 Harness 工作流，同时把标准化入口、验证流程和扩展边界继续做清楚，适合小项目、小模块和开发初期使用。

## 这次更新重点

- 保持 `init / apply / validate` 的最小闭环
- 保持 `INDEX.md`、`SPEC.md`、`CHANGELOG.md`、`tests/smoke.py` 的可交接结构
- 保持 `profiles/`、`templates/` 和 `.openclaw_skill/` 作为轻量扩展面
- 继续用 GitHub Actions 做基础校验
- 保持中文主入口 + 英文镜像的发布形式

## 你会得到什么

- 一套最小闭环：初始化、接入、验证、记录
- 一套可执行验证：`validate_module.py` 会实际运行 `tests/smoke.py`
- 一套轻量扩展：`profiles/`、`templates/`、`.openclaw_skill/`
- 一套发布准备：中文主页、英文镜像、发布说明和检查清单

## 适合谁

- 想把一个模块整理成“可交接、可验证”结构的人
- 想给现有项目补上 `INDEX.md`、`SPEC.md`、`CHANGELOG.md` 的人
- 想把同一套流程同时交给 OpenClaw 和 Codex 使用的人
- 想在开发初期就把模块纳入 Harness 工作流的人

## 包含内容

- `README.md` / `README.en.md`
- `VERSION_DESCRIPTION.zh.md` / `VERSION_DESCRIPTION.en.md`
- `GITHUB_RELEASE.zh.md` / `GITHUB_RELEASE.en.md`
- `DISPLAY_PAGE.zh.md` / `DISPLAY_PAGE.en.md`
- `MANIFEST.md`
- `PUBLISH_CHECKLIST.zh.md` / `PUBLISH_CHECKLIST.en.md`
- `UPGRADE_CHECKLIST.zh.md` / `UPGRADE_CHECKLIST.en.md`

## 版本说明

更完整的版本描述请看：

- [VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)
- [VERSION_DESCRIPTION.en.md](VERSION_DESCRIPTION.en.md)
