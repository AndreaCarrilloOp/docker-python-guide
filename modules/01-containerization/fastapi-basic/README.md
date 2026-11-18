# fastapi-basic

[Module guide](../README.md)

A standalone HTTP service.

## Run

From the repository root, enter this directory:

```bash
cd modules/01-containerization/fastapi-basic
```

```bash
docker build -t guide-fastapi:01 .
docker run --rm -p 127.0.0.1:8000:8000 guide-fastapi:01
```

## Verify

Open http://localhost:8000/health. Interactive API documentation: http://localhost:8000/docs.

## Tests

Use a fresh Python 3.11 virtual environment in this directory. On Bash, run `python -m venv .venv` and `source .venv/bin/activate`; on PowerShell, run `python -m venv .venv` and `.\.venv\Scripts\Activate.ps1`.

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest tests -q
```

Continue to the next checkpoint in the module navigation.
