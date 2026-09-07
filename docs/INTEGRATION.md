# Academic integration

Teaching repositories connect the source repository, the published teaching site, the academic website, and the GitHub profile.

## Repository

The GitHub repository is the source of record for teaching content, metadata, code, small redistributable data, and revision history.

## Teaching site

The current workflow renders the repository and publishes the generated site through GitHub Pages.

```text
https://qselmer.github.io/REPO_NAME/
```

The teaching site is intended for learners and should remain focused on the activity itself.

## Academic website

`qselmer.github.io/teaching/` acts as the catalogue of teaching activities. Each verified activity should have a concise record linking to the repository and, when available, the published teaching site.

## GitHub profile

Use one canonical repository-type topic:

```text
type-training
```

Use:

```text
site-teaching
```

when the activity should also appear in the website catalogue.

## Metadata

`repo.yml` describes repository-level metadata and integration behaviour. `course.yml` describes the teaching activity. `module.yml` describes an individual teaching module.
