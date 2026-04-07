# GitHub Release Guide

This file defines the repository-level release wording. It does not replace the `release/v1.0.1-beta/` package.

## Unified Release Story For v1.0.1 beta

`Harness Tool Minimal v1.0.1 beta` should be released with this story:

- `harness_tool` is the upstream, contract-first base
- `harness_core` owns only protocol, validation, stages, and scaffold semantics
- OpenHarness compatibility stays in the bridge / binding layer
- external verification proves compatibility, not runtime ownership

## What This Release Can Claim

- the core / contract baseline is frozen
- templates, profiles, examples, and the OpenClaw skill mirror are aligned
- an OpenHarness-compatible bridge / binding path exists
- a repo-external OpenHarness app verification path exists

## What This Release Must Not Claim

- no full OpenHarness runtime integration
- no live provider wiring
- no live middleware wiring
- no `harness_core` runtime ownership

## Suggested Release Summary

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

## Pre-Release Checks

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python tools/validate_module.py examples/local_extension --strict --profile default
python tools/validate_module.py examples/openharness_app --strict --profile default
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
```

External OpenHarness verification:

```bash
cd C:/Users/Y2516/Desktop/openharness_app_external_verify
npm run build
npm run smoke
```

## Release Sequence

1. finish the freeze-group commits
2. tag `v1.0.1-beta`
3. publish the release package
4. if anything is contributed upstream to OpenHarness later, keep it narrow: docs, examples, and compatibility notes
