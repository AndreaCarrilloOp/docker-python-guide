#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ "$(kubectl config current-context)" != "docker-desktop" ]]; then
  echo "This lab requires the docker-desktop context." >&2
  exit 1
fi
docker build -t python-guide-flask:local flask-deployment
docker build -t python-guide-fastapi:local fastapi-deployment
kubectl apply -f k8s/namespace.yaml
if ! kubectl -n python-guide get secret postgres-auth >/dev/null 2>&1; then
  read -rsp "Local PostgreSQL password: " password; echo
  [[ -n "$password" ]] || exit 1
  printf '%s' "$password" | kubectl -n python-guide create secret generic postgres-auth --from-file=password=/dev/stdin
  unset password
fi
kubectl apply -f k8s/postgres.yaml -f k8s/redis.yaml
kubectl -n python-guide rollout status deployment/postgres --timeout=180s
kubectl -n python-guide rollout status deployment/redis --timeout=180s
kubectl apply -f k8s/flask.yaml -f k8s/fastapi.yaml
kubectl -n python-guide rollout status deployment/flask --timeout=180s
kubectl -n python-guide rollout status deployment/fastapi --timeout=180s
kubectl -n python-guide get pods,svc
