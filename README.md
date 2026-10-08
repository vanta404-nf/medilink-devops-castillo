# CIT 305 Module 11 Reference Project

This small project supports the guided laboratory on Git workflows and GitHub Actions.
It intentionally uses only the Python standard library.

## Run the demo

```bash
python demo_summary.py
```

## Run local CI-equivalent checks

```bash
python scripts/run_ci_checks.py
```

## Run tests directly

```bash
python -m unittest discover -s tests -v
```

The `.github/workflows/integration-ci.yml` file runs equivalent checks on GitHub Actions.
