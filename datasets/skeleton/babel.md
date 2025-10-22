# BABEL

- **Modality:** Motion capture sequences with SMPL parameters, natural language labels, action segmentation
- **Primary Tasks:** Motion-language alignment, action segmentation, motion synthesis, retrieval
- **Scale:** 43 hours of motion, 3.7k sequences, 250 action classes, dense textual annotations
- **License:** BABEL research license (non-commercial, attribution)
- **Access:** [https://babel.is.tue.mpg.de/](https://babel.is.tue.mpg.de/)

## Summary
BABEL enriches AMASS motion data with temporally localized action labels and free-form text descriptions, enabling cross-modal learning between motion and language. It supports research in sequence segmentation, motion captioning, and retrieval that bridges mocap with semantic understanding.

## Reference Paper
- *Pavlakos et al.* "BABEL: Bodies, Actions and Behavior with English Labels." CVPR, 2022. [`PDF`](https://arxiv.org/abs/2106.09699)

## Benchmarks & Baselines
- **Transformer Segmentation** - mIOU: 77.1 for action segmentation; *Pavlakos et al., 2022.*
- **Motion-to-Text Retrieval** - R@1: 31.6; *Pavlakos et al., 2022.*
- Evaluation protocols include seen/unseen subject splits and long vs. short sequence breakdowns.

## Tooling & Ecosystem
- Official [BABEL toolkit](https://github.com/jihoonerd/babel) for downloading metadata and aligning with AMASS sequences.
- [Text2Poser](https://github.com/Mathux/exbody) demonstrates motion-language modeling using BABEL.
- Integrates smoothly with [SMPL-X](https://smpl-x.is.tue.mpg.de/) and downstream generative models.

## Known Challenges
- Requires prior access to AMASS data; ensure both licenses are met.
- Text annotations contain free-form phrasing; preprocessing (lemmatization, synonyms) improves alignment.
- Some sequences have overlapping labels; segmentation tasks must handle multi-label intervals.

## Cite
```
@inproceedings{pavlakos2022babel,
  title     = {BABEL: Bodies, Actions and Behaviors with English Labels},
  author    = {Pavlakos, Georgios and Choutas, Vasileios and Bolkart, Timo and others},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year      = {2022}
}
```
