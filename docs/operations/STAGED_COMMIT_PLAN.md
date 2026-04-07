# 提交分组执行方案

这个文件把当前工作树拆成可直接执行的 `git add` / `git commit` 批次。它不替代 `FREEZE_GROUPS.md`，而是把冻结分组变成可操作命令。

## 总原则

- 先提交 `core / contract`
- 再提交 `skill mirror`
- 再提交 `bridge / binding`
- 最后提交 `release / snapshot`
- 不要在这轮继续加功能

## 先排除不应提交的内容

这些内容不应进入任何冻结批次：

- `examples/openharness_app/node_modules/`
- 所有 `__pycache__/`
- 终端编码噪声导致的临时输出文件

推荐先执行：

```bash
git status --short
```

确认以下内容不会被纳入：

- `examples/openharness_app/node_modules/`
- `adapters/__pycache__/`
- `scripts/__pycache__/`
- `harness_core/__pycache__/`

## Freeze Group 1: Core / Contract

```bash
git add README.md README.en.md
git add INDEX.md INDEX.en.md
git add HARNESS_SPEC.md HARNESS_SPEC.en.md
git add CORE_PROTOCOL.md ADAPTER_PROTOCOL.md EXTENSION_PROTOCOL.md
git add AI_CHECKLIST.md AI_OPERATIONS.md AI_OPERATIONS.en.md
git add DESIGN_REVIEW.md
git add EXTENSION_POINTS.md EXTENSION_POINTS.en.md
git add VERSION_ROADMAP.md VERSION_ROADMAP.en.md
git add profiles/README.md profiles/README.en.md
git add profiles/default.rules.json profiles/python-service.rules.json
git add templates/INDEX.md.template templates/SPEC.md.template templates/CHANGELOG.md.template
git add tools/init_module.py tools/apply_harness.py tools/validate_module.py tools/fix_module.py
git add harness_core/
git add examples/hello_world/INDEX.md examples/hello_world/SPEC.md
git commit -m "freeze core contract baseline"
```

## Freeze Group 2: Skill Mirror

```bash
git add .openclaw_skill/SKILL.md
git add .openclaw_skill/references/harness_spec.md
git add .openclaw_skill/references/index_template.md
git add .openclaw_skill/references/spec_template.md
git add .openclaw_skill/references/changelog_template.md
git add .openclaw_skill/references/validation_rules.md
git add .openclaw_skill/profiles/
git add .openclaw_skill/templates/
git add .openclaw_skill/scripts/init_harness_module.py
git add .openclaw_skill/scripts/apply_harness.py
git add .openclaw_skill/scripts/validate_harness.py
git commit -m "align openclaw skill mirror with frozen contract"
```

## Freeze Group 3: Bridge / Binding

```bash
git add OPENHARNESS_BRIDGE.md OPENHARNESS_BRIDGE.en.md
git add OPENHARNESS_SDK_BINDING.md OPENHARNESS_SDK_BINDING.en.md
git add OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.en.md
git add adapters/
git add scripts/openharness_validate_transport.py scripts/openharness_sdk_binding_export.py
git add examples/local_extension/
git add examples/openharness_app/
git add docs/OPENHARNESS_*.md
git add docs/CURRENT_CHANGESET_INDEX.md docs/CURRENT_CHANGESET_INDEX.en.md
git add docs/WORK_INDEX.md docs/WORK_INDEX.en.md
git add docs/FREEZE_GROUPS.md docs/FREEZE_GROUPS.en.md
git add docs/STAGED_COMMIT_PLAN.md
git commit -m "freeze openharness bridge and binding layer"
```

## Freeze Group 4: Release / Snapshot

```bash
git add GITHUB_RELEASE.md GITHUB_RELEASE.en.md
git add RELEASE_NOTES_v1.0.1_beta.md
git add release/
git add .github/
git commit -m "freeze release snapshot narrative"
```

## 边界不清文件的归类结论

### 归到 Core / Contract

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

原因：
- 它们定义的是仓库自身的工作方式、边界和合同，不是 bridge 行为。

### 归到 Skill Mirror

- `.openclaw_skill/profiles/`
- `.openclaw_skill/templates/`
- `.openclaw_skill/scripts/apply_harness.py`
- `.openclaw_skill/references/changelog_template.md`

原因：
- 这些都是主合同的 mirror，不应进入 bridge 或 release。

### 归到 Bridge / Binding

- `docs/CURRENT_CHANGESET_INDEX.*`
- `docs/WORK_INDEX.*`
- `docs/FREEZE_GROUPS.*`
- `docs/STAGED_COMMIT_PLAN.md`
- `docs/OPENHARNESS_*.md`
- `examples/local_extension/`
- `examples/openharness_app/`
- `adapters/`
- `scripts/openharness_*`

原因：
- 这些文件用于组织和证明 OpenHarness 兼容路径，不改变 `core` 语义。

### 归到 Release / Snapshot

- `.github/workflows/validate.yml`
- `release/`
- `RELEASE_NOTES_v1.0.1_beta.md`
- `GITHUB_RELEASE.md`
- `GITHUB_RELEASE.en.md`

原因：
- 它们描述发布、CI 和快照口径，不属于 core 或 bridge 实现。

## 执行提示

- 每提交一组前先跑 `git status --short`
- 如果某组里混入了不属于该组的文件，先拆开，不要图快
- 本轮目标是冻结，不是继续扩功能
