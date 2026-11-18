# Module 05 — Test your deployment · FastAPI

[Learning path](../../README.md) · [Previous lesson](../../modules/04-cicd/FASTAPI.md)

## What you'll learn

Deploy the existing container to local Kubernetes and validate it.

## Prerequisites

Complete the previous lesson in this track. Docker Desktop Kubernetes, kubectl and Bash (WSL is acceptable with Docker Desktop integration).

## What's new

Kubernetes manifests and track-selective local deployment scripts.

## Step 1 — Prepare local Kubernetes

Enable Kubernetes in Docker Desktop. Check the context and nodes. Stop the Compose lab first to release port 8000.

```bash
kubectl config current-context
kubectl get nodes
```

Expected: docker-desktop context and a Ready node. The cluster needs local image access.

## Step 2 — Build and deploy the same API

From the repository root:

```bash
cd modules/05-deployment
bash scripts/deploy.sh fastapi
```

The script builds the image directly from module 02, creates the namespace, applies Redis resources, waits for readiness, deploys FastAPI, and waits for rollout. It does not deploy PostgreSQL or require a PostgreSQL password. Read [redis.yaml](k8s/redis.yaml) and [fastapi.yaml](k8s/fastapi.yaml) to understand the Service, Deployment and probes.

## Step 3 — Verify deployment

```bash
kubectl -n python-guide get pods,svc
kubectl -n python-guide rollout status deployment/fastapi
kubectl -n python-guide port-forward svc/fastapi 8000:8000
```

In a separate terminal, check http://localhost:8000/health and repeat the module 04 tests against this endpoint. Expected: Ready pods, successful rollout and HTTP 200. Inspect failures using kubectl -n python-guide logs deployment/fastapi and kubectl -n python-guide describe deployment/fastapi.

## Step 4 — Cleanup

Stop port-forward, then run ```bash
bash scripts/cleanup.sh fastapi
``` Confirm DELETE only when ready to remove this track's lab resources. The other route remains untouched.

## Troubleshooting

If a pod is Pending or cannot start, inspect events, image availability, storage and dependency readiness.

## Key takeaway

Kubernetes manages containers and exposes them through Services.

[Learning path](../../README.md) · [Previous lesson](../../modules/04-cicd/FASTAPI.md)
