# Profiles

Profiles are wired into the CLI through `--profile`.

## Current Files

- `default.rules.json`
- `python-service.rules.json`

## What They Control

- required files
- recommended files
- required `INDEX.md` sections
- required `SPEC.md` sections
- recommended directories for scaffolding

## Current Behavior

- `tools/validate_module.py --profile <name>` loads `profiles/<name>.rules.json`
- `tools/apply_harness.py --profile <name>` loads the same rules and creates recommended directories
- if the named profile is missing, both scripts fall back to `default`

## Notes

- the current profiles are intentionally minimal
- they mostly mirror the default behavior right now
- this is the place to extend per-project presets later
