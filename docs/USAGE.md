# Using the template

## Create the repository

Use **Use this template → Create a new repository**. Do not fork the template for routine course creation.

## Configure metadata

The generated repository initially inherits the identity of `qselmer/.template-training`. Before using it as a real teaching repository:

1. Update `repo.yml` with the real owner, repository name, title, visibility, description, lifecycle status, maturity stage, canonical URL, and `type-training`.
2. Replace the inherited template metadata in `CITATION.cff` with the citation for the actual teaching activity.
3. Replace placeholders in `course.yml`, `_quarto.yml`, the example module, and the teaching files.
4. Keep exactly one canonical `type-*` topic in `repo.yml`: `type-training`.

Then run:

```bash
python -m pip install pyyaml
python scripts/validate_structure.py
```

A generated teaching repository should not pass validation while required placeholders remain or while it still carries the template repository identity or citation.

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

Use `type-training` as the single canonical repository-type topic. Add `site-teaching` only when the activity should also be listed on the academic website. Set `integration.profile.include` in `repo.yml` explicitly according to whether the repository should appear in the GitHub academic profile.
