# Docker Python Guide

**Build · Develop · Test · Deploy**

A hands-on, incremental tutorial for Python applications with Docker. Clone once, choose one framework, and follow five modules in order. You do not need to switch branches or complete both tracks.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
[![CI](https://github.com/AndreaCarrilloOp/docker-python-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/AndreaCarrilloOp/docker-python-guide/actions/workflows/ci.yml)

## Choose your learning path

| Flask | FastAPI |
|---|---|
| Start with Flask, then add PostgreSQL. | Start with FastAPI, then add Redis. |
| [**Start Flask tutorial →**](modules/01-containerization/flask-basic/README.md) | [**Start FastAPI tutorial →**](modules/01-containerization/fastapi-basic/README.md) |

## Learning modules

| Module | Flask track | FastAPI track |
|---|---|---|
| 1. [Containerization](modules/01-containerization/README.md) | [Flask](modules/01-containerization/flask-basic/README.md) | [FastAPI](modules/01-containerization/fastapi-basic/README.md) |
| 2. [Development](modules/02-development/README.md) | [Flask](modules/02-development/flask-postgres/README.md) | [FastAPI](modules/02-development/fastapi-redis/README.md) |
| 3. [Linting and typing](modules/03-linting-typing/README.md) | [Flask](modules/03-linting-typing/FLASK.md) | [FastAPI](modules/03-linting-typing/FASTAPI.md) |
| 4. [CI/CD with GitHub Actions](modules/04-cicd/README.md) | [Flask](modules/04-cicd/FLASK.md) | [FastAPI](modules/04-cicd/FASTAPI.md) |
| 5. [Test your deployment](modules/05-deployment/README.md) | [Flask](modules/05-deployment/FLASK.md) | [FastAPI](modules/05-deployment/FASTAPI.md) |

## Get started

Install Git, Python 3.11, Docker Desktop (or Docker Engine with Compose v2). Kubernetes in Docker Desktop and kubectl are needed only for module 05.

```bash
git clone https://github.com/AndreaCarrilloOp/docker-python-guide.git
cd docker-python-guide
```

Choose your track above. Commands use Bash unless marked PowerShell. Run each command from the stated directory. Stop each lab before reusing its port.

## How the guide grows

- Module 01: a standalone container per framework.
- Module 02: extend the basic example into a service-backed API.
- Modules 03–05: improve, test, automate and deploy that same API without copying source code.

The supplied files are reference implementations; each lesson explains how to reproduce them. This approach keeps four runnable examples and five learning checkpoints.

See [security notes](docs/security.md), [original implementations and migration history](docs/migration-history.md), and [contributing](CONTRIBUTING.md). This is a local educational lab, not a production hosting guide.

[MIT License](LICENSE)
