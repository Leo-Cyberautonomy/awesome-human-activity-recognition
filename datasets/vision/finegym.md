# FineGym

- **Modality:** RGB video (broadcast sports footage)
- **Primary Tasks:** Fine-grained action recognition, temporal localization, event detection
- **Scale:** 32,000 video segments, 300 gymnastics events, multi-level annotations
- **License:** Research-only; follows YouTube/host platform terms
- **Access:** [https://sdolivia.github.io/FineGym/](https://sdolivia.github.io/FineGym/)

## Summary
FineGym focuses on Olympic gymnastics with hierarchical annotations capturing routines, sub-actions, and body movements. Its structured labels facilitate fine-grained recognition and temporal parsing, making it a benchmark for high-resolution sports understanding and compositional action modeling.

## Reference Paper
- *Qiuhong Shao et al.* "FineGym: A Hierarchical Video Dataset for Fine-grained Action Understanding." CVPR, 2020. [`PDF`](https://openaccess.thecvf.com/content_CVPR_2020/papers/Shao_FineGym_A_Hierarchical_Video_Dataset_for_Fine-Grained_Action_Understanding_CVPR_2020_paper.pdf)

## Benchmarks & Baselines
- **TSM + Hierarchical Parsing** - Top-1 Event: 86.2, Action: 79.5; *Shao et al., 2020.*
- **MS-TCN** - Temporal localization mAP@0.5: 60.3; applied to FineGym splits.
- Evaluation uses train/val/test splits for floor, vault, uneven bars, and balance beam events.

## Tooling & Ecosystem
- Official [FineGym toolkit](https://github.com/dementrock/FineGym) for data parsing and annotation alignment.
- [TransFG](https://github.com/Tsinghua-MARS-Lab/transfg) demonstrates transformer-based fine-grained recognition using FineGym.
- [MMAction2](https://github.com/open-mmlab/mmaction2) integrates FineGym dataloaders and configs.

## Known Challenges
- Licensing inherits YouTube policies; download links can expire, requiring manual refresh.
- Class distribution is imbalanced across apparatus types and sub-actions.
- Temporal annotations require precise start/end alignment; ensure consistent frame rates.

## Cite
```
@inproceedings{shao2020finegym,
  title     = {FineGym: A Hierarchical Video Dataset for Fine-grained Action Understanding},
  author    = {Shao, Qiuhong and Zhang, Junjie and Wu, Zhizhong and others},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year      = {2020}
}
```
