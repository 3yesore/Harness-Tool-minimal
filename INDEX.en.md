# Harness Tool Index

## Repository Overview

`Harness Tool Minimal` is a `harness kernel` repository for the full module development and maintenance lifecycle. It is not a thick framework or a package manager. It concentrates responsibilities, interfaces, validation, and handoff details into a small set of fixed files so people and AI stay aligned across development, integration, evolution, and maintenance.

The repository is frozen at the `v1.0.1 beta` baseline. The principles are:

- `core` stays mechanism-only
- `contract` defines legality
- `adapter` translates external integration
- `extension` provides default presets and templates
- `override` allows local customization without breaking the contract

## Protocol Map

- [CORE_PROTOCOL.md](CORE_PROTOCOL.md): frozen core envelope and workflow stages
- [ADAPTER_PROTOCOL.md](ADAPTER_PROTOCOL.md): minimal external integration envelope
- [EXTENSION_PROTOCOL.md](EXTENSION_PROTOCOL.md): project-local extension boundaries
- [adapters/README.md](adapters/README.md): adapter workspace entry
- [docs/OPEN_ITEMS.en.md](docs/OPEN_ITEMS.en.md): intentionally unfinished upgrade items
- [docs/WORK_INDEX.en.md](docs/WORK_INDEX.en.md): organization-order index
- [docs/CURRENT_CHANGESET_INDEX.en.md](docs/CURRENT_CHANGESET_INDEX.en.md): final cleanup index for the current changeset

## Three Layers

### 1. Core
Only mechanisms, contracts, validation, and scaffold plans.

### 2. Adapter
Translates OS / multi-agent / external project differences into standard inputs.

### 3. Extension
Keeps `profiles / templates / marker / override` available for project-local differences.

## Core Files

### Specification and versioning
- [HARNESS_SPEC.md](HARNESS_SPEC.md): repository contract and boundary rules
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md): version roadmap and freeze policy
- [DESIGN_REVIEW.md](DESIGN_REVIEW.md): whitelist, blacklist, and performance floor
- [AI_CHECKLIST.md](AI_CHECKLIST.md): AI handoff checklist
- [GITHUB_RELEASE.md](GITHUB_RELEASE.md): release entry point
- [RELEASE_NOTES_v1.0.1_beta.md](RELEASE_NOTES_v1.0.1_beta.md): current beta freeze note

### Protocol files
- [CORE_PROTOCOL.md](CORE_PROTOCOL.md): core protocol envelope
- [ADAPTER_PROTOCOL.md](ADAPTER_PROTOCOL.md): adapter protocol envelope
- [EXTENSION_PROTOCOL.md](EXTENSION_PROTOCOL.md): extension protocol envelope

### Tools
- [tools/init_module.py](tools/init_module.py): create a new module scaffold
- [tools/apply_harness.py](tools/apply_harness.py): add Harness structure to existing modules
- [tools/validate_module.py](tools/validate_module.py): validate docs, configs, and smoke tests

## Extension Surface

- `templates/`: default skeletons, only safe starting points
- `profiles/`: lightweight presets for module-type differences
- `adapters/`: adapter workspace for external integration envelopes
- `.openclaw_skill/`: mirrored OpenClaw skill bundle
- `examples/local_extension/`: local extension example

## Version Information

- Current version: `v1.0.1 beta`
- Baseline type: thin core, hard contract, large extension space
- Status: independently frozen baseline
- Rollback anchor: `v1.0.0`

## Development Entry

This repository guidance is available from two aligned paths:

- Document entry: [`harness_core/BOUNDARIES.md`](harness_core/BOUNDARIES.md)
- Programmatic entry: `harness_core.describe_development_guidance()`

In particular:

- `core.py` explains how the core boundary is frozen
- `markers.py` explains how key paths, variables, and coupling are marked
- `rendering.py` explains how those markers are rendered into `INDEX.md` / `SPEC.md`
- `validate_module.py` explains how those markers are validated
- `describe_extension_guidance()` explains how the extension layer stays bounded
- `describe_adapter_protocol()` explains the adapter envelope

## Open Items

The following are intentionally left open for later upgrades:

- concrete adapter samples under `adapters/`
- richer OS / multi-agent / external project integration demos
- a fuller adapter validation matrix
- more versioned profile/template pack rules

These are kept as docs and examples first, not folded into a thick platform.

## OpenHarness Bridge

- [OPENHARNESS_BRIDGE.md](OPENHARNESS_BRIDGE.md)
- [OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.en.md](OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.en.md)
- [OPENHARNESS_SDK_BINDING.en.md](OPENHARNESS_SDK_BINDING.en.md)
- [docs/OPENHARNESS_EXTERNAL_VERIFY.en.md](docs/OPENHARNESS_EXTERNAL_VERIFY.en.md)
- [docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.en.md](docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.en.md)
- [docs/OPENHARNESS_BRIDGE_INDEX.en.md](docs/OPENHARNESS_BRIDGE_INDEX.en.md)

## OpenHarness External Verification

- external verify repo: `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- verified: `@openharness/core@0.6.0` `Agent` instantiation
- verified: `Agent.run(...)` dry-run with a local mock model
- verified: `harness_validate` process transport from an external OpenHarness app
- verified: `provider_hints` / `middleware_hints` remain bridge-only metadata
