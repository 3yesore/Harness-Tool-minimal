# Harness Tool Minimal v1.0.1 beta

[![Validate](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml/badge.svg)](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.1-beta-blue.svg)](docs/VERSION_ROADMAP.en.md)

This is the repository homepage and the default beta baseline shown on GitHub.  
`v1.0.1 beta` is not a thick platform. It is a hardened minimal baseline with clearer contracts, clearer extension entrances, and enough room for project-level customization.

## What you get

- A minimal loop: initialize, retrofit, validate, record
- Real validation: `validate_module.py` actually runs `tests/smoke.py`
- Lightweight extension surfaces: `profiles/`, `templates/`, and `.openclaw_skill/`
- A handoff-friendly structure: `INDEX.md`, `SPEC.md`, and `CHANGELOG.md`
- Release resources: Chinese homepage, English mirror, display page, and upgrade checklist

## Best fit

- Small projects
- Small modules
- Early-stage development
- Projects that want AI-assisted maintenance with recoverable context

## Quick Start

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

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
- `examples/local_extension`

## Install the Skill

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
- [docs/VERSION_ROADMAP.en.md](docs/VERSION_ROADMAP.en.md)

## Historical Version

- `v1.0.0`: the initial minimal version, kept as the historical anchor

## Current Status

`v1.0.1 beta` is the default homepage version. Later expansion work, if any, should still flow back into the main line without breaking the minimal baseline.
