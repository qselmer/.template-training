# Repository structure

The template separates repository metadata, teaching content, computation, assessment, and publication.

## Core layers

### Repository metadata

`template.yml`, `repo.yml`, and `course.yml` describe the template, the generated repository, and the teaching activity. These files should remain independent of the rendering system.

### Course-level material

`index.qmd`, `syllabus.qmd`, `schedule.qmd`, and `setup.qmd` define the public entry point, scope, sequence, and prerequisites.

### Modules

`modules/` is the primary teaching structure. Each module should contain the material required to teach one coherent topic:

```text
modules/01-topic/
├── module.yml
├── index.qmd
├── slides.qmd
├── lab.qmd
├── exercise.qmd
└── instructor-notes.md
```

A module should be sufficiently self-contained to be reordered or reused without reorganising the full course.

## Module sequence

A typical quantitative-science module should progress from a scientific or technical question to interpretation:

```text
question
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
interpretation
```

The exact sequence can be shortened for seminars or expanded for workshops and semester courses.

## Optional components

`assignments/` and `project/` are optional. Remove them from navigation when they are not used.

`resources/`, `data/`, `code/`, and `environment/` support teaching but should not duplicate module content.

## Publishing layer

The current implementation uses Quarto and GitHub Pages. These are implementation choices rather than structural requirements. If the publishing system changes, the metadata, modules, code, data, and reproducibility structure should remain usable.
