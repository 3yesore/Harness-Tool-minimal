# Harness Tool Extension Points

This file records the current boundaries and the next reasonable upgrade areas.

## Current Boundaries

- The repository is Python-first.
- Validation currently runs `tests/smoke.py`.
- `apply_harness.py` still relies on heuristics.
- Profile support is wired, but the rule files are intentionally small.
- The OpenClaw skill package mirrors the current repository behavior.

## Extension Point 1: Better Source Discovery

Next improvement:
- detect real entry points more accurately
- infer test files from the module layout
- reduce reliance on directory heuristics

## Extension Point 2: Richer Profile Rules

Next improvement:
- add more difference between profiles
- support project-specific required files and sections
- make recommendations more useful for real modules

## Extension Point 3: Cross-Language Support

Next improvement:
- add language-specific templates
- add non-Python smoke-test paths
- keep the same Harness contract across languages

## Extension Point 4: Machine-Readable Reporting

Next improvement:
- emit structured validation output for CI or dashboards
- keep the current CLI simple while adding an optional report mode later

## Extension Point 5: Repository-Level Automation

Next improvement:
- expand GitHub Actions coverage
- validate more than the reference example
- keep the workflow aligned with the skill package

## Release Rule

Do not describe a feature as available unless it is implemented in the scripts and verified against the example module.
