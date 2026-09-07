# Using the template

## Create the repository

Use **Use this template → Create a new repository**. Do not fork the template for routine course creation.

## Configure metadata

Replace placeholders in:

- `repo.yml`
- `course.yml`
- `_quarto.yml`
- `CITATION.cff`
- root teaching files
- the example module

Then run:

```bash
python scripts/validate_structure.py
```

A generated teaching repository should not pass validation while required placeholders remain.

## Select the teaching format

For a single class or seminar, keep one or two modules and remove unused assessment sections.

For a workshop or short course, use several modules with short concept blocks and practical work.

For a semester course, retain the schedule, assignments, and optional applied project.

## Add modules

Copy `modules/01-topic/`, increment the numeric prefix, and update `module.yml` and the associated teaching files.

## Configure computation

Use only the software environment required by the activity. See `environment/README.md`.

## Publish

In the generated repository, enable:

**Settings → Pages → Build and deployment → Source = GitHub Actions**

The workflow validates and renders changes. Pushes to `main` deploy the course site.

## Academic integration

Add `type-training` to classify the repository. Add `site-teaching` when the activity should also be listed on `qselmer.github.io/teaching/`.
