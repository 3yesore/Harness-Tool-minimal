# Staged Commit Plan

This file turns the freeze groups into directly executable `git add` / `git commit` batches. It does not replace `FREEZE_GROUPS.en.md`; it converts the freeze order into an operational staging plan.

## General Rule

- commit `core / contract` first
- then commit the `skill mirror`
- then commit the `bridge / binding`
- commit `release / snapshot` last
- do not add features in this round

## Exclude Non-Release Artifacts First

These should not enter any freeze batch:

- `examples/openharness_app/node_modules/`
- all `__pycache__/`
- temporary output caused by terminal encoding noise

Recommended first check:

```bash
git status --short
```

Make sure these are not being staged:

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
git add docs/STAGED_COMMIT_PLAN.md docs/STAGED_COMMIT_PLAN.en.md
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

## Classification Of Previously Ambiguous Files

### Core / Contract

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

Reason:
- they define repository behavior, boundaries, and contract expectations

### Skill Mirror

- `.openclaw_skill/profiles/`
- `.openclaw_skill/templates/`
- `.openclaw_skill/scripts/apply_harness.py`
- `.openclaw_skill/references/changelog_template.md`

Reason:
- they are mirror artifacts of the main contract path

### Bridge / Binding

- `docs/CURRENT_CHANGESET_INDEX.*`
- `docs/WORK_INDEX.*`
- `docs/FREEZE_GROUPS.*`
- `docs/STAGED_COMMIT_PLAN.*`
- `docs/OPENHARNESS_*.md`
- `examples/local_extension/`
- `examples/openharness_app/`
- `adapters/`
- `scripts/openharness_*`

Reason:
- they organize and prove the OpenHarness compatibility path without changing core semantics

### Release / Snapshot

- `.github/workflows/validate.yml`
- `release/`
- `RELEASE_NOTES_v1.0.1_beta.md`
- `GITHUB_RELEASE.md`
- `GITHUB_RELEASE.en.md`

Reason:
- they describe release, CI, and snapshot behavior rather than core or bridge implementation

## Execution Notes

- run `git status --short` before each commit batch
- if a batch contains unrelated files, split them first
- this round is about freezing, not feature growth
