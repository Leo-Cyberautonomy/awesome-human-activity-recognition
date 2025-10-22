# Kinetics-700

- **Modality:** RGB video (YouTube clips)
- **Primary Tasks:** Large-scale action recognition, transfer learning, pretraining
- **Scale:** ~650k 10s clips, 700 action classes, 650k unique videos
- **License:** Creative Commons Attribution 4.0 (via DeepMind terms)
- **Access:** [https://deepmind.com/research/open-source/kinetics](https://deepmind.com/research/open-source/kinetics)

## Summary
Kinetics-700 extends the original Kinetics dataset with more classes, clips, and improved annotation coverage. Clips are sourced from YouTube and trimmed to roughly 10 seconds, making the dataset ideal for large-scale supervised pretraining and transfer to downstream action recognition tasks.

## Reference Paper
- *Will Kay et al.* "The Kinetics Human Action Video Dataset." arXiv:1705.06950, 2017. [`PDF`](https://arxiv.org/abs/1705.06950)

## Benchmarks & Baselines
- **SlowFast 16x8, ResNet-101** - Top-1: 65.7, Top-5: 86.7 on Kinetics-700; *Feichtenhofer et al., ICCV 2019.*
- **Video Swin Transformer-L** - Top-1: 84.9 on Kinetics-700; *Liu et al., CVPR 2022.*
- Standard evaluation uses the official train/val/test splits released by DeepMind; test labels are withheld and require leaderboard submission.

## Tooling & Ecosystem
- [PyTorchVideo](https://pytorchvideo.org/) provides dataloaders and preprocessing pipelines.
- [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/kinetics700) ships ready-to-use splits.
- [decord](https://github.com/dmlc/decord) + [ffmpeg](https://ffmpeg.org/) recommended for efficient frame loading.
- Community-maintained mirror scripts: [kinetics-downloader](https://github.com/Showmax/kinetics-downloader).

## Known Challenges
- YouTube links periodically expire; expect ~5-10% missing videos per download and rely on fallbacks or mirrors.
- Some actions are visually similar; class confusion demands strong temporal modeling.
- Dataset is English-centric with potential geographic bias in video sources.

## Cite
```
@article{kay2017kinetics,
  title   = {The Kinetics Human Action Video Dataset},
  author  = {Kay, Will and Carreira, Jo{\~a}o and Simonyan, Karen and others},
  journal = {arXiv preprint arXiv:1705.06950},
  year    = {2017}
}
```
