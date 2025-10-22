# BEHAVE

- **Modality:** RGB-D video, 3D human poses, object meshes, interaction annotations
- **Primary Tasks:** Human-object interaction modeling, contact reasoning, human pose estimation
- **Scale:** 321 sequences, 20 participants, 10 object categories, 12 actions
- **License:** BEHAVE dataset license (research-only, attribution, no redistribution)
- **Access:** [https://virtualhumans.mpi-inf.mpg.de/behave/](https://virtualhumans.mpi-inf.mpg.de/behave/)

## Summary
BEHAVE captures people interacting with everyday objects using synchronized RGB-D cameras and calibrated object meshes. Each sequence includes accurate human pose estimates and contact labels, making it a strong benchmark for modeling physical interactions and learning contact-aware human-object dynamics.

## Reference Paper
- *Minh Vo et al.* "BEHAVE: Dataset and Method for Tracking Human-object Interactions." CVPR, 2022. [`PDF`](https://arxiv.org/abs/2104.02683)

## Benchmarks & Baselines
- **BEHAVE Tracker** - MPJPE: 58 mm, Contact F1: 72.4; *Vo et al., 2022.*
- **GrabNet fine-tuned on BEHAVE** - Contact classification F1: 69.3; demonstrated in supplemental experiments.
- Evaluation metrics emphasize human-object mesh alignment, contact accuracy, and pose errors.

## Tooling & Ecosystem
- Official [BEHAVE toolkit](https://github.com/TimoBolkart/BEHAVE) for downloading, parsing, and visualizing sequences.
- Integrations with [SMPL-X](https://smpl-x.is.tue.mpg.de/) allow joint optimization of body and object poses.
- [ContactOpt](https://github.com/otaheri/ContactOpt) demonstrates physics-aware refinement on BEHAVE sequences.

## Known Challenges
- Requires 300+ GB storage; downloads are per-sequence via Script, so plan for long transfer times.
- Dataset license forbids redistribution; share derived models cautiously.
- Depth sensors introduce noise around reflective objects; incorporate depth filtering for robustness.

## Cite
```
@inproceedings{vo2022behave,
  title     = {BEHAVE: Dataset and Method for Tracking Human-object Interactions},
  author    = {Vo, Minh and Weng, Xulong and Bolkart, Timo and others},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year      = {2022}
}
```
