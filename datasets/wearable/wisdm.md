# WISDM (Wireless Sensor Data Mining)

- **Modality:** Smartphone accelerometer + gyroscope, smartwatch accelerometer
- **Primary Tasks:** Human activity recognition, gesture recognition, sensor fusion
- **Scale:** 51 subjects, 18 activities, 20 Hz sampling (v1); 75 subjects and 7 activities in WISDM v2
- **License:** Creative Commons Attribution-NonCommercial-ShareAlike 3.0
- **Access:** [https://www.cis.fordham.edu/wisdm/dataset.php](https://www.cis.fordham.edu/wisdm/dataset.php)

## Summary
WISDM provides in-the-wild data captured from Android smartphones and smartwatches carried or worn by participants. It is widely used for accelerometer-based HAR baselines, lightweight models, and semi-supervised learning thanks to its accessible format (CSV) and straightforward activity labels.

## Reference Paper
- *Jennifer R. Kwapisz, Gary M. Weiss, Samuel A. Moore.* "Activity Recognition using Cell Phone Accelerometers." SIGKDD Explorations, 2011. [`PDF`](https://www.cis.fordham.edu/wisdm/includes/files/sigkddexp.pdf)

## Benchmarks & Baselines
- **Random Forest (feature-engineered)** - Accuracy: 91.7%; *Kwapisz et al., 2011.*
- **1D CNN (DeepConvLSTM variant)** - Accuracy: 95.8% (10-fold CV); widely cited reimplementations.
- Evaluation splits vary; ensure reproducibility by publishing subject IDs and random seeds.

## Tooling & Ecosystem
- [WISDM preprocessing scripts](https://github.com/mrcslws/wisdm-dataset) for windowing and labeling.
- [TorchHAR](https://github.com/kforest/torch-har) includes loaders and baseline models.
- [Scikit-multiflow](https://scikit-multiflow.github.io/) supports incremental learning experiments with WISDM streams.

## Known Challenges
- Sampling frequency varies slightly between devices; resample windows before training.
- Labels rely on participant compliance (self-report); expect occasional label noise.
- Older versions lack gyroscope data; cross-version comparisons must document sensor availability.

## Cite
```
@article{kwapisz2011wisdm,
  title   = {Activity Recognition Using Cell Phone Accelerometers},
  author  = {Kwapisz, Jennifer R and Weiss, Gary M and Moore, Samuel A},
  journal = {SIGKDD Explorations},
  year    = {2011}
}
```
