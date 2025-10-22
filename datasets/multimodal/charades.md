# Charades

- **Modality:** RGB video (crowdsourced indoor scenes), textual scripts, temporal annotations
- **Primary Tasks:** Multi-label action recognition, temporal localization, video question answering
- **Scale:** 9,848 videos, 157 action classes, 66,500 temporal annotations
- **License:** Creative Commons Attribution-NonCommercial 4.0
- **Access:** [https://allenai.org/plato/charades/](https://allenai.org/plato/charades/)

## Summary
Charades captures everyday indoor activities scripted and recorded by crowd workers in their homes. The dataset's multi-label temporal annotations, natural co-occurring actions, and narrative scripts make it a popular benchmark for compositional action recognition and temporal reasoning.

## Reference Paper
- *Gunnar A. Sigurdsson et al.* "Hollywood in Homes: Crowdsourcing Data Collection for Activity Understanding." ECCV, 2016. [`PDF`](https://arxiv.org/abs/1604.01753)

## Benchmarks & Baselines
- **Two-Stream I3D** - mAP: 32.9 on Charades; *Carreira & Zisserman, CVPR 2017.*
- **SlowFast Networks** - mAP: 42.1; *Feichtenhofer et al., ICCV 2019.*
- Evaluation metrics: mean Average Precision (mAP) over classes using provided validation/test splits.

## Tooling & Ecosystem
- Official [Charades evaluation code](https://github.com/gsig/charades-algorithms) including mAP scripts.
- [AVA-Charades](https://github.com/facebookresearch/ava-dataset) merges Charades with AVA annotations for spatio-temporal localization.
- Integration with [PyTorchVideo](https://pytorchvideo.org/) and [MMAction2](https://github.com/open-mmlab/mmaction2).

## Known Challenges
- Videos contain multiple actions simultaneously; multi-label training is essential.
- Long-tail distribution with rare actions; consider focal loss or class-balanced sampling.
- Lighting varies and some actions are subtle (e.g., "drinking" vs. "chewing") requiring temporal context.

## Cite
```
@inproceedings{sigurdsson2016charades,
  title     = {Hollywood in Homes: Crowdsourcing Data Collection for Activity Understanding},
  author    = {Sigurdsson, Gunnar A. and Varol, Gul and Wang, Xiaolong and others},
  booktitle = {European Conference on Computer Vision},
  year      = {2016}
}
```
