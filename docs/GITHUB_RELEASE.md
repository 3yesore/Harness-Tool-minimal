# GitHub Release Guide

这个文件用于仓库顶层的发布口径，不替代 `release/v1.0.1-beta/` 发布包。

## v1.0.1 beta 的统一发布叙事

`Harness Tool Minimal v1.0.1 beta` 应按下面这条主线发布：

- `harness_tool` 是上游、contract-first 基底
- `harness_core` 只负责协议、验证、阶段和 scaffold 语义
- OpenHarness 兼容能力停留在 bridge / binding 外层
- 外部验证证明兼容性，不代表 `core` 宿主 runtime

## 这次发布可以明确说什么

- 已冻结 core / contract baseline
- 已对齐 templates、profiles、examples 和 OpenClaw skill mirror
- 已提供 OpenHarness-compatible bridge / binding
- 已在外部 OpenHarness app 目录完成验证

## 这次发布不能夸大什么

- 不能说已完整接入 OpenHarness runtime
- 不能说已完成 live provider wiring
- 不能说已完成 live middleware wiring
- 不能说 `harness_core` 承担 runtime ownership

## 建议发布摘要

```markdown
## Harness Tool Minimal v1.0.1 beta

This release freezes the current contract-first baseline instead of turning the project into a thicker platform.

Highlights:
- upstream contract-first base
- thin `harness_core` with explicit protocol boundaries
- synced OpenClaw skill mirror
- OpenHarness-compatible bridge and binding layer
- repo-external OpenHarness verification

Notes:
- OpenHarness compatibility remains bridge-side
- external verification is compatibility evidence, not runtime ownership
- live provider/middleware wiring is still intentionally out of scope
```

## 发布前检查

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python tools/validate_module.py examples/local_extension --strict --profile default
python tools/validate_module.py examples/openharness_app --strict --profile default
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
```

外部 OpenHarness 验证：

```bash
cd C:/Users/Y2516/Desktop/openharness_app_external_verify
npm run build
npm run smoke
```

## 发布顺序

1. 先完成 freeze groups 的提交分组
2. 再打标签 `v1.0.1-beta`
3. 再发布 release 包
4. 后续若要贡献给 OpenHarness，上游贡献以 docs / example / compatibility note 为主
