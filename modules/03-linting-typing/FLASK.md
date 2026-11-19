# 03 · Linting and typing

**Flask track**

Improve the application from module 02 without creating a new copy.

## 1. Prepare the existing project

```bash
cd modules/02-development/flask-postgres
```

Follow [Python environment setup](../../docs/lab-setup.md#python-environment) from this directory. The shared [pyproject.toml](../../pyproject.toml) defines linting and type-checking rules.

## 2. Check and format

```bash
python -m ruff check .
python -m ruff check --fix .
python -m ruff format .
python -m ruff check .
python -m pyright .
```

In [app.py](../02-development/flask-postgres/app.py), inspect the typed Task fields, explicit constructor and SQLAlchemyError handling.

`--fix` and `format` modify local source; review the resulting diff.

## 3. Automate local checks

With your environment active, return to the repository root:

```bash
cd ../../..
pre-commit install
pre-commit run --all-files
```

See [.pre-commit-config.yaml](../../.pre-commit-config.yaml). If formatting changes files, review them and rerun the hooks. Expected: no lint or type errors and passing hooks.

---

[Flask modules](../../tracks/FLASK.md) · [← Module 02](../02-development/FLASK.md) · [Module 04 →](../04-cicd/FLASK.md)
