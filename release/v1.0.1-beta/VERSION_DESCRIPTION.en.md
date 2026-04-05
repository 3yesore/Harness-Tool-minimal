# v1.0.1 beta Version Description

## Version Name

- `Harness Tool Minimal v1.0.1 beta`

## One-Line Summary

- This beta release hardens the minimal baseline, keeps the smallest complete Harness workflow stable, and makes the standard entry points and extension boundaries clearer.

## Core Changes

- Keep the minimal `init / apply / validate` loop so module onboarding, validation, and handoff stay consistent.
- Keep `INDEX.md`, `SPEC.md`, `CHANGELOG.md`, and `tests/smoke.py` as the minimal handoff structure.
- Keep `profiles/`, `templates/`, and `.openclaw_skill/` as lightweight extension surfaces rather than a heavy platform.
- Continue using GitHub Actions for baseline validation.
- Keep the Chinese primary homepage and English mirror format for release and distribution.

## External Commitments

- This release is best suited for small projects, small modules, and early-stage development.
- It provides the smallest complete Harness workflow, not a large all-in-one platform.
- Users can continue to apply project-level customization while still respecting the minimal contract.
- Larger structures and stronger automation may be evaluated later based on real testing and feedback.

## Validation Results

The following commands have passed in the repository:

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py`

## Risk Notes

- The current extension surfaces are intentionally lightweight. They are meant for project-level conventions, not for a shared runtime plugin platform.
- The release stays minimal on purpose, so the core will not be expanded into a thick framework.
- For larger codebases, combine `profiles/`, `templates/`, and the existing examples for step-by-step customization rather than expecting this release to cover every enterprise scenario.

## Rollback Anchor

- `v1.0.0`

## Accuracy Confirmation

The following facts are already verified in the repository and are safe to include in the final release description:

- The repository currently covers module initialization, applying Harness structure to existing modules, and validating docs plus smoke tests.
- `examples/hello_world` and `examples/user_service` are present as reference examples.
- `profiles/`, `templates/`, and `.openclaw_skill/` are available and remain the primary extension and distribution surfaces.
- `v1.0.0` is the historical anchor, and `v1.0.1 beta` is the current beta freeze version.

## Suggested Release Wording

- In short, this update is a round of baseline hardening with some standardized extension entrances opened, all still built on the minimal foundation for stability. It is still recommended for small projects and small modules at the start of development. For the full change list, see [VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md). More extensions and larger structural updates may follow based on real-world testing and community feedback. We welcome discussion.

