# Release v0.1.0 - Initial Public Release

## 🎉 首次公开发布 | Initial Public Release

Human Activity Intelligence Atlas 的首个稳定版本，汇集了 40+ 个跨模态的人体活动识别与动作识别数据集。

### ✨ 核心内容 | Highlights

**📊 Dataset Coverage (40+ datasets across 5 modalities)**
- **Vision-based**: Kinetics-700, NTU RGB+D 120, Something-Something V2, FineGym
- **Skeleton/Mocap**: AMASS, Human3.6M, BABEL, TotalCapture
- **Wearable Sensors**: PAMAP2, WISDM, OPPORTUNITY, HAPT, RealWorld HAR
- **Multimodal**: EPIC-Kitchens-100, Ego4D, Charades
- **Emerging**: BEHAVE, Motion-X, Ego-Exo4D

**📚 Documentation & Structure**
- ✅ Standardized dataset cards with licensing, baselines, citations, and download links
- ✅ Survey collection ([docs/surveys.md](docs/surveys.md)) covering foundational HAR research
- ✅ Benchmark snapshot ([docs/benchmarking.md](docs/benchmarking.md))
- ✅ Contribution guidelines with templates ([CONTRIBUTING.md](CONTRIBUTING.md))

**🛠 Tooling & Automation**
- ✅ Link validation GitHub Action (weekly scheduled + PR checks)
- ✅ Catalog builder script ([tools/catalog_builder.py](tools/catalog_builder.py))
- ✅ ASCII normalization utility ([tools/normalize_ascii.py](tools/normalize_ascii.py))

**🌍 Internationalization**
- ✅ Translations in 8 languages: 中文, Deutsch, Español, Français, 日本語, 한국어, Português, Русский

**🎓 Academic Discoverability**
- ✅ CITATION.cff file (GitHub "Cite this repository" button enabled)
- ✅ BibTeX citation format in README

### 🚀 Getting Started

1. **Browse datasets by modality:**
   ```
   datasets/
   ├── vision/          # RGB/depth video action recognition
   ├── skeleton/        # Mocap, pose estimation
   ├── wearable/        # IMU, smartwatch HAR
   ├── multimodal/      # Egocentric, audio-visual
   └── emerging/        # Latest research datasets
   ```

2. **Search by task:**
   - Action recognition → `vision/`, `multimodal/`
   - Human activity recognition (HAR) → `wearable/`
   - Pose estimation → `skeleton/`
   - Human-object interaction → `emerging/behave.md`

3. **Check licensing before download** — every card specifies access terms

### 📈 What's Next (Q3-Q4 2024)

- 📓 Jupyter starter notebooks for wearable & video baselines
- 🔄 Automated badge generation (dataset counts, modality breakdown)
- 🌐 MkDocs documentation site (GitHub Pages)
- 🏆 Community benchmarking challenges

See full roadmap: [docs/roadmap.md](docs/roadmap.md)

### 🙏 Acknowledgements

Thanks to all dataset authors, annotation teams, and the research community. This catalog aims to amplify their work by making discovery effortless.

---

**Star ⭐ this repo** if it saves you time | **Watch 👀** for updates | **Contribute 🤝** via [CONTRIBUTING.md](CONTRIBUTING.md)

