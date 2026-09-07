# Using the template

## 1. Create the repository

Use GitHub's **Use this template** function. Do not fork the template for ordinary course creation.

## 2. Configure identity

Replace placeholders in:

- `repo.yml`
- `course.yml`
- `_quarto.yml`
- `CITATION.cff`
- root `.qmd` files
- the first module

Run:

```bash
python scripts/validate_structure.py
```

The copied repository should fail validation until required placeholders are replaced.

## 3. Choose the course shape

### Single class / seminar

Keep one or two modules. Remove Assignments and Project from `_quarto.yml` if unused.

### Workshop / short course

Use multiple modules, explicit breaks in `schedule.qmd`, and labs after short concept blocks.

### Semester course

Use one or more modules per week, retain Assignments, and optionally use the Applied Project section.

## 4. Add modules

Copy `modules/01-topic/`, increment the numeric prefix, and update `module.yml` plus the four learner/instructor files.

## 5. Configure computation

Follow `environment/README.md`. Do not add every language environment by default; use only what the course actually needs.

## 6. Publish

Enable **Settings → Pages → Source = GitHub Actions** once. The workflow builds on pull requests/pushes and deploys `main` automatically.

## 7. Integrate academically

Add `type-training` and `site-teaching` topics and synchronize the public teaching record with `qselmer.github.io/teaching/`.
