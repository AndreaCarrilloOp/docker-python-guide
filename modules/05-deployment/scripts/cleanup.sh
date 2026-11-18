#!/usr/bin/env bash
set -euo pipefail
[[ "$(kubectl config current-context)" == docker-desktop ]] || exit 1
track="${1:-}"
[[ "$track" == flask || "$track" == fastapi ]] || { echo "Usage: bash scripts/cleanup.sh flask|fastapi"; exit 1; }
read -rp "Delete $track lab resources? Type DELETE: " answer
[[ "$answer" == DELETE ]] || exit 0
if [[ "$track" == flask ]]; then
  kubectl -n python-guide delete deployment flask postgres --ignore-not-found
  kubectl -n python-guide delete service flask db --ignore-not-found
  kubectl -n python-guide delete pvc postgres-data --ignore-not-found
  kubectl -n python-guide delete secret postgres-auth --ignore-not-found
else
  kubectl -n python-guide delete deployment fastapi redis --ignore-not-found
  kubectl -n python-guide delete service fastapi redis --ignore-not-found
fi
