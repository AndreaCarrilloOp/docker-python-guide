# Module 05 — Kubernetes Deployment

[Previous module](../04-cicd/README.md) · [Return to learning path](../../README.md)

## Overview

Deploy the existing application and its backing service to a local Kubernetes cluster.

Complete the preceding checkpoint first.

## Learning objectives

- Deploy the existing application and its backing service to a local Kubernetes cluster.
- Understand the relationship between Python application code and its runtime configuration.
- Verify a working example before continuing.

## Examples

| Track | Example |
|---|---|
| Flask | [flask-deployment](flask-deployment/README.md) |
| FastAPI | [fastapi-deployment](fastapi-deployment/README.md) |

## Implementation

### Local Kubernetes lab

Use Docker Desktop with Kubernetes enabled. From this module directory:

```bash
kubectl config current-context
kubectl get nodes
bash scripts/deploy.sh
```

The script requires the docker-desktop context and prompts for a fresh local database password if its Secret is absent. It builds both local images, applies namespaced resources and waits for readiness. The cluster must have a default StorageClass and access to locally built images.

In separate terminals:

```bash
kubectl -n python-guide port-forward svc/flask 5000:5000
# Separate terminal:
kubectl -n python-guide port-forward svc/fastapi 8000:8000
```

Check http://localhost:5000/health and http://localhost:8000/health. For Windows PowerShell, use the same kubectl commands, or execute the Bash script in WSL with Docker Desktop integration and the correct Kubernetes context. To clean the disposable lab, run `bash scripts/cleanup.sh` and confirm deletion of the namespace and its data.

The CI workflow parses the manifests; an actual local cluster deployment must also be tested.

## Validation

Follow the selected example README. Confirm that its functional tests pass and that the HTTP health endpoint responds successfully before moving on.

## Next checkpoint

[Return to learning path](../../README.md)
