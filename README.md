# Universal Quarto Teaching Template

Reusable teaching infrastructure maintained by **Elmer Quispe-Salazar** for classes, workshops, short courses, seminars, and semester courses.

This repository is the **template source**. Repositories created from it should contain the actual teaching activity and use the GitHub topic `type-training`. The template repository itself remains `type-template`.

## Design goals

The template is built around five principles:

1. **Learning-first structure** — every module starts from questions, learning objectives, prerequisites, and estimated time.
2. **Topic-level modularity** — notes, slides, labs, exercises, and instructor notes for one topic live together.
3. **Reproducible computation** — R, Python, Julia, C++, notebooks, bibliography, code, and small teaching data can coexist in one Quarto project.
4. **Multiple delivery modes** — the same structure works for a single class, workshop, short course, or semester course.
5. **Academic integration** — repository metadata can feed `qselmer.github.io/teaching/` and the GitHub academic profile.

## Repository structure

```text
.
├── template.yml                 # metadata for this template itself
├── repo.yml                     # metadata seed for the generated teaching repository
├── course.yml                   # teaching-activity metadata
├── _quarto.yml                  # Quarto website configuration
├── index.qmd                    # public landing page
├── syllabus.qmd                 # scope, policies, outcomes
├── schedule.qmd                 # timetable / sequence
├── setup.qmd                    # learner setup and prerequisites
│
├── modules/
│   ├── index.qmd
│   └── 01-topic/
│       ├── module.yml           # structured module metadata
│       ├── index.qmd            # lesson / lecture notes
│       ├── slides.qmd           # reveal.js slides
│       ├── lab.qmd              # guided practical
│       ├── exercise.qmd         # formative practice
│       └── instructor-notes.md  # timing, misconceptions, teaching notes
│
├── assignments/                 # optional take-home or assessed work
├── project/                     # optional capstone / applied project
├── resources/                   # readings, links, cheatsheets
├── data/                        # small teaching data only
├── code/                        # reusable scripts/functions
├── environment/                 # reproducibility instructions / lockfiles
├── assets/                      # CSS and images
├── docs/                        # template documentation
├── scripts/                     # validation utilities
├── references.bib
├── CITATION.cff
├── CONTRIBUTING.md
└── .github/workflows/publish.yml
```

## Authoring standard

Use **Quarto `.qmd` as the canonical source format**. Keep `.Rmd` only when migrating legacy material. A module should be self-contained enough to be reused or reordered without reorganizing the entire course.

## Create a new teaching repository

1. Select **Use this template → Create a new repository**.
2. Give the repository a short descriptive name, e.g. `git-github-teaching`, `stock-assessment-teaching`, or `spatial-models-workshop`.
3. Replace placeholders in `repo.yml`, `course.yml`, `_quarto.yml`, `CITATION.cff`, and the `.qmd` files.
4. Add exactly one repository-type topic: `type-training`.
5. Add `site-teaching` when the activity should be listed on the academic website.
6. Add subject topics such as `stock-assessment`, `mse`, `r`, `python`, `spatiotemporal-models`, or `fisheries`.
7. Open **Settings → Pages → Build and deployment → Source = GitHub Actions**.
8. Push to `main`; validation and publication run automatically.

See [`docs/USING_TEMPLATE.md`](docs/USING_TEMPLATE.md) for the full workflow.

## Template behavior

The template repository is validated and rendered on every push but is **not deployed to GitHub Pages**. A repository created from this template will deploy after Pages is enabled.

## Integration

The intended flow is:

```text
teaching repository
      │
      ├── GitHub Pages course site
      ├── qselmer.github.io/teaching/ catalogue entry
      └── qselmer GitHub profile classification
```

See [`docs/INTEGRATION.md`](docs/INTEGRATION.md).
