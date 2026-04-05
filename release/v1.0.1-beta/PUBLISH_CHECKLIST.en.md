# Publish Checklist

## Before Publishing

- Confirm `README.md` is the Chinese homepage and `README.en.md` is the English mirror
- Confirm `VERSION_DESCRIPTION.zh.md` and `VERSION_DESCRIPTION.en.md` say the same thing
- Confirm `GITHUB_RELEASE.zh.md` keeps the user-provided summary as the first item
- Confirm the version is consistently written as `v1.0.1 beta` / `v1.0.1-beta`
- Confirm `v1.0.0` is no longer mixed into the release package

## Validation Commands

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
```

## GitHub Release

```bash
git status --short
git add .
git commit -m "Prepare v1.0.1 beta release"
git tag v1.0.1-beta
git push origin main
git push origin v1.0.1-beta
```

## After Publishing

- Check the GitHub Release title and body
- Confirm the tag points at the current `main` commit
- Confirm `v1.0.0` and `v1.0.1 beta` are not mixed together

