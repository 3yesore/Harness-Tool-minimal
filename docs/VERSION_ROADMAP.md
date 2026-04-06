# Harness Tool Version Roadmap

## Current Version

- `v1.0.1 beta`
- Status: beta freeze, ready for GitHub publication
- Focus: single-module maintenance, smoke-test validation, and OpenClaw skill packaging
- Homepage: defaults to the `v1.0.1 beta` README
- Historical anchor: `v1.0.0`

## What v1.0 Includes

- `HARNESS_SPEC.md`
- `tools/init_module.py`
- `tools/apply_harness.py`
- `tools/validate_module.py`
- `templates/`
- `profiles/`
- `examples/hello_world/`
- `.openclaw_skill/`

## Planned Direction

### v2.0 Fetcher

Goal: make the tool more adaptive for real projects.

Likely additions:
- better source-file discovery
- improved profile differentiation
- deeper module analysis
- broader template coverage

### v3.0 Intruder

Goal: support larger projects and stronger automation.

Likely additions:
- CI integration
- multi-module orchestration
- team workflow support
- audit-friendly reporting

## Release Policy

- Keep `v1.x` backwards compatible with the current module layout
- Keep the skill package synced with repository behavior
- Prefer incremental changes that can be validated with the example module

## Notes

- The roadmap describes intent, not committed functionality.
- If the implementation changes, update this file together with `INDEX.md` and `HARNESS_SPEC.md`.
