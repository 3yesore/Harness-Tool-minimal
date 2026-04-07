# Current Changeset Index

## Purpose
This index groups the current working changes by responsibility so the final
cleanup can be done without mixing `core`, bridge, and support files.

## Core / Contract Path
These files are still part of the main `harness_tool` contract path:

- `README.md`
- `INDEX.md`
- `HARNESS_SPEC.md`
- `AI_CHECKLIST.md`
- `AI_OPERATIONS.md`
- `DESIGN_REVIEW.md`
- `EXTENSION_POINTS.md`
- `GITHUB_RELEASE.md`
- `VERSION_ROADMAP.md`
- `profiles/default.rules.json`
- `profiles/python-service.rules.json`
- `profiles/README.md`
- `templates/INDEX.md.template`
- `templates/SPEC.md.template`
- `templates/CHANGELOG.md.template`
- `tools/init_module.py`
- `tools/apply_harness.py`
- `tools/validate_module.py`
- `tools/fix_module.py`
- `examples/hello_world/INDEX.md`
- `examples/hello_world/SPEC.md`

## OpenClaw Skill Mirror
These files mirror the main contract path for skill-side reuse:

- `.openclaw_skill/SKILL.md`
- `.openclaw_skill/references/harness_spec.md`
- `.openclaw_skill/references/index_template.md`
- `.openclaw_skill/references/spec_template.md`
- `.openclaw_skill/references/validation_rules.md`
- `.openclaw_skill/scripts/init_harness_module.py`
- `.openclaw_skill/scripts/validate_harness.py`

## Bridge / Binding / External Runtime Path
These files extend `harness_tool` outward to OpenHarness without changing
`harness_core` semantics:

- `ADAPTER_PROTOCOL.md`
- `OPENHARNESS_BRIDGE.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `OPENHARNESS_SDK_BINDING.md`
- `adapters/`
- `scripts/openharness_validate_transport.py`
- `scripts/openharness_sdk_binding_export.py`
- `examples/local_extension/`
- `examples/openharness_app/`
- `docs/OPENHARNESS_*.md`

## Release / Snapshot Path
These files describe the published baseline rather than bridge behavior:

- `release/`
- `RELEASE_NOTES_v1.0.1_beta.md`

## Practical Cleanup Order
1. Freeze the core / contract path first.
2. Keep the OpenClaw mirror aligned with the frozen contract path.
3. Freeze bridge and binding docs only after the core path stops moving.
4. Treat external-runtime files as integration artifacts, not core protocol.
5. Only then prepare release-facing notes.

## Current Direction Check
- `harness_tool` still acts as upstream and contract-first.
- OpenHarness integration remains bridge-side and external-runtime-facing.
- Provider and middleware details remain outside `harness_core`.
- No current bridge file should be promoted into `core` without a separate protocol decision.
