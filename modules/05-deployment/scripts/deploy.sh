#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
track="${1:-}"
[[ "$track" == flask || "$track" == fastapi ]] || { echo "Usage: bash scripts/deploy.sh flask|fastapi"; exit 1; }
[[ "$(kubectl config current-context)" == docker-desktop ]] || { echo "Use the docker-desktop context."; exit 1; }
kubectl apply -f k8s/namespace.yaml
if [[ "$track" == flask ]]; then
  docker build -t python-guide-flask:local ../02-development/flask-postgres
  if ! kubectl -n python-guide get secret postgres-auth >/dev/null 2>&1; then
    read -rsp "Local PostgreSQL password: " password; echo
    [[ -n "$password" ]] || exit 1
    printf '%s' "$password" | kubectl -n python-guide create secret generic postgres-auth --from-file=password=/dev/stdin
    unset password
  fi
  dependency=postgres
else
  docker build -t python-guide-fastapi:local ../02-development/fastapi-redis
  dependency=redis
fi
kubectl apply -f "k8s/$dependency.yaml"
kubectl -n python-guide rollout status "deployment/$dependency" --timeout=180s
kubectl apply -f "k8s/$track.yaml"
kubectl -n python-guide rollout restart "deployment/$track"
kubectl -n python-guide rollout status "deployment/$track" --timeout=180s
kubectl -n python-guide get pods,svc
