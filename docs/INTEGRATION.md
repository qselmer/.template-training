# Academic integration

Teaching repositories have three public roles.

## 1. Repository

The GitHub repository is the source of truth for teaching content, metadata, code, small redistributable data, and revision history.

## 2. Course site

GitHub Actions renders Quarto to GitHub Pages:

```text
https://qselmer.github.io/REPO_NAME/
```

The course site serves learners. It should not duplicate the full academic biography or website navigation.

## 3. Academic website

`qselmer.github.io/teaching/` is the central academic catalogue. It should contain one concise record per verified teaching activity and link to the course site and repository.

## 4. GitHub profile

The profile classifies repositories using the canonical GitHub topic:

```text
type-training
```

Use:

```text
site-teaching
```

when the course should also appear in the website teaching catalogue.

## Metadata contract

`repo.yml` identifies the repository and integration behavior. `course.yml` describes the actual teaching activity. Module-specific structure belongs in `module.yml`.
