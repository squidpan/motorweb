#!/usr/bin/env bash
set -euo pipefail

# Review docs/setup/03-linux-users-service-accounts.md before running.
# Run as pl or another sudo-capable admin user.

sudo adduser dev || true
sudo adduser ted || true

sudo adduser --system --group svc-dev || true
sudo adduser --system --group svc-test || true
sudo adduser --system --group svc-prod || true

sudo groupadd developers || true
sudo groupadd deployers || true
sudo groupadd env-dev || true
sudo groupadd env-test || true
sudo groupadd env-prod || true

sudo usermod -aG developers pl
sudo usermod -aG developers dev
sudo usermod -aG deployers ted

sudo usermod -aG env-dev pl
sudo usermod -aG env-test pl
sudo usermod -aG env-prod pl

sudo usermod -aG env-dev dev
sudo usermod -aG env-test ted
sudo usermod -aG env-prod ted

sudo mkdir -p /opt/projects
sudo mkdir -p /opt/releases/modern-web-platform-py
sudo mkdir -p /opt/envs/dev/modern-web-platform-py
sudo mkdir -p /opt/envs/test/modern-web-platform-py
sudo mkdir -p /opt/envs/prod/modern-web-platform-py

sudo chown -R dev:developers /opt/projects
sudo chown -R ted:deployers /opt/releases
sudo chown -R svc-dev:env-dev /opt/envs/dev
sudo chown -R svc-test:env-test /opt/envs/test
sudo chown -R svc-prod:env-prod /opt/envs/prod

sudo chmod -R 2775 /opt/projects
sudo chmod -R 2775 /opt/releases
sudo chmod -R 2775 /opt/envs/dev
sudo chmod -R 2775 /opt/envs/test
sudo chmod -R 2770 /opt/envs/prod

echo "Done. Log out and back in for group changes to take effect."
