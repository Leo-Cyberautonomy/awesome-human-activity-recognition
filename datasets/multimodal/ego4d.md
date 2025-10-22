# Ego4D

- **Modality:** Egocentric RGB video (mono + stereo), audio, IMU, eye gaze, depth (subset)
- **Primary Tasks:** Episodic memory, social interactions, audio-visual diarization, hand-object interaction, forecasting
- **Scale:** 3,000+ hours, 74 indoor/outdoor environments, 9 countries, 826 participants
- **License:** Ego4D data use agreement (non-commercial research, requires acceptance via CodaLab)
- **Access:** [https://ego4d-data.org/docs/data/](https://ego4d-data.org/docs/data/)

## Summary
Ego4D is the largest open egocentric video dataset to date, capturing daily-life activities with synchronized audio, IMU, gaze, and multi-view recordings. It supports five core benchmark tasks spanning episodic memory, social interactions, audio-visual diarization, hand-object interaction, and future anticipation.

## Reference Paper
- *Kristen Grauman et al.* "Ego4D: Around the World in 2,250 Hours of Egocentric Video." CVPR, 2022. [`PDF`](https://arxiv.org/abs/2110.07058)

## Benchmarks & Baselines
- **Episodic Memory (Recall)** - Baseline TOP-1: 15.6% using CLIP-based retrieval; *Grauman et al., 2022.*
- **Forecasting (Hand-Object Interaction)** - Baseline mAP: 17.2; *Grauman et al., 2022.*
- Leaderboards hosted on [EvalAI](https://eval.ai/web/challenges/challenge-page/1618) per benchmark task.

## Tooling & Ecosystem
- Official [ego4d-toolbox](https://github.com/facebookresearch/Ego4d) for dataset download, preprocessing, and baseline models.
- [Point-Owl](https://github.com/facebookresearch/Ego4d/tree/main/point_owl) for multi-task training on ego4D.
- [PyTorchVideo integration](https://pytorchvideo.org/docs/tutorial_ego4d) provides dataloaders and transforms.

## Known Challenges
- Large storage footprint (~1.4 PB uncompressed); plan selective download via official CLI to target benchmarks.
- Licensing prohibits commercial use; requires maintaining participant privacy (face blurring in some sequences).
- Annotation heterogeneity-each benchmark uses different metadata formats; rely on official parsers.

## Cite
```
@inproceedings{grauman2022ego4d,
  title     = {Ego4D: Around the World in 2,250 Hours of Egocentric Video},
  author    = {Grauman, Kristen and Westbury, Andrew and Byrne, Eugene and others},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year      = {2022}
}
```
