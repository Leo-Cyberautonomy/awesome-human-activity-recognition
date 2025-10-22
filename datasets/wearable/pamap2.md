# PAMAP2

- **Modality:** Wearable IMU (accelerometer, gyroscope, magnetometer) + heart rate monitor
- **Primary Tasks:** Daily activity recognition, wearable HAR benchmarking, transfer learning
- **Scale:** 9 subjects (8 train + 1 optional test), 18 labeled activities, 3 IMUs per subject, 100 Hz sampling
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0)
- **Access:** [https://archive.ics.uci.edu/ml/datasets/pamap2+physical+activity+monitoring](https://archive.ics.uci.edu/ml/datasets/pamap2+physical+activity+monitoring)

## Summary
PAMAP2 captures high-frequency wearable signals for a range of lifestyle activities including household chores and fitness exercises. It remains a standard benchmark for lightweight models and transfer learning with limited subjects thanks to its synchronized multi-sensor setup.

## Reference Paper
- *Attila Reiss and Didier Stricker.* "Introducing a New Benchmarked Dataset for Activity Monitoring." ISWC, 2012. [`PDF`](https://ieeexplore.ieee.org/document/6383629)

## Benchmarks & Baselines
- **DeepConvLSTM** - Accuracy: 94.2% (leave-one-subject-out); *Ordonez & Roggen, IJCNN 2016.*
- **SelfHAR (self-supervised)** - F1: 86.1% (cross-subject); *Yuan et al., ICML 2022.*
- Evaluation typically uses leave-one-subject-out (LOSO) cross-validation; some studies downsample to 33 Hz for efficiency.

## Tooling & Ecosystem
- [UCI HAR Utilities](https://github.com/STRATIS-Group/har) for preprocessing and resampling.
- [tsai library](https://github.com/timeseriesAI/tsai) includes dataloaders and benchmark notebooks.
- [mhealthtools](https://github.com/mhealthgroup/mhealthtools) offers feature extraction pipelines for wearable datasets.

## Known Challenges
- Subjects perform free-form activities causing intra-class variability.
- Sensor noise increases during high-intensity exercises; filtering and normalization strongly impact performance.
- Imbalanced activity durations; consider class-weighted loss or data augmentation.

## Cite
```
@inproceedings{reiss2012pamap2,
  title     = {Introducing a New Benchmarked Dataset for Activity Monitoring},
  author    = {Reiss, Attila and Stricker, Didier},
  booktitle = {Proceedings of the 16th International Symposium on Wearable Computers},
  year      = {2012}
}
```
