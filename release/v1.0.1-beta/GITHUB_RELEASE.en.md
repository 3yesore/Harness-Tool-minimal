# Harness Tool Minimal v1.0.1 beta

`v1.0.1 beta` is the frozen baseline release of `Harness Tool Minimal`.

This release is not about turning the repository into a thicker platform. It is about freezing the structure that is already in place into one coherent story:

- `harness_tool` remains the upstream, contract-first base
- `harness_core` remains thin and owns only protocol, validation, stages, and scaffold semantics
- OpenHarness compatibility remains in the bridge / binding layer
- external verification remains compatibility evidence, not runtime ownership

## Highlights

- frozen core / contract baseline
- explicit `core / adapter / extension` boundaries
- aligned templates, rules, and examples
- synced OpenClaw skill mirror
- OpenHarness-compatible bridge and SDK binding
- repo-external OpenHarness app verification

## What This Release Means

This version is suitable as the baseline release of your own project. It already includes:

- an upstream contract-first narrative
- unified core protocol entry points
- stable extension and template boundaries
- a verified OpenHarness-compatible bridge

It should not be presented as:

- a full OpenHarness runtime integration
- provider / middleware lifecycle integration
- a session / conversation host runtime

## Verified Commands

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `npm run build` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- `npm run smoke` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`

## Notes

- This is a freeze-and-tightening release, not a platform-expansion release
- OpenHarness compatibility is still a narrow bridge
- `v1.0.0` remains the rollback anchor

For the full version description, see:

- [VERSION_DESCRIPTION.en.md](VERSION_DESCRIPTION.en.md)
- [PUBLISH_CHECKLIST.en.md](PUBLISH_CHECKLIST.en.md)
