"""
Normalize Markdown files to ASCII by removing typographic characters.

This helper is intended for maintainers to keep dataset cards consistent with
the repository guideline of defaulting to ASCII. It replaces common punctuation
variants and strips diacritics while leaving Markdown syntax untouched.
Localized files under `i18n/` are intentionally skipped.
"""

from __future__ import annotations

import argparse
import unicodedata
from pathlib import Path
from typing import Dict

DEFAULT_REPLACEMENTS: Dict[str, str] = {
    "–": "-",
    "—": "-",
    "−": "-",
    "‑": "-",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "…": "...",
    "•": "-",
    "·": "-",
    "–": "-",
    "—": "-",
    "™": "TM",
    "°": " deg ",
    "\u00a0": " ",
    "\u202f": " ",
}


def normalize_text(text: str, replacements: Dict[str, str]) -> str:
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    normalized = unicodedata.normalize("NFKD", text)
    return normalized.encode("ascii", "ignore").decode("ascii")


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize Markdown files to ASCII.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Files or directories to process. Defaults to repository root.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files that would change without modifying them.",
    )
    args = parser.parse_args()

    changed = []
    targets = []
    for raw in args.paths:
        path = Path(raw)
        if path.is_dir():
            targets.extend(
                md
                for md in path.rglob("*.md")
                if "i18n" not in md.parts  # keep localized files untouched
            )
        elif path.suffix.lower() == ".md":
            if "i18n" not in path.parts:
                targets.append(path)

    skip_files = {Path("README.md").resolve()}

    for md_file in targets:
        if md_file.resolve() in skip_files:
            continue
        original = md_file.read_text(encoding="utf-8")
        normalized = normalize_text(original, DEFAULT_REPLACEMENTS)
        if normalized != original:
            changed.append(md_file)
            if not args.dry_run:
                md_file.write_text(normalized, encoding="utf-8")

    if changed:
        print("Normalized files:")
        for path in changed:
            print(f" - {path}")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
