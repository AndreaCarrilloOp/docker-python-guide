# 05 · Test your deployment

**FastAPI track · Module 05/05** · ●●●●●

[All modules](../../tracks/FASTAPI.md) · [Solution ↓](#solution)

Deploy the same FastAPI application and Redis to local Kubernetes.

## 1. Prepare Kubernetes

Enable Kubernetes in Docker Desktop. Stop the Compose lab before reusing port 8000.

```bash
kubectl config current-context
kubectl get nodes
```

Expected: `docker-desktop` and a Ready node. The cluster must access local Docker images.

## 2. Deploy

From the repository root:

```bash
cd modules/05-deployment
bash scripts/deploy.sh fastapi
```

The [script](scripts/deploy.sh) builds module 02, applies the namespace, deploys Redis, waits for readiness and deploys FastAPI.

Review [redis.yaml](k8s/redis.yaml) and [fastapi.yaml](k8s/fastapi.yaml) for Services, Deployments and health probes.

## 3. Verify

```bash
kubectl -n python-guide get pods,svc
kubectl -n python-guide rollout status deployment/fastapi
kubectl -n python-guide port-forward svc/fastapi 8000:8000
```

In a second terminal, open http://localhost:8000/health. Repeat your module 04 HTTP tests against this endpoint. Expected: Ready pods, successful rollout and HTTP 200.

If needed, inspect `kubectl -n python-guide logs deployment/fastapi` and `kubectl -n python-guide describe deployment/fastapi`.

## 4. Clean up

Stop port-forward, then run:

```bash
bash scripts/cleanup.sh fastapi
```

Confirm DELETE only to remove this track's resources. This completes the FastAPI track.

## Solution

Local Kubernetes deployment of the module 02 application.

[Namespace](k8s/namespace.yaml) · [Redis resources](k8s/redis.yaml) · [FastAPI resources](k8s/fastapi.yaml)

[Deploy script](scripts/deploy.sh) · [Cleanup script](scripts/cleanup.sh) · [Application](../02-development/fastapi-redis/)

---

[← Module 04](../04-cicd/FASTAPI.md) · [Course complete · Back to track](../../tracks/FASTAPI.md)
