# 01 · Containerization

[← Flask track](../../tracks/FLASK.md) · 1/5

Package a minimal HTTP application into a Docker image.

## 1. Create the application

Open `app.py` and `requirements.txt`. Create the framework instance, a root route and a separate `GET /health` route returning `{"status":"healthy"}`.

## 2. Build the image

Read the `Dockerfile` and `.dockerignore`. The [Dockerfile reference](../../docs/dockerfile.md) explains each instruction, caching and the non-root user.

From the repository root:

```bash
cd modules/01-containerization/flask-basic
docker build -t guide-flask:01 .
docker run --rm -p 127.0.0.1:5000:5000 guide-flask:01
```

## 3. Verify

In a second terminal:

```bash
curl -f http://localhost:5000/health
```

Expected: HTTP 200 and `{"status":"healthy"}`. Open http://localhost:5000/ for the greeting.

Stop the container with Ctrl+C before continuing. [Troubleshooting](../../docs/lab-setup.md#common-checks).

## Solution

[`app.py`](flask-basic/app.py) · [`Dockerfile`](flask-basic/Dockerfile) · [`requirements.txt`](flask-basic/requirements.txt) · [`.dockerignore`](flask-basic/.dockerignore)

---

[Development →](../02-development/FLASK.md)
