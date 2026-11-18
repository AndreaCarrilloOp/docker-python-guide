# flask-quality

[Module guide](../README.md)

A task CRUD API backed by PostgreSQL. This checkpoint retains the development API.

## Run

From the repository root, enter this directory:

```bash
cd modules/03-code-quality/flask-quality
```

Copy `.env.example` to `.env` and enter a unique local password as `POSTGRES_PASSWORD` before starting. Do not commit that file.

```bash
docker compose up --build -d --wait
docker compose ps
```

Stop services with `docker compose down`. Add `-v` only when deliberately deleting lab data.

## Verify

Open http://localhost:5000/health.

Example resource: http://localhost:5000/tasks.

## Tests

Use a fresh Python 3.11 virtual environment in this directory. On Bash, run `python -m venv .venv` and `source .venv/bin/activate`; on PowerShell, run `python -m venv .venv` and `.\.venv\Scripts\Activate.ps1`.

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest tests -q
```

For code quality, run `python -m ruff check .` and `python -m pyright`.

Continue to the next checkpoint in the module navigation.
