# Lab setup

[Course home](../README.md)

## Working directory

Clone the repository once. Lesson paths are relative to the repository root unless specified. Use Bash (Git Bash or WSL on Windows); in PowerShell use `curl.exe` instead of the `curl` alias, and adapt quoting as needed. Stop a running lab before reusing its port.

## Python environment

From the selected example directory in module 01 or 02:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r ../../../requirements-dev.txt
```

PowerShell activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

Reuse this environment in modules 03 and 04. If you reopen a terminal, activate it again.

## Compose

From the selected module 02 example, run `docker compose up --build -d --wait`. For Flask, set the local password first as explained in its lesson.

Use `docker compose ps` and `docker compose logs` to diagnose startup failures. If you enabled optional tools, stop them with `docker compose --profile tools down`; otherwise use `docker compose down`. Add `-v` only when intentionally deleting lab data. Keep credentials outside Git.

## Common checks

| Symptom | Check |
| --- | --- |
| Port already in use | Stop the previous lab or container. |
| Docker build fails | Inspect dependency installation and build output. |
| Service unhealthy | Inspect logs, service-name DNS and environment variables. |
| Ruff/Pyright command missing | Activate the virtual environment and install development requirements. |
| HTTP tests fail | Check that the API and its backing service are running. |
| Kubernetes pod Pending | Check events, image availability, storage and readiness. |

For credentials and local-only usage, see [security notes](security.md).
