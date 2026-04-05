# Harness Tool Minimal v1.0.1 beta

In short, this update hardens the baseline and opens some standardized extension entrances, all still built on the minimal foundation for stability. It is still recommended for small projects and small modules at the start of development. For the full change list, see [VERSION_DESCRIPTION.en.md](VERSION_DESCRIPTION.en.md). More extensions and larger structural updates may follow based on real-world testing and community feedback. We welcome discussion.

## Release Summary

- Keep the minimal loop: `init / apply / validate`
- Keep the standardized module entry points: `INDEX.md`, `SPEC.md`, and `CHANGELOG.md`
- Keep lightweight extension surfaces: `profiles/`, `templates/`, and `.openclaw_skill/`
- Keep GitHub Actions baseline validation
- Keep the Chinese primary homepage plus English mirror release format

## Validation Commands

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
```

## Release Notes

- This is the freeze release for `v1.0.1 beta`.
- Rollback anchor: `v1.0.0`
- Best suited for small projects, small modules, and early-stage development.
- Further structural expansion will depend on testing and feedback.

