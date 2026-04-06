# Harness Tool Main Index

## Repository Overview

Harness Tool Minimal currently defaults to `v1.0.1 beta`. It is a lightweight Harness Engineering repository for module development and maintenance. It keeps responsibilities, interfaces, validation, and handoff details in a small set of fixed files so both humans and AI can pick up work quickly.

The current repository has a working minimal loop. Its core capabilities are:

- create a new module skeleton
- retrofit an existing module with Harness files
- validate module docs, configuration, and smoke tests
- use `profiles/` for lightweight rule presets
- package the same workflow as an OpenClaw / Codex skill
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
├── LICENSE
├── docs/
│  ├── README.md
│  ├── README.en.md
│  ├── AI_CHECKLIST.md
│  ├── AI_REPAIR_GUIDE.md
│  ├── CONTRIBUTING.md
│  ├── DESIGN_REVIEW.md
│  ├── FAQ.md
│  ├── GITHUB_PUBLISH_GUIDE.md
│  ├── RELEASE_NOTES_v1.0.md
│  ├── AI_OPERATIONS.md
│  ├── AI_OPERATIONS.en.md
│  ├── EXTENSION_POINTS.md
│  ├── EXTENSION_POINTS.en.md
│  └── ...
├── .github/
│  └── workflows/validate.yml
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
- `examples/local_extension/`: a local extension example that shows project-owned extensions

### Profiles

- `profiles/default.rules.json`
- `profiles/python-service.rules.json`
- `profiles/README.md`

### Automation and Skill

- `.github/workflows/validate.yml`
- `.openclaw_skill/SKILL.md`

### Supporting Docs

- [docs/README.en.md](docs/README.en.md): documentation hub

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

## Handoff Flow

1. Read the module's `INDEX.md`
2. Read the module's `SPEC.md`
3. Read only the code files needed for the task
4. Sync `SPEC.md` and `INDEX.md` when implementation changes
5. Keep `tests/smoke.py` up to date
6. Run `tools/validate_module.py <module_path>`
7. Update `CHANGELOG.md` when behavior changes

## Version Info

- Current version: `v1.0.1 beta`
- Spec version: `v1.0`
- Status: runnable, verifiable, and aligned with the default homepage
- Last updated: 2026-04-06
