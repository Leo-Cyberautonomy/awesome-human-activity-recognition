# Human3.6M

- **Modality:** Optical motion capture (3D joint positions) + high-resolution RGB + depth + ground-truth camera calibration
- **Primary Tasks:** 3D human pose estimation, pose forecasting, mocap to image alignment
- **Scale:** 3.6 million 3D frames, 11 professional actors, 15 activity scenarios, 4 synchronized cameras
- **License:** Research-only; requires signed license agreement with the Human3.6M consortium
- **Access:** [http://vision.imar.ro/human3.6m/description.php](http://vision.imar.ro/human3.6m/description.php)

## Summary
Human3.6M is a cornerstone benchmark for monocular and multi-view 3D pose estimation. Captured with Vicon mocap and synchronized video, it provides high-quality ground-truth joint trajectories aligned to RGB frames, enabling supervised training and precise evaluation of 3D human reconstruction methods.

## Reference Paper
- *Catalin Ionescu et al.* "Human3.6M: Large Scale Datasets and Predictive Methods for 3D Human Sensing in Natural Environments." IEEE TPAMI, 2014. [`PDF`](https://ieeexplore.ieee.org/document/6639312)

## Benchmarks & Baselines
- **Martinez et al. (Simple Baseline)** - MPJPE 67.5 mm (procrustes-aligned) on Protocol #2.
- **PoseFormer** - MPJPE 44.3 mm on Protocol #1; *Zheng et al., ICCV 2021.*
- Evaluation protocols commonly reported: Protocol #1 (17 joints, MPJPE), Protocol #2 (Procrustes-aligned MPJPE), Protocol #3 (prediction on unnormalized coordinates).

## Tooling & Ecosystem
- Official toolkit with MATLAB evaluation scripts available upon request.
- [Human3.6M Toolkit](https://github.com/una-dinosauria/3d-pose-baseline) for data preprocessing and baseline models.
- [MMPose](https://github.com/open-mmlab/mmpose) maintains configs and evaluation utilities.

## Known Challenges
- Data access approval may take several days; download links can be slow.
- Mixed lighting conditions and motion blur challenge monocular models.
- Protocol confusion is common-explicitly document which evaluation protocol you follow.

## Cite
```
@article{ionescu2014human3,
  title   = {Human3.6M: Large Scale Datasets and Predictive Methods for 3D Human Sensing in Natural Environments},
  author  = {Ionescu, Catalin and Papava, Dragos and Olaru, Vlad and Sminchisescu, Cristian},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year    = {2014}
}
```
