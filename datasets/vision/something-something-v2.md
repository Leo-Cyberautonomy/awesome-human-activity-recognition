# Something-Something V2

- **Modality:** RGB video (crowdsourced, 2-6 seconds)
- **Primary Tasks:** Fine-grained action recognition, temporal reasoning, few-shot transfer
- **Scale:** 220,847 video clips, 174 action templates, 338,000 textual descriptions
- **License:** Apache License 2.0
- **Access:** [https://developer.qualcomm.com/software/ai-datasets/something-something](https://developer.qualcomm.com/software/ai-datasets/something-something)

## Summary
Something-Something V2 focuses on human-object interactions captured with short, templated instructions. Its fine-grained verb-noun combinations drive research in temporal reasoning, compositional action recognition, and grounding natural language descriptions to video.

## Reference Paper
- *R. Goyal et al.* "The 'Something Something' Video Database for Learning and Evaluating Visual Common Sense." ICCV, 2017. [`PDF`](https://arxiv.org/abs/1706.04261)

## Benchmarks & Baselines
- **Temporal Shift Module (TSM)** - Top-1: 63.4, Top-5: 89.5; *Lin et al., ICCV 2019.*
- **ViViT-L/16x2** - Top-1: 68.8, Top-5: 90.6; *Arnab et al., ICCV 2021.*
- Standard split includes train, validation, and test; test labels withheld for leaderboard submission via EvalAI.

## Tooling & Ecosystem
- [EvalAI leaderboard](https://eval.ai/web/challenges/challenge-page/591/leaderboard/1683) for official metrics.
- [PyTorchVideo](https://pytorchvideo.org/) and [MMAction2](https://github.com/open-mmlab/mmaction2) supply dataloaders.
- [something-something-downloader](https://github.com/20bn/something-something-downloader) CLI to fetch videos and metadata.

## Known Challenges
- Video downloads occasionally fail due to host availability; rerun downloader scripts.
- Labels are heavily templated-consider text augmentation to avoid overfitting to phrasing.
- Clips are low-resolution (240p); models benefit from temporal cues rather than spatial detail.

## Cite
```
@inproceedings{goyal2017something,
  title     = {The `Something Something' Video Database for Learning and Evaluating Visual Common Sense},
  author    = {Goyal, Raghav and Kahou, Samira Ebrahimi and Michalski, Vincent and others},
  booktitle = {Proceedings of the IEEE International Conference on Computer Vision},
  year      = {2017}
}
```
