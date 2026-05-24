# motorweb Deploy Scripts v0.5.3 Addendum

This overlay adds release, deploy, and validation wrapper scripts intended to be included in future Git tags.

Goal:

```text
pl cuts a tag
ted deploys that tag
ted runs wrapper scripts included in the tag
ted validates the app consistently
```

Primary scripts:

```text
scripts/release/cut-tag.sh
scripts/deploy/ted-clone-release.sh
scripts/deploy/ted-setup-jobapp.sh
scripts/deploy/ted-run-jobapp-json.sh
scripts/validate/ted-validate-jobapp.sh
scripts/validate/ted-kill-jobapp.sh
```

Docs:

```text
docs/runbooks/ted-local-release-deploy.md
docs/releases/release-tagging-strategy.md
docs/deployment/local-release-flow.md
```
