# GitHub Release Guide

This is the release-prep page for the cleaned-up staging repository. Before publishing, keep the root tidy, verify the example module, and make sure the skill package matches the current implementation.

## Pre-release Checklist

1. Run the repository validators.
2. Confirm `examples/hello_world` still passes smoke testing.
3. Make sure no temporary files, caches, or local build artifacts remain.
4. Sync `.openclaw_skill/` with the current implementation.

Recommended checks:

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
```

## Publish to GitHub

```bash
git status --short
git add .
git commit -m "Prepare harness tool release"
git push
```

If the publish repository is separate from this staging repository, copy the reviewed contents there first, then repeat the same checks.

## Suggested Release Notes

```markdown
## Harness Tool Minimal v1.0

Highlights:
- module handoff flow with `INDEX.md`, `SPEC.md`, and `CHANGELOG.md`
- runnable smoke-test validation
- profile-based rule presets
- bundled OpenClaw / Codex skill package
- reference examples in `examples/`

Skill install:
- download the ZIP archive directly from GitHub
- copy `.openclaw_skill` into your local skill directory
- if your skill manager supports name-based install, publish the package there too

Validation:
- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
```

## After Release

1. Tag the release, for example `v1.0.0`.
2. Add a short GitHub release description.
3. Verify that the README, release page, and skill package still match the published behavior.
4. Update `VERSION_ROADMAP.en.md` if the roadmap changed.
