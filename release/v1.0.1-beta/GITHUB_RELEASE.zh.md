# Harness Tool Minimal v1.0.1 beta

`v1.0.1 beta` 是 `Harness Tool Minimal` 的冻结基线版本。

这次发布的重点不是继续把系统做厚，而是把已经形成的结构收成一条可以解释、可以验证、可以继续演进的主线：

- `harness_tool` 继续作为上游、contract-first 基底
- `harness_core` 继续保持薄，只承载协议、验证、阶段和 scaffold 语义
- OpenHarness 兼容能力继续停留在 bridge / binding 外层
- 外部验证继续只作为兼容性证据，不升级为 runtime ownership

## Highlights

- frozen core / contract baseline
- explicit `core / adapter / extension` boundaries
- aligned templates, rules, and examples
- synced OpenClaw skill mirror
- OpenHarness-compatible bridge and SDK binding
- repo-external OpenHarness app verification

## What This Release Means

这个版本可以作为你自己的项目基线发布。它已经具备：

- 上游 contract-first 叙事
- 统一的核心协议入口
- 本地扩展与模板化的稳定边界
- 可验证的 OpenHarness-compatible bridge

但它不应被表述成：

- 完整 OpenHarness runtime integration
- provider / middleware lifecycle integration
- session / conversation host runtime

## Verified Commands

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `npm run build` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- `npm run smoke` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`

## Notes

- 这是一次冻结与收口发布，不是平台化扩张发布
- OpenHarness 兼容能力当前仍是窄桥
- `v1.0.0` 继续作为回滚锚点

详细说明请见：

- [VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)
- [PUBLISH_CHECKLIST.zh.md](PUBLISH_CHECKLIST.zh.md)
