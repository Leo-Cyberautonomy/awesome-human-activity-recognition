# OPPORTUNITY

- **Modality:** Wearable IMUs, body-worn accelerometers, ambient sensors, location beacons
- **Primary Tasks:** Context-aware activity recognition, sensor fusion, domain adaptation
- **Scale:** 4 participants, ~6 hours per subject, 72 sensor channels at 30-100 Hz
- **License:** Creative Commons Attribution-NonCommercial 4.0
- **Access:** [https://archive.ics.uci.edu/ml/datasets/OPPORTUNITY+Activity+Recognition](https://archive.ics.uci.edu/ml/datasets/OPPORTUNITY+Activity+Recognition)

## Summary
The OPPORTUNITY dataset captures rich multi-modal sensor streams during scripted and unscripted daily-living scenarios. Its dense annotation (gestures, locomotion, high-level activities) and multi-device fusion make it ideal for research on context recognition and missing-sensor robustness.

## Reference Paper
- *Daniel Roggen et al.* "Collecting Complex Activity Datasets in Highly Rich Networked Sensor Environments." INSS, 2010. [`PDF`](https://www.idiap.ch/paper/opportunity)

## Benchmarks & Baselines
- **Hierarchical Conditional Random Fields** - F1: 78.7 for locomotion; *Roggen et al., 2010.*
- **DeepConvLSTM** - F1: 86.0 (locomotion), 70.1 (gestures); *Ordonez & Roggen, IJCNN 2016.*
- Common protocol: preprocess into sliding windows (1s, 50% overlap) and report macro F1 for locomotion and gestures separately.

## Tooling & Ecosystem
- [Opportunity Processing Toolkit](https://github.com/mariusbock/dl-activity-recognition) includes normalization and LOSO splits.
- [TensorFlow HAR examples](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/).
- Feature extraction via [tsfresh](https://tsfresh.readthedocs.io/) and [Pandas](https://pandas.pydata.org/) for classical baselines.

## Known Challenges
- Sensors operate at different frequencies; alignment and interpolation are mandatory.
- High class imbalance (gestures vs. null activity) necessitates rebalancing strategies.
- Dataset includes missing segments; handle NaNs carefully or impute.

## Cite
```
@inproceedings{roggen2010opportunity,
  title     = {Collecting Complex Activity Datasets in Highly Rich Networked Sensor Environments},
  author    = {Roggen, Daniel and Calatroni, Alberto and Rossi, Mirco and others},
  booktitle = {International Conference on Networked Sensing Systems},
  year      = {2010}
}
```
