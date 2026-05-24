# Runbook - Ted Local Release Deploy

This runbook describes how `ted` deploys and validates a tagged `motorweb` release locally.

## Release concept

```text
pl develops
  ↓
pl cuts tag from main
  ↓
ted clones tag
  ↓
ted runs setup script
  ↓
ted runs app
  ↓
ted validates endpoints
```

## 1. pl cuts a tag

```bash
cd /opt/projects/motorweb
scripts/release/cut-tag.sh v0.5.3 "motorweb v0.5.3 deploy scripts"
```

## 2. ted clones release tag

As `ted`:

```bash
cd /opt/releases/motorweb
git clone --branch v0.5.3 git@github-squidpan:squidpan/motorweb.git motorweb-v0.5.3
```

Or use the wrapper script from any existing checkout:

```bash
scripts/deploy/ted-clone-release.sh v0.5.3
```

## 3. ted sets up JobApp

```bash
cd /opt/releases/motorweb/motorweb-v0.5.3
scripts/deploy/ted-setup-jobapp.sh
```

## 4. ted runs JobApp

```bash
scripts/deploy/ted-run-jobapp-json.sh
```

If port 8000 is busy:

```bash
scripts/deploy/ted-run-jobapp-json.sh 8001
```

## 5. ted validates JobApp

In a second terminal:

```bash
cd /opt/releases/motorweb/motorweb-v0.5.3
scripts/validate/ted-validate-jobapp.sh
```

For port 8001:

```bash
scripts/validate/ted-validate-jobapp.sh http://127.0.0.1:8001
```

## 6. ted stops JobApp

Use `Ctrl+C` in the terminal running Uvicorn.

If needed:

```bash
scripts/validate/ted-kill-jobapp.sh
```

## 7. If ted finds a problem

Report:

```text
release tag
command run
error output
endpoint tested
expected result
actual result
```

Then `pl` fixes and cuts a new tag.
