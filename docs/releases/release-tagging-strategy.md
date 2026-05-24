# Release Tagging Strategy

Use Git tags to mark deployable releases.

## Version style

```text
v0.5.2
v0.5.3
v0.5.4
```

## Tag rules

1. Tags are cut from `main`.
2. Working tree must be clean.
3. Use annotated tags.
4. Push tags to origin.
5. `ted` deploys tags, not random branches.

## Cut tag manually

```bash
git switch main
git pull
git status
git tag -a v0.5.3 -m "motorweb v0.5.3 deploy scripts"
git push origin v0.5.3
```

## Cut tag with wrapper

```bash
scripts/release/cut-tag.sh v0.5.3 "motorweb v0.5.3 deploy scripts"
```

## Iterative release cycle

```text
ted finds issue in v0.5.3
pl fixes on feature branch
pl merges to main
pl cuts v0.5.4
ted deploys v0.5.4
```
