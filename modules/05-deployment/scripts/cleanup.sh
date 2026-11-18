#!/usr/bin/env bash
set -euo pipefail
[[ "$(kubectl config current-context)" == "docker-desktop" ]] || exit 1
read -rp "Delete python-guide namespace and its lab data? Type DELETE: " answer
[[ "$answer" == DELETE ]] || exit 0
kubectl delete namespace python-guide
