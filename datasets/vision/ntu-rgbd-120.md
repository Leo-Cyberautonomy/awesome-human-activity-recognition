# NTU RGB+D 120

- **Modality:** RGB video, depth maps, 3D skeleton sequences (Microsoft Kinect V2)
- **Primary Tasks:** 3D action recognition, skeleton-based recognition, cross-view transfer
- **Scale:** 114,480 trimmed sequences, 120 action classes, 106 subjects, 32 setups
- **License:** Research-only; requires signing usage agreement with NTU RGB+D team
- **Access:** [http://rose1.ntu.edu.sg/datasets/actionrecognition.asp](http://rose1.ntu.edu.sg/datasets/actionrecognition.asp)

## Summary
NTU RGB+D 120 expands the seminal NTU-60 dataset with new action classes, subjects, and capture setups. Each recording provides synchronized RGB, depth, infrared, and skeleton data, supporting both vision-based and graph convolution approaches to 3D action recognition.

## Reference Paper
- *J. Liu et al.* "NTU RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Understanding." IEEE TPAMI, 2020. [`PDF`](https://arxiv.org/abs/1905.04757)

## Benchmarks & Baselines
- **Two-Stream Adaptive GCN** - Cross-Subject Top-1: 86.3%, Cross-Setup Top-1: 88.9%; *Liu et al., CVPR 2019.*
- **Shift-GCN** - Cross-Subject Top-1: 85.9%, Cross-Setup Top-1: 87.6%; *Cheng et al., CVPR 2020.*
- Official evaluation splits: *Cross-Subject* and *Cross-Setup*. Recent works often report *Cross-View* as well.

## Tooling & Ecosystem
- [OpenMMLab's MMAction2](https://github.com/open-mmlab/mmaction2) includes dataloaders and benchmarking configs.
- [PyTorch Geometric Temporal](https://pytorch-geometric-temporal.readthedocs.io/) has skeleton-based examples.
- [ntu-download-scripts](https://github.com/shahroudy/nturgb_d_skeleton) host utilities for downloading and parsing skeleton data.

## Known Challenges
- Access requires manual approval and file hosting uses split `.zip` archives; downloads can be slow.
- Skeleton annotations use Kinect joint order; conversions to SMPL or CMU indexes require mapping scripts.
- Class imbalance exists for infrequent "interaction" actions; consider reweighting.

## Cite
```
@article{liu2020nturgbd120,
  title   = {NTU RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Understanding},
  author  = {Liu, Jun and Shahroudy, Amir and Perez, Mauricio and others},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year    = {2020}
}
```
