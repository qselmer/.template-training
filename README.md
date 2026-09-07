# COURSE_TITLE

Teaching repository maintained by **Elmer Quispe-Salazar**.

- Course site: https://qselmer.github.io/REPO_NAME/
- Academic website: https://qselmer.github.io
- Repository type: `type-training`
- Website integration topic: `site-teaching`

## Repository structure

```text
.
├── repo.yml                 # universal repository metadata
├── course.yml               # teaching-specific metadata
├── _quarto.yml              # Quarto website configuration
├── index.qmd                # course landing page
├── syllabus.qmd             # syllabus / course plan
├── lessons/                 # full lesson notes
├── slides/                  # reveal.js slides
├── exercises/               # student exercises
├── solutions/               # instructor solutions
├── resources/               # readings and supporting resources
├── data/                    # small teaching datasets only
├── assets/                  # images and CSS
└── .github/workflows/       # validation and GitHub Pages publication
```

## Authoring standard

New teaching content should be written in **Quarto `.qmd`**. `.Rmd` is accepted only for legacy material that has not yet been migrated. Quarto is the canonical format because it supports R, Python, Julia, C++, executable notebooks, HTML pages, and reveal.js slides in one project.

## Template behavior

This repository is the **source template**, not a published course. Its GitHub Action renders the Quarto project on every push to verify that the template remains valid, but it deliberately does **not deploy this template repository to GitHub Pages**.

For a repository created from this template, the same workflow will publish the rendered `_site` directory after GitHub Pages has been enabled for that new repository.

## After creating a course repository from this template

1. Replace all placeholders in `repo.yml`, `course.yml`, `_quarto.yml`, `README.md`, and the `.qmd` files.
2. Add exactly one repository-type topic: `type-training`.
3. Add the website-integration topic: `site-teaching`.
4. Add subject-specific topics such as `git`, `stock-assessment`, `r`, `python`, or `spatiotemporal-models` as appropriate.
5. Open **Settings → Pages → Build and deployment** and set **Source = GitHub Actions**.
6. Push to `main` or run **Actions → Publish course site → Run workflow**.
7. Confirm that the course is published at `https://qselmer.github.io/REPO_NAME/`.
8. Add or synchronize the corresponding teaching record in `qselmer.github.io/teaching/` so the academic website acts as the central catalogue.

## Integration

This repository pattern connects three surfaces:

1. **Repository:** source material, metadata, teaching code, exercises, and version history.
2. **Academic website:** central teaching record and link to the published course site.
3. **GitHub profile:** automatic classification through the `type-training` topic and repository metadata.

The universal `repo.yml` file is intended to become the metadata contract used across all qselmer repositories, not only teaching repositories.
