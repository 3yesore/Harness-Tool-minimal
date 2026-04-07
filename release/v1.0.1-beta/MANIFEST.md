# 发布清单

这个清单列出 `Harness Tool 1.0.1` 发布时应一起对外的关键文件。它是发布包索引，不是自动打包脚本。

## 仓库主入口

- `README.md`
- `docs/INDEX.md`
- `docs/HARNESS_SPEC.md`
- `docs/VERSION_ROADMAP.md`
- `docs/DESIGN_REVIEW.md`
- `docs/AI_CHECKLIST.md`
- `docs/AI_OPERATIONS.md`
- `docs/GITHUB_RELEASE.md`
- `docs/RELEASE_NOTES_v1.0.1_beta.md`

## Core / Contract

- `docs/CORE_PROTOCOL.md`
- `docs/ADAPTER_PROTOCOL.md`
- `docs/EXTENSION_PROTOCOL.md`
- `harness_core/`
- `tools/`
- `templates/`
- `profiles/`

## Mirror / Examples

- `.openclaw_skill/`
- `examples/hello_world/`
- `examples/local_extension/`
- `examples/openharness_app/`

## OpenHarness Bridge

- `docs/OPENHARNESS_BRIDGE.md`
- `docs/OPENHARNESS_SDK_BINDING.md`
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `adapters/`
- `scripts/openharness_validate_transport.py`
- `scripts/openharness_sdk_binding_export.py`
- `docs/OPENHARNESS_*.md`

## 发布包内文案

- `release/v1.0.1-beta/README.md`
- `release/v1.0.1-beta/README.en.md`
- `release/v1.0.1-beta/VERSION_DESCRIPTION.zh.md`
- `release/v1.0.1-beta/VERSION_DESCRIPTION.en.md`
- `release/v1.0.1-beta/GITHUB_RELEASE.zh.md`
- `release/v1.0.1-beta/GITHUB_RELEASE.en.md`
- `release/v1.0.1-beta/PUBLISH_CHECKLIST.zh.md`
- `release/v1.0.1-beta/PUBLISH_CHECKLIST.en.md`

## CI / 发布辅助

- `.github/workflows/validate.yml`

## 版本标签

- Git 标签：`v1.0.1-beta`
- 对外展示版本名：`Harness Tool 1.0.1`
- 回滚锚点：`v1.0.0`

## 使用说明

- 如果发布到你自己的仓库，优先强调：
  - `harness_tool` 是上游、contract-first 基底
  - OpenHarness 支持是 bridge / binding 路径
  - 外部验证已完成
- 不要把这个版本表述成完整 OpenHarness runtime integration
