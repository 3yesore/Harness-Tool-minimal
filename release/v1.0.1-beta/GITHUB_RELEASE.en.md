# Harness Tool Minimal v1.0.1 Historical Baseline

`v1.0.1 beta` is the frozen minimal baseline for this project.  
It is no longer positioned as a platform-expansion experiment. Instead, it serves as a historical baseline display page that can be used as a stable reference.

For the full version description, risk boundaries, and release resources, see [VERSION_DESCRIPTION.en.md](VERSION_DESCRIPTION.en.md).  
If you want the short historical view, see [DISPLAY_PAGE.en.md](DISPLAY_PAGE.en.md).

## What this release shows

- Minimal loop: `init / apply / validate`
- Standardized module entry points: `INDEX.md`, `SPEC.md`, and `CHANGELOG.md`
- Lightweight extension surfaces: `profiles/`, `templates/`, and `.openclaw_skill/`
- Default consistency mode: `soft`
- Extension style: example-first, project-local implementation

## Why it is worth keeping

- It consolidates module development, validation, handoff, and records into a small set of fixed files.
- It preserves room for project-level customization without making the core thick.
- It is suitable for small projects, small modules, and early-stage development.
- It serves as the historical baseline for later experiments and future expansion.

## Validation commands

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
python examples/local_extension/harness/run_harness.py
```

## Release notes

- Rollback anchor: `v1.0.0`
- Page role: historical baseline display page
- Recommended use: reference baseline for later experiments and extension backflow
