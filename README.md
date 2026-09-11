<img align="right"  src="assets/images/logo.svg" alt="Scientific training logo" width="110">

# Scientific Training<br>Template

<br clear="right">

Reusable structure for scientific teaching and training repositories.

Designed for modular, reproducible delivery of quantitative and computational science material across classes, workshops, short courses, technical training, and semester courses.

<br clear="right"/>

## Repository structure

```text
.
├── template.yml                 # metadata for this template and the type it produces
├── repo.yml                     # canonical metadata for the current repository
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
3. Update the inherited identity in `repo.yml` so the generated repository uses its real owner, name, title, visibility, status, stage, description, URL, and **`type-training`**.
4. Replace the inherited template citation in `CITATION.cff` with the citation metadata for the actual teaching activity.
5. Replace placeholders in `course.yml`, `_quarto.yml`, the example module, and the teaching files.
6. Ensure `repo.yml` contains exactly one canonical `type-*` topic: `type-training`. Add `site-teaching` only when required by the academic website integration.
7. Remove optional sections that are not required for the activity.
8. Enable **Settings → Pages → Source = GitHub Actions** in the generated teaching repository.
9. Push to `main`; validation and publication run automatically.

See [`docs/USAGE.md`](docs/USAGE.md) for the operational workflow and [`docs/STRUCTURE.md`](docs/STRUCTURE.md) for the design of the repository.

## Repository roles

The template repository itself is **`type-template`**. Its root `repo.yml` and `CITATION.cff` therefore describe **this template repository**.

A repository created from it for an actual teaching activity must be converted to **`type-training`** by updating the inherited metadata. The validation workflow intentionally fails if a generated repository keeps the `.template-training` identity or citation.

The template is validated and rendered on each push but is not deployed to GitHub Pages. Generated teaching repositories can be published and linked to the academic website and GitHub profile.

## Metadata

- **Repository type:** `type-template`
- **Status:** `active`
- **Stage:** `stable`
- **Default generated type:** `type-training`
- **Primary authoring framework:** Quarto

## Licensing

The **code, scripts, workflow configuration, and software components** are distributed under the [MIT License](LICENSE).

The **documentation, explanatory text, and original figures** are distributed under [CC BY 4.0](LICENSE-DOCS.md), unless a file explicitly states otherwise.

Teaching datasets are not automatically covered by either license. Each dataset must retain its own access, attribution, use, and redistribution conditions.
