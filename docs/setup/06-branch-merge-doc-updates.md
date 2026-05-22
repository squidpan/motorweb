# 06 - Branch and Merge Documentation Updates

Use this process when applying documentation-only overlay packages.

## 1. Start from main

```bash
cd /opt/projects/motorweb
git checkout main
git pull
git status
```

## 2. Create feature branch

```bash
git checkout -b feature/opt-projects-shared-model
```

## 3. Apply doc overlay package

```bash
unzip ~/Downloads/motorweb-doc-updates-v0.4.2.zip -d .
```

## 4. Review changes

```bash
git status
git diff --stat
```

Optional:

```bash
git diff
```

## 5. Commit

```bash
git add .
git commit -m "Document shared opt projects model"
```

## 6. Push branch

```bash
git push -u origin feature/opt-projects-shared-model
```

## 7. Merge locally

```bash
git checkout main
git pull
git merge feature/opt-projects-shared-model
git push origin main
```

## 8. Optional cleanup

```bash
git branch -d feature/opt-projects-shared-model
git push origin --delete feature/opt-projects-shared-model
```
