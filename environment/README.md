# Computational environment

Use this directory to document the software environment required to reproduce the teaching material.

Add only the files needed by the activity.

## R

Use `renv` when package versions are important.

```text
renv.lock
renv/
```

## Python

Use one explicit dependency mechanism, such as:

```text
requirements.txt
```

or

```text
environment.yml
```

## Julia

Use:

```text
Project.toml
Manifest.toml
```

## Mixed-language activities

Record relevant versions of interpreters, compilers, rendering software, and key libraries. Prefer reproducible environment files to long manual installation instructions.
