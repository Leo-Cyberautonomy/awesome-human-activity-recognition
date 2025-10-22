# RealWorld HAR

- **Modality:** Smartphone and smartwatch accelerometer + gyroscope
- **Primary Tasks:** Human activity recognition in-the-wild, domain adaptation, sensor placement robustness
- **Scale:** 15 activities, 60 subjects, 3 body locations (hand, chest, ankle), 50 Hz sampling
- **License:** Creative Commons Attribution 4.0
- **Access:** [https://sensor.informatik.uni-mannheim.de/#dataset_realworld](https://sensor.informatik.uni-mannheim.de/#dataset_realworld)

## Summary
RealWorld HAR captures daily activities both indoors and outdoors with participants wearing smartphones and smartwatches at multiple body locations. Its realistic variability (different devices, environments, and placements) provides a challenging benchmark for domain adaptation and robust wearable HAR.

## Reference Paper
- *Henrik Sztyler and Heiner Stuckenschmidt.* "On-body Localization of Wearable Devices: An Investigation of Position-aware Activity Recognition." PERCOM, 2016. [`PDF`](https://ieeexplore.ieee.org/document/7456521)

## Benchmarks & Baselines
- **Position-aware Activity Recognition** - Accuracy: 86.7%; *Sztyler & Stuckenschmidt, 2016.*
- **DeepConvLSTM + Domain Adversarial Training** - F1: 79.3%; applied in follow-up work on cross-location adaptation.
- Evaluation protocols often use leave-one-location-out and leave-one-subject-out to measure robustness.

## Tooling & Ecosystem
- [realworld-har-toolkit](https://github.com/sztyler/realworld-har-toolkit) for downloading, preprocessing, and data alignment.
- [Domain adaptation benchmarks](https://github.com/wmcnicho/activity-domain-adaptation) include experiments using RealWorld HAR.
- Works with [scikit-multiflow](https://scikit-multiflow.github.io/) for streaming evaluation.

## Known Challenges
- Missing data segments occur during outdoor sessions; imputation or window filtering needed.
- Sensor orientation varies; apply orientation normalization or quaternion representations.
- Combining smartphone and smartwatch data requires careful synchronization.

## Cite
```
@inproceedings{sztyler2016realworld,
  title     = {On-body Localization of Wearable Devices: An Investigation of Position-aware Activity Recognition},
  author    = {Sztyler, Henrik and Stuckenschmidt, Heiner},
  booktitle = {IEEE International Conference on Pervasive Computing and Communications},
  year      = {2016}
}
```
