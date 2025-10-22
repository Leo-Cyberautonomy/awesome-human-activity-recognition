# Tooling Overview

Utilities that keep the Awesome Human Activity Recognition list healthy. Scripts here are optional helpers for local validation and catalog generation.

## Link Validation
- `validate_links.ps1`  
  Runs [`lychee`](https://github.com/lycheeverse/lychee) against all Markdown files.  
  Usage:
  ```powershell
  # First run installs lychee locally inside tools/bin
  pwsh tools/validate_links.ps1 -Install
  # Subsequent runs
  pwsh tools/validate_links.ps1
  ```

## Catalog Builder (alpha)
- `catalog_builder.py`  
  Generates a machine-readable snapshot (JSON) of dataset metadata grouped by modality.
  ```powershell
  python tools/catalog_builder.py --output data/catalog.json
  ```
  Current output is a modality -> datasets map with bullet metadata. Planned upgrades include schema validation and CSV/Markdown exports.

## Formatting Utilities
- `normalize_ascii.py`  
  Normalizes Markdown files to ASCII, replacing typographic punctuation and stripping diacritics to match repository style.
  ```powershell
  python tools/normalize_ascii.py
  python tools/normalize_ascii.py datasets/vision --dry-run
  ```

## Planned Utilities
- `dataset_schema.json` - JSON Schema definition to lint dataset cards (front-matter metadata).
- Notebook templates (wearable + video) demonstrating baseline training with curated configs.

Contribute new tooling via issues labeled `type:tooling` and follow the contributing guide for validation and documentation.
