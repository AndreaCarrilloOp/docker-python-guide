# 01 · Containerization

[← FastAPI track](../../tracks/FASTAPI.md) · 1/5

Package a minimal HTTP application into a Docker image.

## 1. Create the application

Open `main.py` and `requirements.txt`. Create the framework instance, a root route and a separate `GET /health` route returning `{"status":"healthy"}`.

## 2. Build the image

Read the `Dockerfile` and `.dockerignore`. The [Dockerfile reference](../../docs/dockerfile.md) explains each instruction, caching and the non-root user.

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

## Solution

[`main.py`](fastapi-basic/main.py) · [`Dockerfile`](fastapi-basic/Dockerfile) · [`requirements.txt`](fastapi-basic/requirements.txt) · [`.dockerignore`](fastapi-basic/.dockerignore)

---

[Development →](../02-development/FASTAPI.md)
