# 最终冻结分组

这个文件把当前工作树按可提交的冻结批次拆开。目标不是继续加功能，而是把已经完成的内容分层固定下来，避免 `core`、mirror、bridge、release 混在一个大 changeset 里。

## 冻结原则

- `harness_tool` 继续作为上游、contract-first 基底
- OpenHarness 兼容能力继续停留在 bridge / binding 外层
- 外部验证继续只作为兼容性证据，不变成 runtime ownership
- 本轮不新增通用 adapter，也不继续加深 OpenHarness runtime 集成

## Freeze Group 1: Core / Contract

这组应最先冻结。它定义 `harness_tool` 的稳定叙事和最小合同。

建议包含：
- `README.md`
- `README.en.md`
- `INDEX.md`
- `INDEX.en.md`
- `HARNESS_SPEC.md`
- `HARNESS_SPEC.en.md`
- `CORE_PROTOCOL.md`
- `ADAPTER_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`
- `AI_CHECKLIST.md`
- `AI_OPERATIONS.md`
- `AI_OPERATIONS.en.md`
- `DESIGN_REVIEW.md`
- `EXTENSION_POINTS.md`
- `EXTENSION_POINTS.en.md`
- `VERSION_ROADMAP.md`
- `VERSION_ROADMAP.en.md`
- `profiles/README.md`
- `profiles/README.en.md`
- `profiles/default.rules.json`
- `profiles/python-service.rules.json`
- `templates/INDEX.md.template`
- `templates/SPEC.md.template`
- `templates/CHANGELOG.md.template`
- `tools/init_module.py`
- `tools/apply_harness.py`
- `tools/validate_module.py`
- `tools/fix_module.py`
- `harness_core/`
- `examples/hello_world/INDEX.md`
- `examples/hello_world/SPEC.md`

提交意图：
- 冻结 contract-first 基线
- 冻结顶层叙事
- 不引入新的 core 语义

## Freeze Group 2: Skill Mirror

这组只做 mirror 对齐，不引入独立语义。

建议包含：
- `.openclaw_skill/SKILL.md`
- `.openclaw_skill/references/harness_spec.md`
- `.openclaw_skill/references/index_template.md`
- `.openclaw_skill/references/spec_template.md`
- `.openclaw_skill/references/changelog_template.md`
- `.openclaw_skill/references/validation_rules.md`
- `.openclaw_skill/profiles/`
- `.openclaw_skill/templates/`
- `.openclaw_skill/scripts/init_harness_module.py`
- `.openclaw_skill/scripts/apply_harness.py`
- `.openclaw_skill/scripts/validate_harness.py`

提交意图：
- 让 OpenClaw mirror 跟随主合同
- 明确 mirror 不是独立产品面

## Freeze Group 3: Bridge / Binding

这组收口 OpenHarness 兼容能力，但不进入 `core`。

建议包含：
- `OPENHARNESS_BRIDGE.md`
- `OPENHARNESS_BRIDGE.en.md`
- `OPENHARNESS_SDK_BINDING.md`
- `OPENHARNESS_SDK_BINDING.en.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.en.md`
- `adapters/`
- `scripts/openharness_validate_transport.py`
- `scripts/openharness_sdk_binding_export.py`
- `examples/local_extension/`
- `examples/openharness_app/`
- `docs/OPENHARNESS_*.md`
- `docs/CURRENT_CHANGESET_INDEX.md`
- `docs/CURRENT_CHANGESET_INDEX.en.md`
- `docs/WORK_INDEX.md`
- `docs/WORK_INDEX.en.md`
- `docs/FREEZE_GROUPS.md`
- `docs/FREEZE_GROUPS.en.md`

提交意图：
- 固定 narrow bridge / binding 形状
- 固定 process transport、external app template、mock dry-run 验证
- 明确 provider / middleware 仍然只是 bridge metadata

明确不做：
- live provider wiring
- live middleware wiring
- non-process transport
- session / conversation validation
- real model invocation

## Freeze Group 4: Release / Snapshot

最后冻结发布叙事，不夸大未实现能力。

建议包含：
- `GITHUB_RELEASE.md`
- `GITHUB_RELEASE.en.md`
- `RELEASE_NOTES_v1.0.1_beta.md`
- `release/`
- `.github/`

提交意图：
- 固定对外发布口径
- 强调 upstream base + bridge compatibility + external verification
- 明确 `core` 不宿主 runtime

## 推荐提交顺序

1. Freeze Group 1: Core / Contract
2. Freeze Group 2: Skill Mirror
3. Freeze Group 3: Bridge / Binding
4. Freeze Group 4: Release / Snapshot

## 发布前最低检查

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `npm run build` in `C:\\Users\\Y2516\\Desktop\\openharness_app_external_verify`
- `npm run smoke` in `C:\\Users\\Y2516\\Desktop\\openharness_app_external_verify`

## 发布判断

当前内容已经接近可发布，但不建议从一个未分组的大工作树直接发布。

正确动作是：
- 先按本文件拆成冻结批次
- 再以你自己的项目名义发布
- 然后把 docs / example / compatibility note 这类窄贡献回流给 OpenHarness
