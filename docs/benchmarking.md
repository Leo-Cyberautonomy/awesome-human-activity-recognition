# Benchmark Snapshots

High-level view of representative baselines and state-of-the-art (SOTA) models for key datasets. Use this to understand reasonable performance bands before planning experiments.

## Vision Datasets

| Dataset | Metric | Baseline (paper) | SOTA (2024Q1) | Notes |
| --- | --- | --- | --- | --- |
| Kinetics-700 | Top-1 | SlowFast R101 (65.7) | Video Swin-L (84.9) | Pure RGB performance; multimodal models can push higher with audio. |
| NTU RGB+D 120 | CS Top-1 | Shift-GCN (85.9) | MS-G3D-Net (92.7) | Cross-setup SOTA trails by ~2 points; skeleton methods lead. |
| Something-Something V2 | Top-1 | TSM (63.4) | TimesFormer-L (69.7) | Transformers benefit from longer temporal receptive fields (clip len  32). |
| FineGym | Event Top-1 | TSM hierarchy (86.2) | UniFormerV2-L (90.4) | Requires hierarchical loss; using pose priors yields gains on sub-actions. |

## Skeleton & Mocap

| Dataset | Metric | Baseline | SOTA (2024Q1) | Notes |
| --- | --- | --- | --- | --- |
| AMASS | MPJPE  | VPoser prior (70 mm) | MotionDiffuse (42 mm) | Generative diffusion models dominate long sequence synthesis. |
| Human3.6M | MPJPE  | Martinez et al. (67.5 mm) | MixSTE (39.7 mm) | Report protocol; leaderboard splits differ by joints and alignment. |
| BABEL | Segmentation mIOU  | Transformer baseline (77.1) | MotionBERT (84.3) | Text-aligned supervision improves segmentation + retrieval. |
| TotalCapture | MPJPE  | TotalCapture baseline (19 mm) | PoseFormerV3D (13.6 mm) | Multi-view fusion with transformer aggregation leads. |

## Wearable Sensors

| Dataset | Metric | Baseline | SOTA (2024Q1) | Notes |
| --- | --- | --- | --- | --- |
| PAMAP2 | Accuracy | DeepConvLSTM (94.2) | HARFormer (96.8) | Domain augmentation (SpecAugment, jitter) helps >1 point. |
| WISDM | Accuracy | Random Forest (91.7) | SelfHAR (96.1) | Subject splits matter; report LOSO + random for comparability. |
| HAPT | Accuracy | SVM (96.3) | MetaSenseNet (97.5) | Postural transitions remain hardest; model F1 in addition to accuracy. |
| RealWorld HAR | F1 | Position-aware (86.7) | AdaHAR (92.4) | Evaluate across device placements; cross-location generalization critical. |
| OPPORTUNITY | F1 (Gestures) | DeepConvLSTM (70.1) | CPM-Net (77.8) | Data imbalance; class-weighted losses still recommended. |

## Multimodal & Egocentric

| Dataset | Metric | Baseline | SOTA (2024Q1) | Notes |
| --- | --- | --- | --- | --- |
| EPIC-Kitchens-100 | Action mAP | TSN RGB+Flow (38.9) | InternVideo2 (52.6) | Multi-modal (audio/text) pretraining narrows gap. |
| Ego4D | Recall@5 (Episodic) | CLIP retrieval (25.4) | EgoVLP (38.1) | Foundation models fine-tuned on ego data lead. |
| Charades | mAP | Two-Stream I3D (32.9) | XClip (49.5) | Consider multi-label calibration for threshold selection. |
| Ego-Exo4D | Top-1 (Cross-view) | Baseline (46.5) | CrossFormer++ (57.4) | Joint ego-exo transformers are emerging; numbers moving fast. |

## Using This Table
- Cite the relevant paper when referencing SOTA metrics; numbers change quickly.
- Reproduce baselines with provided configs in `tools/` (planned) to validate reproducibility.
- Open an issue tagged `type:benchmark` when updating numbers, including validation logs or leaderboard links.
