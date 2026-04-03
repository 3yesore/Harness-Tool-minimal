# Harness Tool Minimal

Harness Tool Minimal is the staging repository for a small Harness Engineering toolchain. It keeps module maintenance centered on `INDEX.md`, `SPEC.md`, a runnable smoke test, and a lightweight validation loop.

The repository is currently Python-first and is organized for GitHub publication after validation.

## What It Includes

- `tools/init_module.py` to create a new module skeleton
- `tools/apply_harness.py` to retrofit an existing module with Harness docs and a smoke test
- `tools/validate_module.py` to validate docs, configs, and smoke-test execution
- `templates/` for `INDEX.md`, `SPEC.md`, and `CHANGELOG.md`
- `profiles/` for validation and scaffolding presets
- `examples/hello_world/` as the reference module
- `.openclaw_skill/` as the packaged OpenClaw skill version of the same workflow

## Core Workflow

1. Read the module `INDEX.md`
2. Read the module `SPEC.md`
3. Make the smallest relevant code change
4. Run the smoke test
5. Run the validator
6. Update `CHANGELOG.md` when behavior changes

## Quick Start

### Create a new module

```bash
python tools/init_module.py my_module
```

### Retrofit an existing module

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

### Run the reference example

```bash
python examples/hello_world/tests/smoke.py
```

## Documentation

- [HARNESS_SPEC.en.md](HARNESS_SPEC.en.md) for the repository-level contract
- [INDEX.en.md](INDEX.en.md) for the repository map
- [GITHUB_RELEASE.en.md](GITHUB_RELEASE.en.md) for release preparation
- [VERSION_ROADMAP.en.md](VERSION_ROADMAP.en.md) for the roadmap
- [profiles/README.en.md](profiles/README.en.md) for profile status
- [.openclaw_skill/SKILL.md](.openclaw_skill/SKILL.md) for the packaged skill

## Current Status

- The validation loop is working
- The example module passes smoke testing
- The skill package is synced to the current implementation
- The repository is still the staging copy before GitHub publication

## Notes

- This repository is intentionally minimal.
- Profile rules are currently small and mostly mirror default behavior.
- `apply_harness.py` still uses heuristics rather than deep source parsing.
