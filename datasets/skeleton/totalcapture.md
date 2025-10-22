# TotalCapture

- **Modality:** Optical motion capture with synchronized multi-view RGB, depth, IMU
- **Primary Tasks:** 3D pose estimation, multi-view reconstruction, IMU-to-mocap fusion
- **Scale:** 5 subjects, 4 camera views, 4 Vicon cameras, 11 sequences per subject
- **License:** Creative Commons Attribution 4.0 (non-commercial recommended)
- **Access:** [http://totalcapture.net/](http://totalcapture.net/)

## Summary
TotalCapture provides high-quality motion capture data aligned with RGB videos, depth maps, and inertial measurements. It is widely used to evaluate multi-view reconstruction and to benchmark IMU fusion algorithms thanks to precise calibration between sensors and mocap ground truth.

## Reference Paper
- *Matthew Trumble et al.* "Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies." IEEE TPAMI, 2019. [`PDF`](https://ieeexplore.ieee.org/document/8419328)

## Benchmarks & Baselines
- **TotalCapture baseline** - MPJPE: 19.0 mm for multi-view reconstruction; *Trumble et al., 2019.*
- **VNect + Fusion** - MPJPE: 28.2 mm when fusing IMU data; *Mehta et al., SIGGRAPH 2017.*
- Standard evaluation splits include *Freestyle*, *Walking*, *Acting*, and *Rom* sequences, often with cross-subject validation.

## Tooling & Ecosystem
- [TotalCapture Toolbox](https://github.com/TotalCapture/TotalCapture) for downloading and preprocessing.
- [OpenPose calibration scripts](https://github.com/CMU-Perceptual-Computing-Lab/openpose) for aligning 2D detections to 3D.
- [IMU-to-mocap fusion frameworks](https://github.com/facebookresearch/BodyPose) leverage TotalCapture for evaluation.

## Known Challenges
- Dataset size is modest; combine with AMASS or Human3.6M for training when possible.
- Calibration metadata requires careful parsing; check camera intrinsics/extrinsics before reprojection.
- IMU data contains drift over long sequences; use provided synchronization markers.

## Cite
```
@article{trumble2019totalcapture,
  title   = {Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies},
  author  = {Trumble, Matthew and Gilbert, Andrew and Hilton, Adrian and others},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year    = {2019}
}
```
