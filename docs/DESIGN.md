# Design rationale

This template combines patterns observed across mature public teaching infrastructures and quantitative-science repositories rather than reproducing any single course design.

## Benchmarked patterns

### The Carpentries Workbench

Useful patterns adopted:

- explicit setup before the lesson;
- learner questions and observable objectives per teaching unit;
- modular episodes;
- instructor-facing notes;
- automated build/validation;
- accessibility as part of the lesson infrastructure.

References:
- https://carpentries.github.io/workbench/
- https://github.com/carpentries/workbench-template-rmd

### Quarto university course sites

Useful patterns adopted:

- a course site generated from source-controlled `.qmd`;
- separate syllabus, schedule, setup, and learning materials;
- HTML-first publication with the option for PDF/slides/notebooks;
- structured schedules and reproducible publishing.

References:
- https://github.com/berkeley-cdss/course-site-quarto
- https://github.com/Pakillo/quarto-course-website-template

### Posit / RStudio workshop repositories

Useful patterns adopted:

- explicit audience and time commitment;
- clear learning outcomes;
- separation between conceptual material, slides, and applied work;
- practical sessions as central learning components.

Reference:
- https://github.com/rstudio-conf-2022/intro-to-tidyverse

### Quantitative ecology teaching

Useful patterns adopted:

- pre-class preparation;
- individual and group/application work;
- in-class activities linked to quantitative concepts;
- authentic datasets and scientific interpretation.

Example:
- https://michaelfrancenelson.github.io/intro_quant_ecol/

### Fisheries quantitative methods / James Thorson ecosystem

The VAST/FishStats ecosystem emphasizes multiple learning entry points: user manuals, high-level functions, examples, publications, talks, issue history, and training classes. The template therefore treats slides as only one component and prioritizes worked examples, labs, diagnostics, documentation, and reusable resources.

Reference:
- https://github.com/James-Thorson-NOAA/VAST

## Resulting teaching model

Each module follows:

```text
scientific question
      ↓
learning objectives
      ↓
minimal concepts
      ↓
worked example
      ↓
guided practice / lab
      ↓
checkpoint
      ↓
independent exercise
      ↓
scientific interpretation
```

This sequence is intentionally usable for fisheries science, quantitative marine ecology, stock assessment, MSE, spatio-temporal modelling, programming, and general scientific computing.
