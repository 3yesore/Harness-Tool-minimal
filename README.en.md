# Harness Tool Minimal

[![Validate](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml/badge.svg)](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](docs/VERSION_ROADMAP.md)

A minimal Harness Engineering toolkit for module maintenance.

It brings module entry points, specs, smoke tests, and change records into one verifiable handoff flow. It fits both staging cleanup and lightweight module onboarding.

## What you get

- A minimal loop: initialize, retrofit, validate, record
- Real validation: `validate_module.py` actually runs `tests/smoke.py`
- Extensible structure: `profiles/`, `.openclaw_skill/`, and `templates/`
- A release-friendly layout: Chinese primary docs, English mirrors, and GitHub Actions checks

## Quick Start

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

## Who it is for

- People who want a module to be handoff-friendly and verifiable
- People who need `INDEX.md`, `SPEC.md`, and `CHANGELOG.md` in an existing project
- People who want the same workflow available in OpenClaw and Codex

## What is included

- `tools/init_module.py` to create a module skeleton
- `tools/apply_harness.py` to retrofit an existing module
- `tools/validate_module.py` to validate docs, configs, and smoke tests
- `templates/` for document templates
- `profiles/` for rule presets
- `examples/` for reference modules
- `.openclaw_skill/` as the skill package for OpenClaw and Codex

## Examples

- `examples/hello_world`
- `examples/user_service`

## Install the Skill

### Online Download

- [Download the skill ZIP](https://github.com/3yesore/Harness-Tool-minimal/archive/refs/heads/main.zip)
- Or use `Code` -> `Download ZIP` on the GitHub repository page

After downloading, unzip it and copy the `.openclaw_skill` directory into your local skill directory.
If your skill manager supports name-based install, you can also publish the package there and install it by name.

### OpenClaw

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.openclaw\skills" | Out-Null
Copy-Item -Recurse -Force ".openclaw_skill" "$env:USERPROFILE\.openclaw\skills\harness"
```

### Codex / VS Code

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".openclaw_skill" "$env:USERPROFILE\.codex\skills\harness"
```

## Documentation

- [docs/README.en.md](docs/README.en.md)
- [README.md](README.md)

## Current Status

Testing stage, with more features and adapter support still being added. Feedback is welcome.
