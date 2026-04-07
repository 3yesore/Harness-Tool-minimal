# Harness Tool

[English](README.md) | [中文](README.zh.md)

Contract-first engineering base with a thin core and an OpenHarness-compatible bridge.

## Why this project exists

Repositories usually fail in one of two ways:

- the core is too soft, so structure and validation drift over time
- the core is too heavy, so every integration pulls more runtime logic into the base

Harness Tool exists to hold a stricter middle line:

- keep the core small
- make the contract explicit
- let extensions vary without redefining the base
- connect external runtimes through a bridge instead of absorbing them into core

## What it is

Harness Tool is:

- an upstream engineering base
- a contract-first repository structure
- a validation, scaffold, and project-boundary toolset
- intended for module development, maintenance, handoff, and AI-assisted work

In this repository, `harness_core` owns protocol, validation, stages, and scaffold semantics.

## What it is not

Harness Tool is not:

- a full agent runtime
- a workflow host
- a plugin platform
- an OpenHarness-owned integration layer
- a thick framework that absorbs project-specific runtime behavior

## Architecture at a glance

The repository is split into three layers.

- `harness_core/`
  Protocol, validation, stages, and scaffold semantics.
- extension surfaces
  `profiles/`, `templates/`, `.openclaw_skill/`, and local extensions such as `examples/local_extension/`.
- bridge layer
  `adapters/`, `scripts/openharness_*`, and the OpenHarness examples.

The design intent is simple: keep the contract stable, keep local variation outside core, and connect external runtimes through a narrow bridge.

## Relationship to OpenHarness

OpenHarness is an external runtime. This repository does not own it and does not host its runtime responsibilities in `harness_core`.

Current integration is bridge-side and includes:

- bridge and binding documents
- transport-based validation calls
- context injection
- OpenHarness-oriented examples
- external verification material

This repository supports:

- OpenHarness-compatible bridge and binding
- `harness_validate` through a process transport
- context and skill-style injection material
- runtime-side registration examples outside core

This repository does not claim:

- full OpenHarness runtime ownership
- live provider wiring in core
- live middleware wiring in core
- full session or conversation integration
- a complete agent platform inside this repository

## Quick start

Initialize a new module:

```bash
python tools/init_module.py my_module
```

Apply Harness Tool to an existing module:

```bash
python tools/apply_harness.py path/to/module
python tools/apply_harness.py path/to/module --profile python-service
```

Validate a module:

```bash
python tools/validate_module.py path/to/module
python tools/validate_module.py path/to/module --strict
python tools/validate_module.py path/to/module --strict --profile python-service
```

Validate the OpenHarness example:

```bash
python tools/validate_module.py examples/openharness_app --strict --profile default
```

For the external verification path, see [OPENHARNESS_EXTERNAL_VERIFY](docs/OPENHARNESS_EXTERNAL_VERIFY.md).

## Repository layout

- root entrypoints
  `README.md`, `README.zh.md`, `README.en.md`.
- `docs/`
  repository docs, protocols, release notes, work indexes, and OpenHarness bridge material.
- `harness_core/`
  shared protocol and validation implementation.
- `tools/`
  module initialization, harness application, validation, and repair entrypoints.
- `examples/`
  baseline examples, local extension examples, and the OpenHarness example app.
- `adapters/`
  bridge-side protocol and OpenHarness integration surface.
- `release/`
  packaged release materials and publishing artifacts.

## Current scope and limitations

Current scope is intentionally narrow:

- OpenHarness support is bridge-side only
- `harness_core` does not own runtime responsibilities
- provider and middleware support are documented as bridge metadata, not live core wiring
- full session and conversation integration is out of scope
- `examples/openharness_app` may skip npm-based smoke when local dependencies are absent

This repository is usable as an engineering base and as a bridge source. It should not be described as a complete runtime product.

## Where to read more

- [Repository index](docs/INDEX.md)
- [Harness spec](docs/HARNESS_SPEC.md)
- [Core protocol](docs/CORE_PROTOCOL.md)
- [Adapter protocol](docs/ADAPTER_PROTOCOL.md)
- [Extension protocol](docs/EXTENSION_PROTOCOL.md)
- [OpenHarness bridge](docs/OPENHARNESS_BRIDGE.md)
- [OpenHarness SDK binding](docs/OPENHARNESS_SDK_BINDING.md)
- [GitHub release notes](docs/GITHUB_RELEASE.md)
