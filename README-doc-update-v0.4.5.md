# README Update - v0.4.5 Requirements Addendum

Add this section near the top of the root `README.md`, after the project overview and before Quick Start.

---

## Hardware and Software Requirements

This project can be built and run on a Linux development workstation.

The reference workstation used for this project is documented in:

```text
docs/setup/software-and-hardware-requirements.md
```

Linux setup guide:

```text
docs/setup/linux-development-environment.md
```

Tooling prerequisites:

```text
docs/setup/tooling-prerequisites.md
```

Local validation runbook:

```text
docs/runbooks/validate-local-dev-environment.md
```

### Minimum practical setup

```text
Linux workstation
Python 3.13
Git
OpenSSH client
curl
zip/unzip
Python virtual environment support
```

### Recommended development tools

```text
PyCharm
Obsidian
Insomnia or Postman
Docker
kubectl
Helm
Node.js/npm
Java
```

### Reference Linux machine

The current reference machine is:

```text
Pop!_OS 22.04 LTS
AMD Ryzen 9 8945HS
16 logical CPUs
60 GiB RAM
934 GiB root filesystem
Python 3.13.13
Git 2.34.1
Docker 29.1.4-rd
kubectl 1.33.3
Helm 4.0.5
Node.js 22.20.0
Java 25
PyCharm 2026.1
Obsidian
Insomnia
```

Note: `pip` was not available globally in the captured output. This is okay because the project should use a virtual environment and `python -m pip` after creating `.venv`.
