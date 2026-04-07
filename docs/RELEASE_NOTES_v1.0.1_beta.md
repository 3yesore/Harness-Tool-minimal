# Harness Tool Minimal v1.0.1 beta

## Summary

`v1.0.1 beta` is a freeze-and-tightening release.

It does not expand `harness_tool` into a thicker platform. It freezes the current contract-first baseline and keeps OpenHarness compatibility in a narrow bridge / binding layer.

## Included In This Release

- frozen `core / contract` baseline
- aligned top-level protocol docs
- aligned templates and profiles
- synced OpenClaw skill mirror
- OpenHarness-compatible bridge and SDK binding
- repo-external OpenHarness verification

## Boundary Statement

- `harness_tool` remains the upstream base
- `harness_core` remains thin
- OpenHarness support remains bridge-side
- provider / middleware details remain bridge metadata
- external verification is evidence, not runtime ownership

## Not Included

- full OpenHarness runtime integration
- live provider wiring
- live middleware wiring
- non-process transport
- session / conversation validation
- real model invocation

## Verified Checks

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `npm run build` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- `npm run smoke` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`

## Rollback Anchor

- `v1.0.0`
