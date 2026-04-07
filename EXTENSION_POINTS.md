# Harness Tool Extension Points v1.0.1 beta

This file records the current boundaries and the next reasonable upgrade areas.

## Current Boundaries

- The repository is thin and Python-first.
- Validation runs `tests/smoke.py` and checks the contract files.
- `apply_harness.py` still relies on safe heuristics.
- Profile support is wired, but the rule files are intentionally small.
- The OpenClaw skill package mirrors the repository contract.
- OpenHarness compatibility stays in bridge and binding files, not in `harness_core`.

## Mounting Rule

- Extension mounting is not built into the core as a full runtime system.
- The repository keeps extension points explicit and gives users examples, not a heavy plugin platform.
- If a project needs richer mounting behavior, it should implement that locally on top of the contract.
- The current freeze does not allow new generic adapter expansion.

## Extension Point 1: Better Source Discovery

Next improvement:

- detect real entry points more accurately
- infer test files from the module layout
- reduce reliance on directory heuristics

## Extension Point 2: Richer Profile Rules

Next improvement:

- add more difference between profiles
- support project-specific required files and sections
- keep profiles lightweight, not policy-heavy

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


## Example-First Rule

- Treat extension examples as guidance, not as a hidden runtime dependency.
- Do not claim a mounting feature is available unless it is implemented and verified.
- Keep the core harness contract stable while allowing project-specific extension code outside the core.

## Local Example

- `examples/local_extension/README.md` shows the smallest project-owned mounting pattern.
- Use it as guidance, not as a hidden runtime dependency.

## OpenHarness Rule

- Keep OpenHarness integration bridge-side.
- Do not move provider, middleware, session, or runtime ownership into `core`.
- Treat external verification as evidence, not as a reason to widen the core contract.
