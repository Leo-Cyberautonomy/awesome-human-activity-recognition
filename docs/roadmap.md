# Roadmap

This roadmap tracks high-priority milestones to mature the Awesome Human Activity Recognition list into a best-in-class open resource. Timelines are quarter-based targets; adapt as contributors join.

## Q2 2024
- Publish 40+ dataset cards spanning all modalities with canonical references.
- Finalize link validation pipeline (GitHub Action using `lycheeverse/lychee`).
- Launch GitHub Discussions with channels for dataset requests and SOTA tracking.
- Release wearable (PAMAP2) and video (Kinetics-700) quick-start notebooks.

## Q3 2024
- Ship `tools/catalog_builder.py` to aggregate metadata into CSV/JSON for downstream tooling.
- Add baseline reproducibility scripts (PyTorch) covering at least:
  - Skeleton-based GCN on NTU RGB+D 120.
  - Transformer video model on Something-Something V2.
  - Self-supervised wearable baseline on WISDM.
- Publish MkDocs documentation site served via GitHub Pages, synced with repository metadata.
- Introduce monthly digest (via Discussions) summarizing new datasets, papers, and PR highlights.

## Q4 2024
- Expand dataset coverage to synthetic human simulations (e.g., SAPIEN, Habitat, ManiSkill2).
- Integrate automated badge generation (dataset counts, modalities) via GitHub Action + Shields endpoint.
- Provide standardized dataset schema (YAML/JSON) with validation to support API consumers.
- Host community benchmarking challenge (e.g., wearable activity recognition transfer) with partner labs.

## Beyond
- Build interactive web explorer with filtering by modality, license, tasks, and download size.
- Offer dataset health metrics (link uptime, missing files, version notes).
- Collaborate with dataset authors to host official mirrors or metadata updates.
- Explore plugin integrations (Weights & Biases, Hugging Face Datasets) to keep entries live.

Contributors can propose roadmap updates via issues tagged `type:roadmap`. Priorities adjust as the community scales.
