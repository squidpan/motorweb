#!/usr/bin/env bash
set -euo pipefail

TAG="${1:-}"
REPO_URL="${MOTORWEB_REPO_URL:-git@github-squidpan:squidpan/motorweb.git}"
RELEASE_ROOT="${MOTORWEB_RELEASE_ROOT:-/opt/releases/motorweb}"

if [[ -z "$TAG" ]]; then
  echo "Usage: $0 <tag>"
  echo "Example: $0 v0.5.3"
  exit 1
fi

TARGET_DIR="${RELEASE_ROOT}/motorweb-${TAG}"

echo "[INFO] Repo URL: $REPO_URL"
echo "[INFO] Release root: $RELEASE_ROOT"
echo "[INFO] Target dir: $TARGET_DIR"

mkdir -p "$RELEASE_ROOT"

if [[ -d "$TARGET_DIR" ]]; then
  echo "[ERROR] Target release directory already exists: $TARGET_DIR"
  echo "Remove it first if you intentionally want to redeploy:"
  echo "  rm -rf \"$TARGET_DIR\""
  exit 1
fi

echo "[INFO] Cloning tag $TAG..."
git clone --branch "$TAG" --depth 1 "$REPO_URL" "$TARGET_DIR"

echo "[INFO] Release cloned: $TARGET_DIR"
