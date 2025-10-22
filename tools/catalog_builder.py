"""
Catalog Builder
---------------

Parses dataset cards to produce machine-readable summaries (JSON/CSV).
This scaffolding will be expanded in Q3 2024 to support automated stats,
Shields badges, and documentation exports.

Current capabilities:
- Enumerates Markdown files under datasets/ grouped by modality.
- Extracts front-matter style key-value pairs (future enhancement).
- Prints a simple report (dataset count per modality).
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

DATASET_ROOT = Path(__file__).resolve().parents[1] / "datasets"
MODALITIES = ["vision", "skeleton", "wearable", "multimodal", "emerging"]


def collect_dataset_files() -> Dict[str, List[Path]]:
    """Return mapping of modality -> list of dataset Markdown files."""
    catalog: Dict[str, List[Path]] = defaultdict(list)
    for modality in MODALITIES:
        folder = DATASET_ROOT / modality
        if not folder.exists():
            continue
        for md_file in sorted(folder.glob("*.md")):
            if md_file.name.startswith("_"):
                continue
            catalog[modality].append(md_file)
    return dict(catalog)


def extract_title(markdown: Path) -> str:
    """Grab the first level-1 heading as the dataset title."""
    for line in markdown.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return markdown.stem.replace("-", " ").title()


HEADER_PATTERN = re.compile(r"^- \*\*(?P<key>[^*:\n]+):\*\*\s*(?P<value>.+)$")


def extract_metadata(markdown: Path) -> Dict[str, str]:
    """
    Extract simple key/value metadata from the bullet list in each card.

    Example:
    - **Modality:** RGB video
    """
    metadata: Dict[str, str] = {}
    for line in markdown.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        match = HEADER_PATTERN.match(text)
        if match:
            metadata[match.group("key").strip().lower()] = match.group("value").strip()
        # stop at the first blank line after metadata block
        if metadata and not text:
            break
    metadata.setdefault("title", extract_title(markdown))
    return metadata


def build_catalog() -> Dict[str, List[Dict[str, str]]]:
    catalog = {}
    for modality, files in collect_dataset_files().items():
        catalog[modality] = [extract_metadata(md) for md in files]
    return catalog


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate dataset catalog exports.")
    parser.add_argument(
        "--format",
        choices=["json"],
        default="json",
        help="Output format. CSV/Markdown planned for future releases.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output path. Defaults to stdout.",
    )
    args = parser.parse_args()

    catalog = build_catalog()
    output = json.dumps(catalog, indent=2, sort_keys=True)

    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
