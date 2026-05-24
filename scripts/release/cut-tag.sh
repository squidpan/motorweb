#!/usr/bin/env bash
set -euo pipefail

TAG="${1:-}"
MESSAGE="${2:-}"

if [[ -z "$TAG" || -z "$MESSAGE" ]]; then
  echo "Usage: $0 <tag> <message>"
  echo "Example: $0 v0.5.3 \"motorweb v0.5.3 deploy scripts\""
  exit 1
fi

if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "[ERROR] Not inside a Git repository."
  exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

CURRENT_BRANCH="$(git branch --show-current)"

echo "[INFO] Repo root: $REPO_ROOT"
echo "[INFO] Current branch: $CURRENT_BRANCH"
echo "[INFO] Target tag: $TAG"

if [[ "$CURRENT_BRANCH" != "main" ]]; then
  echo "[ERROR] Tags should be cut from main. Current branch: $CURRENT_BRANCH"
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "[ERROR] Working tree is not clean. Commit or stash changes first."
  git status --short
  exit 1
fi

echo "[INFO] Pulling latest main..."
git pull origin main

if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "[ERROR] Tag already exists locally: $TAG"
  exit 1
fi

if git ls-remote --tags origin | grep -q "refs/tags/${TAG}$"; then
  echo "[ERROR] Tag already exists on origin: $TAG"
  exit 1
fi

echo "[INFO] Creating annotated tag..."
git tag -a "$TAG" -m "$MESSAGE"

echo "[INFO] Pushing tag..."
git push origin "$TAG"

echo "[INFO] Release tag created and pushed: $TAG"
