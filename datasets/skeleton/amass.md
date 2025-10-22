# AMASS

- **Modality:** Unified MoCap parameter sequences (SMPL/SMPL+H/DMPL parameters)
- **Primary Tasks:** Motion synthesis, pose estimation, imitation learning, generative modeling
- **Scale:** ~16,000 minutes, 344 subjects, 40+ MoCap datasets merged
- **License:** AMASS custom research license (non-commercial, attribution required)
- **Access:** [https://amass.is.tue.mpg.de/](https://amass.is.tue.mpg.de/)

## Summary
AMASS (Archive of Motion Capture as Surface Shapes) consolidates dozens of motion-capture datasets into a common SMPL parameterization, providing temporally consistent body poses and shapes. It serves as a foundational corpus for human motion synthesis and as pretraining data for pose estimation models that operate in parametric body-space.

## Reference Paper
- *Armin Mahmood et al.* "AMASS: Archive of Motion Capture as Surface Shapes." ICCV, 2019. [`PDF`](https://arxiv.org/abs/1904.03278)

## Benchmarks & Baselines
- **VPoser** prior trained on AMASS underpins many downstream pose/shape models; *Mahmood et al., ICCV 2019.*
- **Motion VAE** based on AMASS achieves high-fidelity sequence generation; *Kanazawa et al., CVPR 2019 (HMR follow-ups).*
- No single official leaderboard; evaluations often use training/validation splits by source dataset to prevent leakage.

## Tooling & Ecosystem
- Official [AMASS processing code](https://github.com/nghorbani/amass) for downloading and converting sequences.
- [SMPLify-X](https://github.com/vchoutas/smplify-x) leverages AMASS for pose/shape priors.
- [MoCap Act](https://github.com/abhinavsagar/mocap-act) provides dataset loaders aligned with AMASS segments.

## Known Challenges
- Licensing varies per constituent dataset; ensure you honor original dataset terms when redistributing derivatives.
- Some sequences lack foot-contact labels; contact detection requires post-processing.
- Requires large storage (~43 GB compressed) and relies on SMPL model assets (need separate license from MPI).

## Cite
```
@inproceedings{mahmood2019amass,
  title     = {AMASS: Archive of Motion Capture as Surface Shapes},
  author    = {Mahmood, Armin and Ghorbani, Navid and Pons-Moll, Gerard and others},
  booktitle = {Proceedings of the IEEE International Conference on Computer Vision},
  year      = {2019}
}
```
