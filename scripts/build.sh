#!/usr/bin/env bash
# Agent Sentinel - build & validate the production site.
#   scripts/build.sh {build|serve}
set -euo pipefail

cd "$(dirname "$0")/.."

export PATH="$HOME/.local/bin:$PATH"

echo "==> Running validation (JSON schema + link checks)"
python3 scripts/validate.py

echo "==> Building site"
if ! command -v mkdocs >/dev/null 2>&1; then
  echo "ERROR: mkdocs not found. Install via: pipx install --include-deps mkdocs-material" >&2
  exit 1
fi
mkdocs build --strict

echo "==> Build OK: site contents in ./site"
