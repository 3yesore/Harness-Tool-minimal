# Harness Tool Minimal

Harness Tool Minimal is a Harness Engineering toolkit for module maintenance.

It keeps `INDEX.md`, `SPEC.md`, `tests/smoke.py`, and the change log in a small verifiable handoff loop, which fits long-lived modules and projects that need AI to take over safely.

## Highlights

- Minimal loop: initialize, retrofit, validate, record
- Real execution: `validate_module.py` actually runs `tests/smoke.py`
- Bilingual docs: Chinese primary docs plus English mirrors
- Extensible: `profiles/`, `.openclaw_skill/`, and `templates/` are already in place
- Publication-ready: the repository is organized for GitHub syncing

## Good Fit For

- handing a module to AI for long-term maintenance
- retrofitting legacy code with a minimal maintainable structure
- keeping a fixed validation entry point after changes
- turning a module into something easier to hand off
- packaging the same skill for OpenClaw and Codex

## 3-Minute Start

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

## What It Includes

- `tools/init_module.py`: create a new module skeleton
- `tools/apply_harness.py`: retrofit an existing module with Harness
- `tools/validate_module.py`: validate docs, configs, and smoke tests
- `templates/`: templates
- `profiles/`: rule presets
- `examples/`: reference examples
- `.openclaw_skill/`: a skill package installable into OpenClaw or Codex

## Reference Examples

- `examples/hello_world`: the smallest verifiable example
- `examples/user_service`: a sample closer to a real project

## Skill Installation

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

## Next Steps

1. Read [INDEX.md](INDEX.md) for the repository map
2. Read [HARNESS_SPEC.md](HARNESS_SPEC.md) for the contract
3. Run `examples/hello_world/tests/smoke.py`
4. Run `python tools/validate_module.py examples/hello_world --strict --profile python-service`
