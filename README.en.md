# Harness Tool Minimal

Harness Tool Minimal is a Harness Engineering toolkit for module maintenance.

It keeps `INDEX.md`, `SPEC.md`, `tests/smoke.py`, and the change log in a small verifiable handoff loop.

## Highlights

- Minimal loop: initialize, retrofit, validate, record
- Real execution: `validate_module.py` actually runs `tests/smoke.py`
- Bilingual docs: Chinese primary docs plus English mirrors
- Extensible: `profiles/`, `.openclaw_skill/`, and `templates/`
- Publication-ready: organized for GitHub syncing

## Quick Start

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

## Includes

- `tools/init_module.py` to create a module skeleton
- `tools/apply_harness.py` to retrofit an existing module
- `tools/validate_module.py` to validate docs, configs, and smoke tests
- `templates/` templates
- `profiles/` rule presets
- `examples/` reference examples
- `.openclaw_skill/` skill package for OpenClaw / Codex

## Examples

- `examples/hello_world`
- `examples/user_service`

## Install Skill

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

- [INDEX.md](INDEX.md)
- [HARNESS_SPEC.md](HARNESS_SPEC.md)
- [GITHUB_RELEASE.md](GITHUB_RELEASE.md)
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md)
- [README.md](README.md)

## Current Status

Testing stage, with more features and adapter support still being added. Feedback is welcome.
