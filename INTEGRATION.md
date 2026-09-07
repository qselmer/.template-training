# Integration contract

## Universal metadata

Every qselmer repository should eventually contain `repo.yml`. It records the canonical repository name, type, status, description, and integration settings.

## GitHub profile

The profile repository should classify repositories using exactly one canonical `type-*` topic. `repo.yml` can be used later as a metadata enrichment source, but the topic remains the authoritative type signal.

## Academic website

Repositories intended for the website should use one `site-*` topic. For teaching repositories use:

```text
type-training
site-teaching
```

The website automation can then discover these repositories, read `repo.yml` and `course.yml`, and generate entries in the website's teaching collection.

## Project Pages

Each teaching repository publishes its own Quarto site with GitHub Pages at:

```text
https://qselmer.github.io/REPO_NAME/
```

The central website `/teaching/` page should link to that course site rather than duplicate all lesson content.
