# Profiles

Profiles are the lightweight preset layer for `v1.0.1 beta`.

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

## Rules

- keep profiles small
- keep profiles descriptive, not policy-heavy
- use profiles to express module-type differences, not to override the contract

## Freeze Rule

- keep profiles on the contract side, not the runtime side
- do not move OpenHarness bridge metadata into profiles
- do not turn profiles into a policy engine or integration registry
