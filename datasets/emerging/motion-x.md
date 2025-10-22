# Motion-X

- **Modality:** Unified full-body motion capture with synchronized hands, face, audio, and inertial sensors
- **Primary Tasks:** Whole-body motion synthesis, human-object interaction, multi-actor coordination
- **Scale:** 10 subjects, 7 sensing modalities, 2 million frames, 330 motion categories
- **License:** Research license (non-commercial); request via dataset maintainers
- **Access:** [https://caizhongang.github.io/projects/Motion-X/](https://caizhongang.github.io/projects/Motion-X/)

## Summary
Motion-X integrates optical motion capture, IMU, hand pose, and facial expression data into a single normalized format (SMPL-X parameters). The dataset covers collaborative tasks, daily activities, and object interactions, offering dense annotations for developing whole-body generative models and cross-modal fusion techniques.

## Reference Paper
- *Zhongang Cai et al.* "Motion-X: A Large-scale 4D Human Motion Dataset." 2023. [`PDF`](https://arxiv.org/abs/2305.13180)

## Benchmarks & Baselines
- **Motion-X Variational Autoencoder** - Reconstruction MPJPE: 23.4 mm; *Cai et al., 2023.*
- **InterHuman** transfer - Contact F1: 74.1 when fine-tuned on Motion-X sequences.
- Benchmark protocol evaluates MPJPE and acceleration error on separated validation sets; follow official splits.

## Tooling & Ecosystem
- Official [Motion-X toolkit](https://github.com/caizhongang/Motion-X) for downloading, processing, and visualizing sequences.
- Works with [SMPL-X body model](https://smpl-x.is.tue.mpg.de/) and integrates with PyTorch3D pipelines.
- Community conversions available for Blender and Unreal Engine to support animation and robotics downstream tasks.

## Known Challenges
- Dataset release includes large `.npz` bundles (hundreds of GB); ensure ample disk space and use resumable downloads.
- Requires SMPL-X model license to interpret body parameters fully.
- Multi-actor sequences have occlusion and interaction complexity; models must reason about contacts and collisions.

## Cite
```
@article{cai2023motionx,
  title   = {Motion-X: A Large-scale 4D Human Motion Dataset},
  author  = {Cai, Zhongang and Leng, Zekun and Shuai, Guanbin and others},
  journal = {arXiv preprint arXiv:2305.13180},
  year    = {2023}
}
```
