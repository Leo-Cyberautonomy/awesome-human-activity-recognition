# HAPT (Human Activities and Postural Transitions)

- **Modality:** Smartphone accelerometer + gyroscope
- **Primary Tasks:** Activity recognition, postural transition detection, transfer learning
- **Scale:** 30 participants, 12 activities, 6 postural transitions, 50 Hz sampling
- **License:** Creative Commons Attribution 4.0
- **Access:** [https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones)

## Summary
HAPT augments the classic UCI HAR dataset with additional postural transitions captured using smartphone sensors fixed to the waist. It enables models that discriminate subtle transitions (e.g., sitting to standing) and remains a staple for benchmarking lightweight sequence models.

## Reference Paper
- *Davide Anguita et al.* "A Public Domain Dataset for Human Activity Recognition Using Smartphones." ESANN, 2013. [`PDF`](https://www.esann.org/sites/default/files/proceedings/legacy/es2013-84.pdf)

## Benchmarks & Baselines
- **SVM with hand-crafted features** - Accuracy: 96.3%; *Anguita et al., 2013.*
- **DeepConvLSTM** - Accuracy: 94.6% (10-fold CV); widely reproduced baseline.
- Evaluation typically reports subject-wise stratified 70/30 splits; ensure transitions are not leaked between sets.

## Tooling & Ecosystem
- [HAR smartphone preprocessing](https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition) includes scripts and models.
- [TensorFlow Lite HAR example](https://github.com/tensorflow/examples/tree/master/lite/examples/activity_recognition) uses HAPT for on-device inference.
- [Skorch HAR templates](https://github.com/Alex-Lekov/Smartphone-Activity-Recognition) for PyTorch-based training.

## Known Challenges
- Device placement is fixed (waist), limiting generalization to free-placement scenarios.
- Postural transitions are shorter than activities; windowing strategy affects performance.
- Sensor noise requires filtering (Butterworth) prior to feature extraction for classical pipelines.

## Cite
```
@inproceedings{anguita2013hapt,
  title     = {A Public Domain Dataset for Human Activity Recognition Using Smartphones},
  author    = {Anguita, Davide and Ghio, Alessandro and Oneto, Luca and others},
  booktitle = {Proceedings of the 21th International European Symposium on Artificial Neural Networks},
  year      = {2013}
}
```
