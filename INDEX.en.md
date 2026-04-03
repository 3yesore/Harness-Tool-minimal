# Harness Tool Main Index

## Repository Overview

Harness Tool Minimal is a lightweight Harness Engineering repository for module maintenance. It is designed to keep responsibilities, interfaces, validation, and handoff details in a small set of fixed files.

The current repository is a working minimal loop. Its core capabilities are:

- create a new module skeleton
- retrofit an existing module with Harness files
- validate module docs, configuration, and smoke tests
- use `profiles/` for lightweight rule presets
- package the same workflow as an OpenClaw skill
- run basic GitHub Actions validation

## Repository Layout

```text
harness_tool/
├── README.md
├── README.en.md
├── HARNESS_SPEC.md
├── HARNESS_SPEC.en.md
├── INDEX.md
├── INDEX.en.md
├── VERSION_ROADMAP.md
├── VERSION_ROADMAP.en.md
├── GITHUB_RELEASE.md
├── GITHUB_RELEASE.en.md
├── RELEASE_NOTES_v1.0.md
├── LICENSE
├── .gitignore
├── .github/
│   └── workflows/validate.yml
├── templates/
├── tools/
├── examples/
├── profiles/
└── .openclaw_skill/
```

## Key Files

### Guidance

- [HARNESS_SPEC.en.md](HARNESS_SPEC.en.md): repository-level Harness specification
- [VERSION_ROADMAP.en.md](VERSION_ROADMAP.en.md): version plan
- [GITHUB_RELEASE.en.md](GITHUB_RELEASE.en.md): GitHub release checklist
- [RELEASE_NOTES_v1.0.md](RELEASE_NOTES_v1.0.md): current release notes

### Tools

- [tools/init_module.py](tools/init_module.py): create a module skeleton
- [tools/apply_harness.py](tools/apply_harness.py): retrofit an existing module
- [tools/validate_module.py](tools/validate_module.py): validate structure and smoke tests

### Templates

- `templates/INDEX.md.template`
- `templates/SPEC.md.template`
- `templates/CHANGELOG.md.template`

### Examples

- `examples/hello_world/`: the smallest reference module
- `examples/user_service/`: a more complex sample with multiple files and configs

### Profiles

- `profiles/default.rules.json`
- `profiles/python-service.rules.json`
- `profiles/README.md`

### Automation and Skill

- `.github/workflows/validate.yml`
- `.openclaw_skill/SKILL.md`

## Quick Start

### Create a new module

```bash
python tools/init_module.py <module_name> [--path <output_dir>]
```

### Apply Harness to an existing module

```bash
python tools/apply_harness.py <module_path>
python tools/apply_harness.py <module_path> --profile python-service
```

### Validate a module

```bash
python tools/validate_module.py <module_path>
python tools/validate_module.py <module_path> --strict
python tools/validate_module.py <module_path> --strict --profile python-service
```

### Run the examples

```bash
python examples/hello_world/tests/smoke.py
python examples/user_service/tests/smoke.py
```

## Current Status

- Module initialization works
- Module retrofit works
- Module validation works
- The OpenClaw skill package is synced
- GitHub Actions validation is available

## Version Info

- Current version: `v1.0.0 Minimal`
- Spec version: `v1.0`
- Status: runnable, verifiable, and ready for publication cleanup
