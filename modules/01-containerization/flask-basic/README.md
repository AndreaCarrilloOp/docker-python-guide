# Module 01 — Containerization · Flask

[Learning path](../../../README.md) · [Next lesson →](../../../modules/02-development/flask-postgres/README.md)

## What you'll learn

Package a minimal HTTP application into a Docker image.

## Prerequisites

Python 3.11, Docker and Git. 

## What's new

Application source, dependency file, Dockerfile and .dockerignore.

## Step 1 — Create a minimal Python application

Read [app.py](app.py) and [requirements.txt](requirements.txt). Create a framework instance, a root route and a GET /health route that returns JSON. Run locally after installing requirements: python app.py.

## Step 2 — Containerize

Read [Dockerfile](Dockerfile). Start from python:3.11-slim, set WORKDIR, copy/install requirements before source for layer caching, create a non-root user, expose port 5000, add a health check and set CMD. Exclude local files using [.dockerignore](.dockerignore). Docker init is an optional way to generate a starter Dockerfile; compare it to the supplied file rather than overwriting the reference.

## Step 3 — Build and run

```bash
cd modules/01-containerization/flask-basic
docker build -t guide-flask:01 .
docker run --rm -p 127.0.0.1:5000:5000 guide-flask:01
```

## Validate

In a second terminal: ```bash
curl -f http://localhost:5000/health
```
Expected: {"status":"healthy"}. Visit / for the greeting. Stop with Ctrl+C.

## Troubleshooting

If port 5000 is busy, stop the previous container. If the build fails, inspect the Docker build output.

## Key takeaway

An image packages the app; a container runs it.

[Learning path](../../../README.md) · [Next lesson →](../../../modules/02-development/flask-postgres/README.md)
