# 01 - GitHub Multiple SSH Accounts Setup

Goal: use one Linux workstation with two GitHub accounts:

```text
squidpan
paulchlyu
```

This allows Git operations from Tilix, PyCharm, and GitHub Desktop.

---

## 1. Confirm Git is installed

```bash
git --version
```

If missing:

```bash
sudo apt update
sudo apt install git
```

---

## 2. Configure default Git identity

```bash
git config --global user.name "squidpan"
git config --global user.email "squidpan11@gmail.com"
```

Check:

```bash
git config --global --list
```

---

## 3. Create SSH key for squidpan

```bash
ssh-keygen -t ed25519 -C "squidpan11@gmail.com" -f ~/.ssh/id_ed25519_squidpan
```

---

## 4. Create SSH key for paulchlyu

Replace the email with the correct email for that GitHub account.

```bash
ssh-keygen -t ed25519 -C "paulchlyu_email@example.com" -f ~/.ssh/id_ed25519_paulchlyu
```

---

## 5. Start ssh-agent

```bash
eval "$(ssh-agent -s)"
```

---

## 6. Add both keys

```bash
ssh-add ~/.ssh/id_ed25519_squidpan
ssh-add ~/.ssh/id_ed25519_paulchlyu
```

Check:

```bash
ssh-add -l
```

---

## 7. Add public keys to GitHub

Display squidpan public key:

```bash
cat ~/.ssh/id_ed25519_squidpan.pub
```

Add it to:

```text
GitHub squidpan account → Settings → SSH and GPG keys → New SSH key
```

Display paulchlyu public key:

```bash
cat ~/.ssh/id_ed25519_paulchlyu.pub
```

Add it to:

```text
GitHub paulchlyu account → Settings → SSH and GPG keys → New SSH key
```

---

## 8. Create SSH config aliases

```bash
nano ~/.ssh/config
```

Add:

```sshconfig
# GitHub - squidpan
Host github-squidpan
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_squidpan
  IdentitiesOnly yes

# GitHub - paulchlyu
Host github-paulchlyu
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_paulchlyu
  IdentitiesOnly yes
```

Set permissions:

```bash
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519_squidpan
chmod 600 ~/.ssh/id_ed25519_paulchlyu
chmod 644 ~/.ssh/id_ed25519_squidpan.pub
chmod 644 ~/.ssh/id_ed25519_paulchlyu.pub
```

---

## 9. Test SSH access

```bash
ssh -T github-squidpan
ssh -T github-paulchlyu
```

---

## 10. Remote URL examples

For squidpan:

```bash
git remote add origin git@github-squidpan:squidpan/motorweb.git
```

For paulchlyu:

```bash
git remote add origin git@github-paulchlyu:paulchlyu/some-repo.git
```

---

## 11. Per-repository identity

Inside this repo:

```bash
git config user.name "squidpan"
git config user.email "squidpan11@gmail.com"
```

Check:

```bash
git config --local --list
```
