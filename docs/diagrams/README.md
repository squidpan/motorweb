# Diagrams

This folder stores architecture and design diagrams.

## Folder Layout

```text
docs/diagrams/
├── plantuml/       # .puml source files
├── drawio/         # .drawio source files
├── images/         # imported images/screenshots
├── exports/        # exported PNG/SVG/PDF files
├── architecture/   # architecture diagrams
├── sequence/       # sequence diagrams
├── class/          # class diagrams
├── yaml/           # YAML/Kubernetes diagrams
└── json/           # JSON payload diagrams
```

## Can PlantUML be generated from Python source?

Partially, yes.

Good candidates:

```text
Class diagrams
Module dependency diagrams
Package diagrams
```

Possible tools later:

```text
pyreverse
pylint
py2puml
```

Usually better manually designed:

```text
Sequence diagrams
Architecture diagrams
Deployment diagrams
Kubernetes diagrams
Business process flows
```

Reason: Python source code does not fully explain runtime behavior, business flows, network topology, or deployment architecture.

## Starter PlantUML Files

```text
docs/diagrams/plantuml/jobapp-context.puml
docs/diagrams/plantuml/job-create-sequence.puml
docs/diagrams/plantuml/linux-users-env-access.puml
```
