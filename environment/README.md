# Computational environment

This template is language-neutral. Add only the environment files required by the actual course.

## R

Recommended for version-sensitive courses:

```text
renv.lock
renv/
```

## Python

Choose one explicit mechanism, for example:

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

## Mixed-language courses

Document the exact versions of Quarto, interpreters, compilers, and key libraries. Prefer a reproducible environment over long manual installation instructions.
