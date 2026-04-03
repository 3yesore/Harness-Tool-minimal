# GitHub Release Guide

This repository is the staging copy. Before updating the publish repository, keep the working tree clean, verify the example module, and sync the OpenClaw skill package.

## 1. Pre-release Checklist

1. Run the repository validators.
2. Confirm `examples/hello_world` still passes smoke testing.
3. Make sure no temporary files or local build artifacts remain.
4. Sync `.openclaw_skill/` with the current implementation.

Recommended checks:

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
```

## 2. Publish to GitHub

```bash
git status --short
git add .
git commit -m "Prepare harness tool release"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

If the publish repository is separate from this staging repository, copy the reviewed contents there first, then repeat the same validation commands.

## 3. Suggested Release Notes

```markdown
## Initial Harness Tool Release

Highlights:
- standard module structure with `INDEX.md`, `SPEC.md`, and `CHANGELOG.md`
- runnable smoke-test validation
- profile-based rule presets
- bundled OpenClaw skill package
- reference example in `examples/hello_world`

Validation:
- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
```

## 4. After Release

1. Tag the release, for example `v1.0.0`.
2. Add a short GitHub release description.
3. Verify that the repository README and skill package still match the published behavior.
4. Record the release date in `VERSION_ROADMAP.en.md` if the roadmap changed.
