# Harness Specification v1.0.1 beta

## Goal

`Harness Tool Minimal` is a `harness kernel`, not a thick platform. Its job is to collect responsibilities, interfaces, validation, and handoff information into a small set of fixed files so people and AI stay aligned during development, integration, evolution, and maintenance.

## Four Layers

### 1. Core
`core` only handles mechanisms, not project business semantics.

`core` freezes:
- `ModuleContext`
- `ContractRules`
- `ValidationResult`
- `ScaffoldPlan`
- `Discovery -> Contract -> Validate -> Suggest`

`core` does not handle:
- OS runtime integration
- multi-agent scheduling
- external project translation
- thick platform behavior

### 2. Adapter
`adapter` is the outer translation layer for external integration.

`adapter` freezes:
- `name`
- `version`
- `type`
- `scope`
- `entrypoint`
- `capabilities`
- `protocol_version`
- `required_core_version`

`adapter` supports:
- `discover()`
- `attach()`
- `adapt()`
- `execute()`
- `teardown()`

`adapter` outputs:
- `adapted_context`
- `capability_report`
- `warnings`
- `errors`

`adapter` does not:
- decide module legality
- replace `core contract`
- swallow `extension` protocol
- become a thick platform

### 3. Extension
`extension` handles local differences without breaking the contract.

It includes:
- `profiles`
- `templates`
- `marker`
- `override`

It may soften:
- default values
- wording
- presets
- local wrappers
- directory preferences

It may not:
- bypass `validate`
- change protocol field meaning
- break `core contract`
- masquerade as `core`

### 4. Override
`override` only changes local defaults; it may not break boundaries.

## Workflow Stages

Freeze these four stages:
- `Discovery`
- `Contract`
- `Validate`
- `Suggest`

Meaning:
- `Discovery` discovers structure
- `Contract` validates docs, markers, and entry consistency
- `Validate` runs smoke tests, config checks, and recommended checks
- `Suggest` emits gaps, extension advice, and patch drafts

## Minimum Contract Shape

A module should at least have:
- `INDEX.md`
- `SPEC.md`
- `tests/smoke.py`
- `CHANGELOG.md`

Recommended:
- `configs/default.json`
- `src/main.py`
- extra marker guidance

## Protocol Map

Repository-level guidance stays aligned through:
- Document entry: [`harness_core/BOUNDARIES.md`](harness_core/BOUNDARIES.md)
- Extension entry: [`harness_core/EXTENSIONS.md`](harness_core/EXTENSIONS.md)
- Protocol files:
  - [`CORE_PROTOCOL.md`](CORE_PROTOCOL.md)
  - [`ADAPTER_PROTOCOL.md`](ADAPTER_PROTOCOL.md)
  - [`EXTENSION_PROTOCOL.md`](EXTENSION_PROTOCOL.md)

## Minimum Validation Gate

### Must check
- required files exist
- required sections exist
- entry exists
- marker core keys exist
- smoke tests are runnable
- config files parse

### Soft hints
- marker wording
- template layout preferences
- profile default values
- local wrapper shape
- directory preferences

## Open Items

Keep these as docs and samples for now, not part of `core`:
- concrete adapter examples under `adapters/`
- OS / multi-agent / external project demos
- a fuller adapter validation matrix
- more versioned pack rules

## Version Principle

- `v1.0.1 beta` is an independently frozen baseline
- older versions remain historical references
- future extensions must respect the current contract
- default stays `soft`, but the soft rules are built on frozen protocol, not on ad hoc documentation

## OpenHarness External Verification

The current bridge / SDK binding has been re-checked in a repo-external
OpenHarness app:

- `Agent` instantiation passes
- `Agent.run(...)` mock dry-run passes
- `harness_validate` process transport passes
- `provider_hints` / `middleware_hints` remain bridge contract data and do not enter `core`
