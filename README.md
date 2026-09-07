<img align="right"  src="assets/images/logo.svg" alt="Scientific training logo" width="110">

# Scientific Training Template

<br clear="right">

Reusable structure for scientific teaching and training repositories.

Designed for modular, reproducible delivery of quantitative and computational science material across classes, workshops, short courses, technical training, and semester courses.

<br clear="right"/>

## Repository structure

```text
.
├── template.yml                 # metadata for the template repository
├── repo.yml                     # metadata for a generated teaching repository
├── course.yml                   # teaching-activity metadata
├── _quarto.yml                  # current site configuration
├── index.qmd                    # course landing page
├── syllabus.qmd                 # scope, outcomes, policies
├── schedule.qmd                 # teaching sequence and timing
├── setup.qmd                    # software and prerequisites
│
├── modules/
│   ├── index.qmd
│   └── 01-topic/
│       ├── module.yml           # module metadata
│       ├── index.qmd            # lesson notes
│       ├── slides.qmd           # presentation material
│       ├── lab.qmd              # guided practical work
│       ├── exercise.qmd         # formative exercise
│       └── instructor-notes.md  # delivery notes
│
├── assignments/                 # optional assessed work
├── project/                     # optional applied project
├── resources/                   # readings and supporting material
├── data/                        # small redistributable teaching data
├── code/                        # shared scripts and functions
├── environment/                 # computational-environment files
├── assets/                      # figures and styles
├── docs/                        # template documentation
├── scripts/                     # validation utilities
├── references.bib
├── CITATION.cff
├── CONTRIBUTING.md
└── .github/workflows/publish.yml
```

## Teaching unit

The module is the basic teaching unit. Each module is designed to keep conceptual material, worked examples, practical work, exercises, and instructor notes together.

A typical module follows this sequence:

```text
question or problem
    ↓
learning objectives
    ↓
core concepts
    ↓
worked example
    ↓
guided practice
    ↓
checkpoint
    ↓
independent exercise
    ↓
scientific interpretation
```

This structure is suitable for quantitative ecology, fisheries science, stock assessment, management strategy evaluation, spatio-temporal modelling, programming, and related scientific-computing topics.

## Authoring

Use `.qmd` as the current source format for new material. Retain `.Rmd`, Markdown, LaTeX, notebooks, or other formats only when required by the teaching activity or during migration of existing material.

The repository structure should remain independent of the publishing tool: content, metadata, data, code, and reproducibility files should continue to have clear roles if the rendering system changes in the future.

## Create a teaching repository

1. Select **Use this template → Create a new repository**.
2. Choose a short, descriptive repository name.
3. Replace placeholders in `repo.yml`, `course.yml`, `_quarto.yml`, `CITATION.cff`, and the example module.
4. Add the GitHub topic `type-training`.
5. Add `site-teaching` when the activity should appear on the academic website.
6. Remove optional sections that are not required for the activity.
7. Enable **Settings → Pages → Source = GitHub Actions** in the generated teaching repository.
8. Push to `main`; validation and publication run automatically.

See [`docs/USAGE.md`](docs/USAGE.md) for the operational workflow and [`docs/STRUCTURE.md`](docs/STRUCTURE.md) for the design of the repository.

## Repository roles

The template repository itself uses `type-template`. A repository created from it for an actual teaching activity uses `type-training`.

The template is validated and rendered on each push but is not deployed to GitHub Pages. Generated teaching repositories can be published and linked to `qselmer.github.io/teaching/` and the GitHub academic profile.
