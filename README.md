# Harness Tool 1.0.1

[English](README.md) | [中文](README.zh.md)

`Harness Tool 1.0.1` is a **contract-first engineering base** for module development, maintenance, handoff, and AI-assisted work.

Its goal is not to turn the repository into a thick platform. Its goal is to keep module responsibilities, interfaces, validation, critical boundaries, and handoff information inside a small set of fixed entrypoints so both humans and AI can work against the same constraints.

This release is about four things:

- making `core` hard
- making the `contract` explicit
- keeping extension boundaries outside the core
- providing a real, verified OpenHarness-compatible bridge

## Positioning

`Harness Tool` acts as the **upstream base** in this architecture.

- `harness_core` owns protocol, validation, stages, and scaffold semantics
- `profiles / templates / markers / overrides` own project-side variation
- OpenHarness enters as an external runtime and stays outside `core`

So the main design is:

> stabilize project structure and contract first, then connect external agent runtime through a bridge

not:

> turn `Harness Tool` into a runtime host

## Why It Exists

Many repositories fail in one of two ways:

- the core is too soft, so extensions drift and maintenance gets noisy
- the core is too thick, so every new integration makes the system heavier

`Harness Tool 1.0.1` is built around a stricter middle line:

- **thin core**
- **hard contract**
- **explicit extension boundaries**
- **project-owned customization**
- **bridge-side external integration**

## What You Get

### Contract-first baseline

The repository uses fixed entrypoints to express what a module is, how it is validated, and which boundaries cannot be broken:

- `INDEX.md`
- `SPEC.md`
- `CHANGELOG.md`
- `validate`
- `marker`

### Thin but hard core

`harness_core` keeps the mechanism layer only. It does not host external runtime behavior and it does not absorb project-private semantics.

The current protocol skeleton is defined by:

- `docs/CORE_PROTOCOL.md`
- `docs/ADAPTER_PROTOCOL.md`
- `docs/EXTENSION_PROTOCOL.md`

### Controlled extension space

Extensions are allowed to grow, but only outside the core boundary:

- `profiles/`
- `templates/`
- `adapters/`
- `.openclaw_skill/`
- `examples/local_extension/`

### Verified OpenHarness compatibility path

This version includes a real OpenHarness-compatible bridge, not just a conceptual claim.

## Recommended Pairing: OpenHarness

If your goal is:

- to keep a stable project contract
- and then attach an agent runtime for execution, tool use, and workflow composition

then **using `Harness Tool 1.0.1` together with OpenHarness is recommended**.

The split is intentional:

### Harness Tool

Owns:

- engineering contract
- module structure
- validation entrypoints
- boundary discipline
- handoff and maintenance baseline

### OpenHarness

Owns:

- agent runtime
- tools / providers
- middleware composition
- execution flow
- external runtime behavior

### Why this pairing is practical

`Harness Tool` is stronger as the upstream engineering base because it stabilizes project meaning.  
OpenHarness is stronger as the downstream runtime because it executes agents.

So the recommended model is:

> `Harness Tool` defines the project structure and contract, and OpenHarness consumes that structure to act on the project.

## OpenHarness Support In 1.0.1

The current version already includes:

- OpenHarness bridge documentation
- SDK binding documentation
- `harness_validate` process transport
- a repo-internal OpenHarness example
- a repo-external OpenHarness verification app
- a runtime-side registration example
- a provider / middleware bridge-side metadata contract

Relevant entrypoints:

- [OPENHARNESS_BRIDGE.md](docs/OPENHARNESS_BRIDGE.md)
- [OPENHARNESS_SDK_BINDING.md](docs/OPENHARNESS_SDK_BINDING.md)
- [OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md](docs/OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md)
- [docs/OPENHARNESS_EXTERNAL_VERIFY.md](docs/OPENHARNESS_EXTERNAL_VERIFY.md)
- [docs/OPENHARNESS_BRIDGE_INDEX.md](docs/OPENHARNESS_BRIDGE_INDEX.md)

### What this version supports

- narrow bridge / binding
- context injection
- transport-based validation calls
- repo-external compatibility verification

### What this version does not claim

- no full OpenHarness runtime integration
- no live provider wiring
- no live middleware wiring
- no session / conversation integration
- no `harness_core` runtime ownership

That is a deliberate boundary, not hidden incompleteness.

## Repository Layout

### Core

- `harness_core/`
- `tools/`

### Docs

- `docs/CORE_PROTOCOL.md`
- `docs/ADAPTER_PROTOCOL.md`
- `docs/EXTENSION_PROTOCOL.md`
- `docs/INDEX.md`
- `docs/HARNESS_SPEC.md`
- `docs/VERSION_ROADMAP.md`
- `docs/DESIGN_REVIEW.md`
- `docs/AI_CHECKLIST.md`
- `docs/AI_OPERATIONS.md`

### Extensions

- `profiles/`
- `templates/`
- `.openclaw_skill/`
- `examples/local_extension/`

### OpenHarness bridge

- `adapters/`
- `scripts/openharness_*`
- `examples/openharness_app/`
- `docs/OPENHARNESS_*.md`

### Release

- `docs/GITHUB_RELEASE.md`
- `docs/RELEASE_NOTES_v1.0.1_beta.md`
- `release/v1.0.1-beta/`

## Quick Start

### Initialize a new module

```bash
python tools/init_module.py my_module
```

### Add Harness to an existing module

```bash
python tools/apply_harness.py path/to/module
python tools/apply_harness.py path/to/module --profile python-service
```

### Validate a module

```bash
python tools/validate_module.py path/to/module
python tools/validate_module.py path/to/module --strict
python tools/validate_module.py path/to/module --strict --profile python-service
```

### Run built-in examples

```bash
python examples/hello_world/tests/smoke.py
python examples/local_extension/harness/run_harness.py
```

### OpenHarness-compatible example

```bash
python tools/validate_module.py examples/openharness_app --strict --profile default
```

External verification:

```bash
cd C:/Users/Y2516/Desktop/openharness_app_external_verify
npm run build
npm run smoke
```

## Verified Checks

The current repository passes:

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`

The external OpenHarness app passes:

- `npm run build`
- `npm run smoke`

## Release Statement

`Harness Tool 1.0.1` is a freeze-and-tightening release, not a platform-expansion release.

It is accurate to describe it as:

- an independent upstream engineering base
- a contract-first module framework
- a repository with a real OpenHarness-compatible bridge

It should still be described carefully:

> **stable as a core, usable as a bridge, intentionally not a runtime host**

## Release Entry

- [GITHUB_RELEASE.md](docs/GITHUB_RELEASE.md)
- [RELEASE_NOTES_v1.0.1_beta.md](docs/RELEASE_NOTES_v1.0.1_beta.md)
- [release/v1.0.1-beta/README.md](release/v1.0.1-beta/README.md)
- [release/v1.0.1-beta/VERSION_DESCRIPTION.en.md](release/v1.0.1-beta/VERSION_DESCRIPTION.en.md)
- [release/v1.0.1-beta/PUBLISH_CHECKLIST.en.md](release/v1.0.1-beta/PUBLISH_CHECKLIST.en.md)

## Cleanup And Freeze Entry

- [docs/CURRENT_CHANGESET_INDEX.md](docs/CURRENT_CHANGESET_INDEX.md)
- [docs/FREEZE_GROUPS.md](docs/FREEZE_GROUPS.md)
- [docs/STAGED_COMMIT_PLAN.md](docs/STAGED_COMMIT_PLAN.md)
- [docs/WORK_INDEX.md](docs/WORK_INDEX.md)
