# Awesome Human Activity Recognition

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/intelli-cave/awesome-human-activity-recognition?style=social)](https://github.com/intelli-cave/awesome-human-activity-recognition/stargazers)
[![Forks](https://img.shields.io/github/forks/intelli-cave/awesome-human-activity-recognition?style=social)](https://github.com/intelli-cave/awesome-human-activity-recognition/network/members)
[![License](https://img.shields.io/github/license/intelli-cave/awesome-human-activity-recognition)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/intelli-cave/awesome-human-activity-recognition)](https://github.com/intelli-cave/awesome-human-activity-recognition/commits)

> **人体活动识别（HAR）精选资源列表** | A curated list of Human Activity Recognition (HAR), action recognition, motion capture, and pose estimation datasets.

**[中文](i18n/README.zh.md)** | [English](README.md) | [Deutsch](i18n/README.de.md) | [Español](i18n/README.es.md) | [Français](i18n/README.fr.md) | [日本語](i18n/README.ja.md) | [한국어](i18n/README.ko.md) | [Português](i18n/README.pt.md) | [Русский](i18n/README.ru.md)

---

**40+ datasets** spanning **vision-based action recognition**, **wearable sensor HAR**, **skeleton/mocap**, and **multimodal egocentric** tasks. Each card includes licensing, benchmark baselines, SOTA leaderboards, download instructions, and canonical paper citations—designed for ML researchers, product teams, and motion science labs.

**Keywords:** Human Activity Recognition · HAR · Action Recognition · Motion Capture · Pose Estimation · Skeleton-based · Wearable Sensors · IMU · Computer Vision · Time-Series · Multimodal · Benchmark Datasets · Deep Learning

- Built for ML researchers, product teams, and motion science labs.
- Highlights state-of-the-art (SOTA) datasets and the foundational classics they build upon.
- Ships with contribution workflows, validation tooling, and roadmap for community stewardship.

> *Goal: become the go-to GitHub resource for human activity datasets, mirroring the depth of Papers with Code while staying dataset-first.*

## Quick Links
- Dataset cards: [`datasets/`](datasets/)
- Survey and benchmark papers: [`docs/surveys.md`](docs/surveys.md)
- Benchmark snapshot: [`docs/benchmarking.md`](docs/benchmarking.md)
- Contribution guidelines: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Automation roadmap: [`docs/roadmap.md`](docs/roadmap.md)
- Translations: [`i18n/`](i18n/)

## Taxonomy Snapshot

| Dataset | Modality | Primary Tasks | Scale | Access |
| --- | --- | --- | --- | --- |
| [Kinetics-700](datasets/vision/kinetics-700.md) | RGB video | Action recognition | 650k clips / 700 classes | Public (CC BY) |
| [NTU RGB+D 120](datasets/vision/ntu-rgbd-120.md) | RGB + depth + skeleton | 3D action recognition | 114k seq / 120 classes | Public (research-only) |
| [Something-Something V2](datasets/vision/something-something-v2.md) | RGB video | Fine-grained interactions | 220k clips / 174 labels | Public (Apache 2.0) |
| [AMASS](datasets/skeleton/amass.md) | Parametric body poses | Motion synthesis, estimation | 16k mins / 344 subjects | Public (AMASS license) |
| [Human3.6M](datasets/skeleton/human36m.md) | Mocap + RGB | Pose estimation, 3D reconstruction | 3.6M 3D frames | Research license |
| [BABEL](datasets/skeleton/babel.md) | SMPL + text labels | Motion-language alignment | 43 hrs / 3.7k seq | Research (non-commercial) |
| [PAMAP2](datasets/wearable/pamap2.md) | IMU + HR | Wearable HAR | 3 users / 18 activities | Public (CC BY-SA) |
| [WISDM](datasets/wearable/wisdm.md) | Smartphone + smartwatch | HAR, gesture recognition | 51 subjects / 1M+ samples | Public (Creative Commons) |
| [OPPORTUNITY](datasets/wearable/opportunity.md) | Wearable + ambient sensors | Context recognition | 4 subjects / 72 sensors | Public (research-only) |
| [HAPT](datasets/wearable/hapt.md) | Smartphone IMU | Activity + transitions | 30 subjects / 12 activities | Public (CC BY) |
| [RealWorld HAR](datasets/wearable/realworld-har.md) | Phone + watch IMU | In-the-wild HAR | 60 subjects / 15 activities | Public (CC BY) |
| [EPIC-Kitchens-100](datasets/multimodal/epic-kitchens-100.md) | Ego RGB + audio | Long-term egocentric actions | 700 hrs / 90 kitchens | Public (research license) |
| [Ego4D](datasets/multimodal/ego4d.md) | Ego RGB + stereo + audio | 4D actions, SQA, AV tasks | 3.3k hrs / 74 scenes | Public (non-commercial) |
| [Charades](datasets/multimodal/charades.md) | Indoor RGB + scripts | Multi-label actions | 9.8k videos / 157 labels | Public (CC BY-NC) |
| [BEHAVE](datasets/emerging/behave.md) | RGB-D + pose | Human-object interaction | 321 seq / 20 subjects | Public (BEHAVE license) |
| [Motion-X](datasets/emerging/motion-x.md) | Multisensor mocap | Full-body & hand joints | 10 subjects / 2M frames | Public (research) |
| [Ego-Exo4D](datasets/emerging/ego-exo4d.md) | Ego+exo RGB + mocap | Cross-view actions | 1.4k seq / 20 hrs ego | Public (research) |

Explore every dataset card for download instructions, citation info, baseline scores, and known challenges.

## Why This Repo
- **Problem-first navigation:** start from the task or modality you care about, not just alphabetical lists.
- **Research context included:** every dataset card links the canonical paper, key benchmarks, and follow-up SOTA work.
- **Actionable tooling:** common data-format conversion notes, link-checking action (roadmap), and planned download helpers.
- **Quality gate:** contribution templates, review checklist, and automated validation keep the catalog trustworthy.

## Repository Structure
```
.
 datasets/               # Dataset cards grouped by modality
   vision/
   skeleton/
   wearable/
   multimodal/
   emerging/
 docs/                   # Surveys, roadmap, research framing
 tools/                  # Scripts and utilities (validators, catalog builders)
 .github/workflows/      # Automation (link checking, catalog regeneration)
```

## Featured Papers & Surveys
- Aggarwal & Ryoo. **Human Activity Analysis: A Review.** ACM Computing Surveys, 2011.
- Lara & Labrador. **A Survey on Human Activity Recognition using Wearable Sensors.** IEEE Communications Surveys, 2013.
- Li et al. **A Systematic Survey on Deep Learning for Human Activity Recognition.** ACM Computing Surveys, 2022.
- Grauman et al. **Ego4D: Around the World in 2,250 Hours of Egocentric Video.** CVPR, 2022. *(Dataset + benchmarks)*
- Pavlakos et al. **BABEL: Bodies, Actions and Behavior with English Labels.** CVPR, 2022.

Extended reading list lives in [`docs/surveys.md`](docs/surveys.md).

## How to Use This Catalog
1. **Find a dataset:** Start with the taxonomy table or browse directories.
2. **Read the dataset card:** Understand licensing, tasks, baseline protocols, and data quirks before downloading.
3. **Prototype faster:** Use the "Getting started" tips to convert formats or plug into PyTorch/TF dataloaders.
4. **Stay current:** Watch the repo or subscribe to Discussions; each release summarizes new datasets and SOTA shifts.

### Citation
If this repository helps your research or product, please cite it:

```bibtex
@misc{awesome_har_2025,
  title   = {Awesome Human Activity Recognition: A Curated List},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/intelli-cave/awesome-human-activity-recognition},
  note    = {GitHub repository}
}
```

## Contributing
- Check [`CONTRIBUTING.md`](CONTRIBUTING.md) for dataset card templates, review requirements, and style guide.
- Use issues to request new datasets or report stale links. We track modalities with labels (e.g., `modality:wearable`).
- Pull requests undergo dataset quality review + automated link validation. Expect review within 5-7 days.

## Roadmap Highlights
- Weekly automated link validation and dataset badge regeneration.
- Jupyter starter notebooks for wearable and video baselines.
- Community spotlight: quarterly digest of new datasets and leaderboards.
- Long-term: convert catalog into searchable static site via MkDocs.

## Acknowledgements
Thanks to dataset authors, annotation teams, and benchmark maintainers who make open research in human activity understanding possible. This project aims to amplify their work by making discovery effortless.
