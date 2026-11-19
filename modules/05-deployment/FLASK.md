# 05 · Test your deployment

[← Flask track](../../tracks/FLASK.md) · 5/5

Deploy the same Flask application and PostgreSQL to local Kubernetes.

## 1. Prepare Kubernetes

Enable Kubernetes in Docker Desktop. Stop the Compose lab before reusing port 5000.

```bash
kubectl config current-context
kubectl get nodes
```

Expected: `docker-desktop` and a Ready node. The cluster must access local Docker images and provide a default StorageClass for PostgreSQL.

## 2. Deploy

From the repository root:

```bash
cd modules/05-deployment
bash scripts/deploy.sh flask
```

The `script` builds module 02, applies the namespace, deploys PostgreSQL, waits for readiness and deploys Flask. Enter a local password when prompted; the script creates the Kubernetes Secret outside Git.

Review `postgres.yaml` and `flask.yaml` for Services, Deployments and health probes.

## 3. Verify

```bash
kubectl -n python-guide get pods,svc
kubectl -n python-guide rollout status deployment/flask
kubectl -n python-guide port-forward svc/flask 5000:5000
```

In a second terminal, open http://localhost:5000/health. Repeat your module 04 HTTP tests against this endpoint. Expected: Ready pods, successful rollout and HTTP 200.

If needed, inspect `kubectl -n python-guide logs deployment/flask` and `kubectl -n python-guide describe deployment/flask`.

## 4. Clean up

Stop port-forward, then run:

```bash
bash scripts/cleanup.sh flask
```

Confirm DELETE only to remove this track's resources, including its database volume. This completes the Flask track.

## Solution

[`namespace.yaml`](k8s/namespace.yaml) · [`postgres.yaml`](k8s/postgres.yaml) · [`flask.yaml`](k8s/flask.yaml)

[`deploy.sh`](scripts/deploy.sh) · [`cleanup.sh`](scripts/cleanup.sh)

---

[← CI/CD with GitHub Actions](../04-cicd/FLASK.md) · [Finish track →](../../tracks/FLASK.md)
