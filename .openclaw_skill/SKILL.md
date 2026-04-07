---
name: harness
description: Apply Harness Engineering to make modules AI-maintainable. Use when creating new modules, retrofitting existing modules, validating module compliance, or keeping a module handoff-ready across sessions.
---

# Harness Engineering

Use this skill to keep module development contract-driven, index-first, and verifiable across handoff cycles.

## Frozen Protocol

The current beta baseline freezes the core around four primitives:

- `ModuleContext`
- `ContractRules`
- `ValidationResult`
- `ScaffoldPlan`

The workflow stages are also frozen:

- `Discovery`
- `Contract`
- `Validate`
- `Suggest`

## What This Skill Includes

- `scripts/init_harness_module.py`: create a new module skeleton
- `scripts/apply_harness.py`: retrofit an existing module with Harness docs and a smoke test
- `scripts/validate_harness.py`: validate docs, configs, markers, and smoke-test execution
- `templates/`: INDEX, SPEC, and CHANGELOG templates
- `profiles/`: rule presets used by the scripts

## Core Principles

1. Index-first: every maintained module should have `INDEX.md`
2. Contract-driven: `SPEC.md` should define inputs, outputs, config, markers, and errors
3. Minimal context: keep maintenance-critical details in a few files
4. Verifiable: every module should have a runnable smoke test
5. Handoff-ready: another maintainer should recover the module quickly from `INDEX.md`, `SPEC.md`, and the smoke test
6. Thin core, explicit extension: project-local overrides and markers stay outside `harness_core`

## Quick Reference

```bash
# Initialize new module
python scripts/init_harness_module.py my_module

# Apply Harness to existing module
python scripts/apply_harness.py existing_module

# Validate module compliance
python scripts/validate_harness.py my_module

# Validate with a profile
python scripts/validate_harness.py my_module --profile python-service

# Run module tests
python my_module/tests/smoke.py
```

## AI Workflow

1. Read `INDEX.md` and `SPEC.md`
2. Read only the code files needed for the task
3. Make the change
4. Run the smoke test
5. Run `validate_harness.py`
6. Update `CHANGELOG.md` when behavior changes

## Profile Support

Profiles are bundled with the skill and are consumed by the scripts through `--profile`.

- `default.rules.json`
- `python-service.rules.json`

Profiles stay lightweight and only tune the frozen contract.

## What You Get From Skill Only

If you only install this skill, you get the current Harness workflow, templates, profiles, and validation scripts packaged together. You do not get future repository-only changes unless the skill is updated again.

## References

- `references/index_template.md`
- `references/spec_template.md`
- `references/changelog_template.md`
- `references/harness_spec.md`
- `references/validation_rules.md`
