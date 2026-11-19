# Docker Python Guide

Learn to containerize, develop, test and deploy Python applications with Docker — one framework, five progressive modules.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
[![CI](https://github.com/AndreaCarrilloOp/docker-python-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/AndreaCarrilloOp/docker-python-guide/actions/workflows/ci.yml)

## Choose your path

| Flask + PostgreSQL | FastAPI + Redis |
| :--- | :--- |
| [Start Flask →](modules/01-containerization/FLASK.md) | [Start FastAPI →](modules/01-containerization/FASTAPI.md) |

## Curriculum

| Module | Flask | FastAPI |
| :--- | :---: | :---: |
| 01 · Containerization | [Lesson](modules/01-containerization/FLASK.md) | [Lesson](modules/01-containerization/FASTAPI.md) |
| 02 · Development | [Lesson](modules/02-development/FLASK.md) | [Lesson](modules/02-development/FASTAPI.md) |
| 03 · Linting and typing | [Lesson](modules/03-linting-typing/FLASK.md) | [Lesson](modules/03-linting-typing/FASTAPI.md) |
| 04 · CI/CD with GitHub Actions | [Lesson](modules/04-cicd/FLASK.md) | [Lesson](modules/04-cicd/FASTAPI.md) |
| 05 · Test your deployment | [Lesson](modules/05-deployment/FLASK.md) | [Lesson](modules/05-deployment/FASTAPI.md) |

## Getting started

Install Git, Python 3.11 and Docker with Compose v2. Kubernetes and kubectl are only needed for module 05.

```bash
git clone https://github.com/AndreaCarrilloOp/docker-python-guide.git
cd docker-python-guide
```

Choose one path and follow its lessons in order. Modules 03–05 build on the same application from module 02.

See [lab instructions](docs/lab-setup.md) for shell conventions and troubleshooting.

---

[Dockerfile reference](docs/dockerfile.md) · [Security](docs/security.md) · [History](docs/migration-history.md) · [Contributing](CONTRIBUTING.md) · [MIT](LICENSE)
