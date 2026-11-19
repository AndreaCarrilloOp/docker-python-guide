# 01 · Containerization

**FastAPI track**

Package a minimal HTTP application into a Docker image.

## 1. Create the application

Open [main.py](fastapi-basic/main.py) and [requirements.txt](fastapi-basic/requirements.txt). Create the framework instance, a root route and a separate `GET /health` route returning `{"status":"healthy"}`.

## 2. Build the image

Read the [Dockerfile](fastapi-basic/Dockerfile) and [.dockerignore](fastapi-basic/.dockerignore). The [Dockerfile reference](../../docs/dockerfile.md) explains each instruction, caching and the non-root user.

From the repository root:

```bash
cd modules/01-containerization/fastapi-basic
docker build -t guide-fastapi:01 .
docker run --rm -p 127.0.0.1:8000:8000 guide-fastapi:01
```

## 3. Verify

In a second terminal:

```bash
curl -f http://localhost:8000/health
```

Expected: HTTP 200 and `{"status":"healthy"}`. Open http://localhost:8000/docs for interactive API documentation.

Stop the container with Ctrl+C before continuing. [Troubleshooting](../../docs/lab-setup.md#common-checks).

---

[Course home](../../README.md) · [Module 02 →](../02-development/FASTAPI.md)
