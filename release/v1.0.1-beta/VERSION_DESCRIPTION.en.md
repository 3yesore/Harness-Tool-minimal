# v1.0.1 beta Version Description

## Version Name

- `Harness Tool Minimal v1.0.1 beta`

## One-Line Summary

- This is a release freeze focused on a thin core, a hard contract, and an OpenHarness-compatible bridge that stays outside `core`.

## Release Positioning

- `harness_tool` remains the upstream, contract-first base
- `harness_core` remains responsible only for protocol, validation, stages, and scaffold semantics
- OpenHarness-related work stays in the bridge / binding layer
- external verification is compatibility evidence, not runtime ownership

## Core Changes

### 1. Core / contract baseline frozen

- The top-level entry documents now share one protocol narrative:
  - `README.md`
  - `INDEX.md`
  - `HARNESS_SPEC.md`
- `CORE_PROTOCOL.md`, `ADAPTER_PROTOCOL.md`, and `EXTENSION_PROTOCOL.md` now define the three-layer boundary more explicitly
- `harness_core/` now serves as the unified contract layer instead of relying on scattered script semantics
- `init / apply / validate` continue to share one core model

### 2. Templates, rules, and examples aligned

- `templates/` now match the current contract headings and fields
- `profiles/` remain lightweight and preset-oriented
- `examples/hello_world/` remains the minimal contract example
- `examples/local_extension/` remains the project-local extension example

### 3. OpenClaw skill mirror aligned

- `.openclaw_skill/` remains a mirror, not an independent product surface
- mirror templates, rules, and scripts have been aligned with the current contract path

### 4. OpenHarness-compatible bridge completed

- A narrow OpenHarness bridge / binding path is now present:
  - `OPENHARNESS_BRIDGE.md`
  - `OPENHARNESS_SDK_BINDING.md`
  - `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `adapters/` and `scripts/openharness_*` remain bridge-side only
- `provider_hints` and `middleware_hints` remain bridge metadata, not core semantics

### 5. External verification completed

- The repository includes `examples/openharness_app/` as a minimal OpenHarness app example
- A repo-external verification app also exists at:
  - `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- Verified:
  - `Agent` instantiation
  - `Agent.run(...)` mock dry-run
  - `harness_validate` process transport

## External Commitments

- This version is suitable for release under your own project identity
- It provides:
  - a thin core
  - a hard contract
  - explicit extension boundaries
  - a verified OpenHarness-compatible bridge
- It does not provide:
  - a core-owned runtime
  - provider lifecycle ownership
  - middleware lifecycle ownership
  - deep session / conversation integration

## Validation Results

The following checks have passed in the current repository and the external verification app:

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `npm run build` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- `npm run smoke` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`

## Risk Notes

- The current OpenHarness integration remains a narrow bridge, not a full runtime integration
- Still intentionally deferred:
  - live provider wiring
  - live middleware wiring
  - non-process transport
  - session / conversation validation
  - real model invocation
- These are not hidden gaps; they remain open on purpose to keep `core` clean

## Scope Fit

- Suitable as the baseline release for your own repository
- Suitable for small projects, small modules, and contract-first engineering
- Suitable as an upstream base for future bridge / compatibility work
- Not suitable to describe as a full OpenHarness runtime integration

## Rollback Anchor

- `v1.0.0`

## Suggested Release Framing

- `Harness Tool Minimal v1.0.1 beta` is a freeze-and-tightening release, not a platform expansion release
- The current repository now has:
  - an upstream contract-first base
  - stable core/extension boundaries
  - an OpenHarness-compatible bridge
  - repo-external verification evidence
- If anything is contributed upstream to OpenHarness, the natural path is docs / example / compatibility notes rather than pushing the whole interface layer into their core
