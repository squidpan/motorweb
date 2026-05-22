#!/usr/bin/env bash
set -euo pipefail

git init
git add .
git commit -m "Initial validated platform baseline with Job Application Platform"
git branch -M main

echo "Now create the GitHub repo, then run:"
echo "git remote add origin git@github-squidpan:squidpan/modern-web-platform-py.git"
echo "git push -u origin main"
