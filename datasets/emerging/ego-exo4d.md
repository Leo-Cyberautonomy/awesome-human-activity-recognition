# Ego-Exo4D

- **Modality:** Synchronized egocentric and exocentric RGB video, audio, motion capture, text transcripts
- **Primary Tasks:** Cross-view action understanding, third-person to first-person translation, 4D reconstruction
- **Scale:** 1,422 sequences, 20+ hours ego video, 120+ hours exo video, 40 action categories
- **License:** Research license (non-commercial); requires acceptance through dataset agreement
- **Access:** [https://ego-exo4d-data.org/](https://ego-exo4d-data.org/)

## Summary
Ego-Exo4D presents paired first- and third-person views of skilled human activities with synchronized audio and motion capture. The dataset enables cross-view domain adaptation, egocentric-exocentric translation, and holistic 4D reasoning about interaction-intensive tasks (e.g., cooking, musical performance).

## Reference Paper
- *Hanbyul Joo et al.* "Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-person Perspectives." arXiv, 2023. [`PDF`](https://arxiv.org/abs/2306.08639)

## Benchmarks & Baselines
- **Cross-view Action Recognition Baseline** - Top-1 exo-to-ego: 46.5; *Joo et al., 2023.*
- **Pose Estimation with Motion Capture Supervision** - MPJPE: 28.6 mm for ego/exo fusion.
- Tasks include cross-view action classification, 4D pose reconstruction, and audio-visual alignment; official metrics described in the paper.

## Tooling & Ecosystem
- Official [ego-exo4d toolkit](https://github.com/facebookresearch/ego-exo4d) for download, preprocessing, and baseline models.
- Integration examples for [PyTorch3D](https://pytorch3d.org/) and [Detectron2](https://github.com/facebookresearch/detectron2) provided.
- Compatible with [Ego4D](datasets/multimodal/ego4d.md) metadata schemas for multi-dataset experimentation.

## Known Challenges
- Large data volume and multi-camera synchronization demand significant storage and careful handling of timestamps.
- Licensing prohibits commercial use and redistributing raw footage; review terms before derivative releases.
- Motion capture coverage varies by sequence; some activities have partial mocap data.

## Cite
```
@article{joo2023egoexo4d,
  title   = {Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-person Perspectives},
  author  = {Joo, Hanbyul and Sharma, Gaurav and Vo, Minh and others},
  journal = {arXiv preprint arXiv:2306.08639},
  year    = {2023}
}
```
