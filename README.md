# Harness Tool

[English](README.md) | [中文](README.zh.md)

Contract-first engineering base with a thin core and a narrow OpenHarness bridge.

## What problem this project solves

Repositories usually fail in one of two ways:

- the core is too soft, so structure and validation drift
- the core is too heavy, so every integration pulls runtime logic into the base

Harness Tool exists to keep a stable middle line:

- explicit contract
- predictable validation
- bounded extension surfaces
- external runtime integration without turning the repository into a runtime host

## What it is

Harness Tool is:

- an upstream engineering base
- a contract-first repository structure
- a validation and scaffold toolset
- intended for module development, maintenance, handoff, and AI-assisted work

`harness_core` owns protocol, validation, stages, and scaffold semantics.

## What it is not

Harness Tool is not:

- a full agent runtime
- a workflow host
- a plugin platform
- an OpenHarness replacement
- a thick framework

## Architecture at a glance

The repository is split into three layers:

- `harness_core/`
  protocol, validation, stages, scaffold semantics
- extension surfaces
  `profiles/`, `templates/`, `.openclaw_skill/`, and local extensions
- bridge layer
  `adapters/`, `scripts/openharness_*`, and the OpenHarness examples

The contract stays in core. Variation stays outside core. External runtimes connect through bridges.

## Relationship to OpenHarness

OpenHarness is an external runtime. It is not owned by this repository’s core.

Harness Tool provides:

- project contract
- validation entrypoints
- module context
- boundary discipline

OpenHarness provides:

- agent runtime
- tools and providers
- middleware composition
- execution flow

Current support is real but narrow:

- bridge and binding documents
- `harness_validate` process transport
- context injection
- internal and external examples

This repository does not claim:

- runtime ownership in `harness_core`
- live provider wiring
- live middleware wiring
- full session or conversation integration

## Quick start

Initialize a module:

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
```

Validate the OpenHarness example:

```bash
python tools/validate_module.py examples/openharness_app --strict --profile default
```

## Repository layout

- `README.md`
  primary entrypoint
- `docs/`
  protocols, specs, integration docs, release notes
- `harness_core/`
  core implementation
- `tools/`
  init, apply, validate, repair entrypoints
- `examples/`
  reference modules and the OpenHarness example
- `adapters/`
  bridge-side integration code
- `release/`
  packaged release material

## Current scope and limitations

Current scope is intentionally narrow:

- OpenHarness support is bridge-side only
- `harness_core` does not host runtime responsibilities
- provider and middleware handling remain outside core
- full session and conversation integration is out of scope
- `examples/openharness_app` may skip npm smoke when local dependencies are absent

This repository is a usable engineering base and a real bridge source. It is not a complete runtime product.

## Documentation map

- [Core docs](docs/core/README.md)
- [Extension docs](docs/extensions/README.md)
- [OpenHarness integration](docs/integrations/openharness/README.md)
- [Operations notes](docs/operations/README.md)
- [Release notes](docs/releases/README.md)
