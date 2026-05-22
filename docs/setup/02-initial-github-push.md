# 02 - Initial GitHub Push

Goal: push `motorweb` to GitHub under `squidpan`.

---

## 1. Create empty GitHub repository

In GitHub account:

```text
squidpan
```

Create repository:

```text
motorweb
```

Recommended:

```text
Do not initialize with README
Do not add .gitignore
Do not add license yet
```

---

## 2. Go to local repo root

```bash
cd ~/pjs/repos/PycharmProjects/motorweb
```

---

## 3. Initialize Git

```bash
git init
```

---

## 4. Add files

```bash
git add .
```

---

## 5. Commit baseline

```bash
git commit -m "Initial validated platform baseline with Job Application Platform"
```

---

## 6. Rename branch to main

```bash
git branch -M main
```

---

## 7. Add GitHub remote

```bash
git remote add origin git@github-squidpan:squidpan/motorweb.git
```

Check:

```bash
git remote -v
```

---

## 8. Push

```bash
git push -u origin main
```

---

## 9. Create first docs branch

```bash
git checkout -b feature/platform-foundation-docs
```
