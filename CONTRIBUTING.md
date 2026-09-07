# Contributing

Contributions should improve clarity, reproducibility, or instructional value without weakening the repository structure.

## Teaching content

- Keep modules self-contained and numerically ordered.
- State learning objectives in observable terms.
- Distinguish explanation, worked examples, guided practice, and independent exercises.
- Update references when scientific or technical content changes.
- Do not include confidential assessments, student information, credentials, or restricted data.

## Code and data

- Prefer small reproducible examples.
- Document dependencies, assumptions, inputs, outputs, and data provenance.
- Keep shared code in `code/`; keep module-specific code with the module when portability is more useful.
- Commit only small, redistributable teaching datasets.

## Validation

Before merging changes, run:

```bash
python scripts/validate_structure.py
quarto render
```

## Accessibility

Use informative alternative text, descriptive links, hierarchical headings, and simple tables. Do not rely on colour alone to communicate information.
