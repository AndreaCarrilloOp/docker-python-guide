# Lab setup

[Course home](../README.md)

## Prerequisites

Install Git, Python 3.11 and Docker with Compose v2. Docker Desktop Kubernetes and kubectl are needed only for module 05.

## Working directory

Clone the repository once:

```bash
git clone https://github.com/AndreaCarrilloOp/docker-python-guide.git
cd docker-python-guide
```

Lesson paths are relative to the repository root unless specified. Use Bash (Git Bash or WSL on Windows); in PowerShell use `curl.exe` instead of the `curl` alias, and adapt quoting as needed. Stop a running lab before reusing its port.

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

Follow the selected module 02 tutorial to start services.

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

## References

[Dockerfile reference](dockerfile.md) · [Security notes](security.md) · [Migration history](migration-history.md) · [Contributing](../CONTRIBUTING.md) · [MIT license](../LICENSE)
