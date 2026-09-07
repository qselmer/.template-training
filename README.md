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
└── .github/workflows/       # automatic GitHub Pages publication
```

## Authoring standard

New teaching content should be written in **Quarto `.qmd`**. `.Rmd` is accepted only for legacy material that has not yet been migrated. Quarto is the canonical format because it supports R, Python, Julia, C++, executable notebooks, HTML pages, and reveal.js slides in one project.

## Integration

This repository is designed to connect to three surfaces:

1. **Repository:** source material and version history.
2. **Academic website:** public teaching record and course link.
3. **GitHub profile:** automatic classification through the `type-training` topic.

The universal `repo.yml` file is intended to become the metadata contract used across all qselmer repositories, not only teaching repositories.
