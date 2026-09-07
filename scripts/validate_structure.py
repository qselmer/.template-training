#!/usr/bin/env python3
"""Validate the qselmer teaching-template structure using only the Python standard library."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

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
    "repo.yml",
    "course.yml",
    "_quarto.yml",
    "CITATION.cff",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--template",
        action="store_true",
        help="Allow template placeholders (used only in qselmer/.template-training).",
    )
    args = parser.parse_args()

    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"  - {path}")
        return 1

    if not args.template:
        unresolved: list[tuple[str, str]] = []
        for rel in PLACEHOLDER_FILES:
            text = (ROOT / rel).read_text(encoding="utf-8")
            for token in PLACEHOLDERS:
                if token in text:
                    unresolved.append((rel, token))
        if unresolved:
            print("Unresolved required placeholders:")
            for rel, token in unresolved:
                print(f"  - {rel}: {token}")
            return 1

    print("Teaching repository structure is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
