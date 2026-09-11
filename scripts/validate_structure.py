#!/usr/bin/env python3
"""Validate the scientific training template and repositories generated from it."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "repo.yml",
    "course.yml",
    "_quarto.yml",
    "index.qmd",
    "syllabus.qmd",
    "schedule.qmd",
    "setup.qmd",
    "modules/index.qmd",
    "modules/01-topic/module.yml",
    "modules/01-topic/index.qmd",
    "modules/01-topic/slides.qmd",
    "modules/01-topic/lab.qmd",
    "modules/01-topic/exercise.qmd",
    "references.bib",
    "CITATION.cff",
    "LICENSE",
    "LICENSE-DOCS.md",
]

PLACEHOLDERS = [
    "REPO_NAME",
    "COURSE_TITLE",
    "SHORT_TITLE",
    "SHORT_DESCRIPTION",
    "COURSE_TYPE",
    "DELIVERY_MODE",
    "AUDIENCE",
    "LEVEL",
    "YYYY-MM-DD",
    "TOPIC_TITLE",
]

PLACEHOLDER_FILES = [
    "course.yml",
    "_quarto.yml",
    "modules/01-topic/module.yml",
]


def load_yaml(relative_path: str) -> dict:
    path = ROOT / relative_path
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def type_topics(topics: list) -> list[str]:
    return [str(topic) for topic in (topics or []) if str(topic).startswith("type-")]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--template",
        action="store_true",
        help="Validate qselmer/.template-training itself rather than a generated training repository.",
    )
    args = parser.parse_args()

    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if args.template and not (ROOT / "template.yml").is_file():
        missing.append("template.yml")

    errors: list[str] = []
    if missing:
        errors.extend(f"missing required file: {path}" for path in missing)

    if not missing:
        repo_meta = load_yaml("repo.yml")
        repo = repo_meta.get("repository", {})
        integration = repo_meta.get("integration", {})

        if repo_meta.get("schema_version") != 2:
            errors.append("repo.yml: schema_version must be 2")

        if args.template:
            expected = {
                "owner": "qselmer",
                "name": ".template-training",
                "title": "Scientific Training Template",
                "type": "type-template",
                "status": "active",
                "stage": "stable",
                "visibility": "public",
            }
            for key, value in expected.items():
                if repo.get(key) != value:
                    errors.append(f"repo.yml: repository.{key} must be {value!r}")

            if type_topics(repo.get("topics", [])) != ["type-template"]:
                errors.append("repo.yml: exactly one canonical type topic, 'type-template', is required")

            if integration.get("profile", {}).get("include") is not True:
                errors.append("repo.yml: integration.profile.include must be true")

            expected_url = "https://github.com/qselmer/.template-training"
            if integration.get("repository_url") != expected_url:
                errors.append(f"repo.yml: integration.repository_url must be {expected_url!r}")

            template = load_yaml("template.yml").get("template", {})
            template_expected = {
                "owner": "qselmer",
                "repository": ".template-training",
                "type": "type-template",
                "produces": "type-training",
            }
            for key, value in template_expected.items():
                if template.get(key) != value:
                    errors.append(f"template.yml: template.{key} must be {value!r}")

            citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
            if "COURSE_TITLE" in citation or "REPO_NAME" in citation:
                errors.append("CITATION.cff: template citation must not contain generated-course placeholders")
        else:
            for rel in PLACEHOLDER_FILES:
                text = (ROOT / rel).read_text(encoding="utf-8")
                for token in PLACEHOLDERS:
                    if token in text:
                        errors.append(f"{rel}: unresolved placeholder {token}")

            if repo.get("type") != "type-training":
                errors.append("repo.yml: generated repositories must use repository.type 'type-training'")
            if repo.get("name") == ".template-training" or repo.get("title") == "Scientific Training Template":
                errors.append("repo.yml: replace the inherited template identity with the training repository identity")
            if not repo.get("stage"):
                errors.append("repo.yml: repository.stage is required")
            if type_topics(repo.get("topics", [])) != ["type-training"]:
                errors.append("repo.yml: generated repositories require exactly one canonical type topic, 'type-training'")
            if integration.get("profile", {}).get("include") not in (True, False):
                errors.append("repo.yml: integration.profile.include must be boolean")

            github_repository = os.getenv("GITHUB_REPOSITORY")
            if github_repository and "/" in github_repository:
                owner, name = github_repository.split("/", 1)
                if repo.get("owner") != owner or repo.get("name") != name:
                    errors.append("repo.yml: repository.owner/name must match GITHUB_REPOSITORY")

            citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
            if "qselmer/.template-training" in citation or "Scientific Training Template" in citation:
                errors.append("CITATION.cff: replace the inherited template citation with the training activity citation")

    if errors:
        print("Training repository validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Training repository validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
