# EPIC-Kitchens-100

- **Modality:** Egocentric RGB video, multi-channel audio, narrative annotations
- **Primary Tasks:** Action recognition (verb/noun/interaction), anticipation, detection, audio-visual learning
- **Scale:** 700+ hours, 100 kitchens, 45 million frames, 97 participants, 90 verb / 300 noun classes
- **License:** Non-commercial research license; requires agreement with EPIC-Kitchens consortium
- **Access:** [https://epic-kitchens.github.io/2021](https://epic-kitchens.github.io/2021)

## Summary
EPIC-Kitchens-100 extends the original EPIC-Kitchens dataset with additional hours of cooking activity, richer annotations, and new benchmarks. Recordings are captured with head-mounted cameras in home kitchens, providing fine-grained egocentric interactions and natural audio cues.

## Reference Paper
- *Dima Damen et al.* "EPIC-KITCHENS-100: Challenges for Egocentric Action Recognition." IJCV, 2022. [`PDF`](https://arxiv.org/abs/2006.13256)

## Benchmarks & Baselines
- **TSN (RGB+Flow)** - Top-1 verb: 65.1, noun: 45.3, action: 38.9; *Damen et al., 2022.*
- **Temporal Alignment Networks (TAN)** - Action anticipation Top-5: 32.1; *Miech et al., ECCV 2020.*
- Official leaderboards available on [CodaLab](https://competitions.codalab.org/competitions/26924) for recognition, detection, and anticipation tasks.

## Tooling & Ecosystem
- [EPIC-Kitchens Toolkit](https://github.com/epic-kitchens/epic-kitchens-toolkit) with metadata parsers, evaluation scripts, and download helpers.
- [MMAction2](https://github.com/open-mmlab/mmaction2) includes configs for EPIC-Kitchens recognition and anticipation.
- [Narrations](https://github.com/epic-kitchens/annotations) provide time-aligned verb/noun labels and bounding boxes.

## Known Challenges
- Verb/noun imbalance is significant; weighted losses or focal losses are common.
- Audio quality varies; consider pre-processing for anticipation tasks.
- Storage requirements (~2.2 TB) and download quotas necessitate selective fetching via toolkit.

## Cite
```
@article{damen2022epickitchens100,
  title   = {EPIC-KITCHENS-100: Challenges for Egocentric Action Recognition},
  author  = {Damen, Dima and Doughty, Hazel and Farinella, Giovanni Maria and others},
  journal = {International Journal of Computer Vision},
  year    = {2022}
}
```
