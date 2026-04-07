# Final Freeze Groups

This file splits the current working tree into commit-sized freeze batches. The goal is not to add more features. The goal is to lock down what is already finished so `core`, mirror, bridge, and release materials do not stay mixed in one large changeset.

## Freeze Principles

- `harness_tool` remains the upstream, contract-first base
- OpenHarness compatibility remains in the bridge / binding layer
- external verification remains compatibility evidence, not runtime ownership
- this round adds no new generic adapters and no deeper OpenHarness runtime integration

## Freeze Group 1: Core / Contract

Freeze this group first. It defines the stable `harness_tool` contract path and repository narrative.

Suggested scope:
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

Commit intent:
- freeze the contract-first baseline
- freeze the top-level narrative
- do not add new core semantics

## Freeze Group 2: Skill Mirror

This group only mirrors the frozen contract path. It must not introduce independent semantics.

Suggested scope:
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

Commit intent:
- keep the OpenClaw mirror aligned with the frozen contract
- make it explicit that the mirror is not a separate product surface

## Freeze Group 3: Bridge / Binding

This group freezes the OpenHarness-compatible bridge shape without moving any of it into `core`.

Suggested scope:
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

Commit intent:
- freeze the narrow bridge / binding shape
- keep process transport, external app template, and mock dry-run verification
- keep provider / middleware as bridge metadata only

Explicitly out of scope:
- live provider wiring
- live middleware wiring
- non-process transport
- session / conversation validation
- real model invocation

## Freeze Group 4: Release / Snapshot

Freeze release-facing material last and avoid overstating unfinished runtime behavior.

Suggested scope:
- `GITHUB_RELEASE.md`
- `GITHUB_RELEASE.en.md`
- `RELEASE_NOTES_v1.0.1_beta.md`
- `release/`
- `.github/`

Commit intent:
- freeze the public release story
- describe the repo as upstream base + bridge compatibility + external verification
- keep it explicit that `core` does not host runtime responsibilities

## Recommended Commit Order

1. Freeze Group 1: Core / Contract
2. Freeze Group 2: Skill Mirror
3. Freeze Group 3: Bridge / Binding
4. Freeze Group 4: Release / Snapshot

## Minimum Pre-Release Checks

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `npm run build` in `C:\\Users\\Y2516\\Desktop\\openharness_app_external_verify`
- `npm run smoke` in `C:\\Users\\Y2516\\Desktop\\openharness_app_external_verify`

## Release Judgment

The repository contents are close to publishable, but it is still not a good idea to publish directly from one large unsplit working tree.

The correct sequence is:
- split the work into the freeze groups above
- publish it under your own project identity
- contribute only narrow docs / examples / compatibility notes back to OpenHarness
