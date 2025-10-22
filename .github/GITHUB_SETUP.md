# GitHub 仓库设置指南 | Repository Setup Guide

完成以下设置以最大化仓库的可发现性与学术影响力。

## 1️⃣ 仓库描述 | Repository Description

**在仓库首页点击 "About" 右侧的齿轮 ⚙️，添加：**

### 英文版 (English) - 推荐
```
Curated catalog of 40+ Human Activity Recognition (HAR) and action recognition datasets: vision, wearable sensors, skeleton/mocap, multimodal. Includes benchmarks, baselines, and citations.
```

### 中文版 (Chinese)
```
精选 40+ 个人体活动识别（HAR）与动作识别数据集：视觉、可穿戴传感器、骨架/动捕、多模态。含基准、基线与引用。
```

**建议使用英文版**（GitHub 搜索对英文关键词优化更好）

---

## 2️⃣ Topics 标签 | Repository Topics

**在 "About" 设置中添加以下 Topics（最多 20 个，建议 12-15 个）：**

### 核心标签（必选）
```
human-activity-recognition
action-recognition
har
datasets
benchmark
motion-capture
pose-estimation
```

### 技术标签（推荐）
```
computer-vision
deep-learning
machine-learning
skeleton-based
wearable-sensors
time-series
multimodal
```

### 社区标签（可选）
```
awesome
awesome-list
research
dataset-catalog
```

**完整复制（可直接粘贴到 Topics 输入框）：**
```
human-activity-recognition, action-recognition, har, datasets, benchmark, motion-capture, pose-estimation, computer-vision, deep-learning, machine-learning, skeleton-based, wearable-sensors, time-series, multimodal, awesome
```

---

## 3️⃣ 网站链接 | Website URL

**在 "About" 设置中添加（未来可替换为 GitHub Pages 文档站）：**
```
https://github.com/intelli-cave/human-activity-recognition-datasets
```

**未来规划：** 当 MkDocs 文档站上线后，替换为：
```
https://intelli-cave.github.io/human-activity-recognition-datasets
```

---

## 4️⃣ 社交预览图 | Social Preview Image

**路径：** Settings → General → Social preview → Upload an image

### 设计规范
- **尺寸：** 1280 × 640 px（推荐）
- **格式：** PNG 或 JPG
- **内容建议：**
  - 仓库标题："Human Activity Intelligence Atlas"
  - 副标题："40+ HAR & Action Recognition Datasets"
  - 关键词可视化：`Vision · Skeleton · Wearable · Multimodal`
  - 简洁图标（传感器、骨架、摄像头等）
  - 背景色：深色科技风或白底简洁风

### 在线工具
- [Canva](https://www.canva.com/) - 模板：GitHub Social
- [Figma](https://www.figma.com/) - 社区模板搜索 "GitHub OG image"
- [Pablo by Buffer](https://pablo.buffer.com/)

### 示例文案（置于预览图上）
```
🎯 Human Activity Intelligence Atlas
   40+ HAR & Action Recognition Datasets
   Vision · Skeleton · Wearable · Multimodal
   📊 Benchmarks | 📚 Citations | 🛠 Tooling
```

---

## 5️⃣ 发布 Release | Create Release

### 操作步骤
1. 前往 **Releases** → **Draft a new release**
2. **Tag version:** `v0.1.0`
3. **Release title:** `v0.1.0 - Initial Public Release`
4. **Description:** 复制 `.github/RELEASE_v0.1.0.md` 的内容
5. **Set as the latest release** ✅
6. 点击 **Publish release**

**效果：**
- 仓库右侧显示 "Latest release" 徽章
- GitHub 搜索会提升有 Release 的仓库排名
- 支持 Zenodo DOI 自动生成（需额外设置）

---

## 6️⃣ 启用功能 | Enable Features

### Settings → General → Features
- ✅ **Issues** - 允许社区请求新数据集
- ✅ **Discussions** - 开启社区讨论（推荐分类：Ideas, Q&A, Show and tell）
- ✅ **Projects** - 可选，用于路线图管理
- ✅ **Wiki** - 可选，未来可迁移文档

### Settings → Manage access
- 确保仓库为 **Public**

---

## 7️⃣ Zenodo DOI（学术引用）

### 操作步骤
1. 访问 [Zenodo GitHub 集成](https://zenodo.org/account/settings/github/)
2. 登录后授权 GitHub 访问
3. 找到 `intelli-cave/human-activity-recognition-datasets`，点击 **ON** 启用
4. 发布任意 Release（如 v0.1.0）后，Zenodo 自动生成 DOI
5. 复制 DOI 徽章代码添加到 README 顶部

**徽章示例：**
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

---

## 8️⃣ 提交到 Awesome 列表

### 推荐目标
- [awesome-action-recognition](https://github.com/jinwchoi/awesome-action-recognition)
- [awesome-human-pose-estimation](https://github.com/wangzheallen/awesome-human-pose-estimation)
- [awesome-activity-recognition](https://github.com/topics/activity-recognition)（GitHub Topics）

### PR 模板
```markdown
## Human Activity Recognition Datasets

Curated catalog of 40+ HAR and action recognition datasets across vision, wearable sensors, skeleton/mocap, and multimodal domains. Includes licensing, benchmarks, baselines, and citations.

- Repository: https://github.com/intelli-cave/human-activity-recognition-datasets
- Modalities: Vision, Skeleton, Wearable, Multimodal
- Features: Dataset cards, benchmark tables, automated link validation, multi-language support
```

---

## ✅ 设置完成检查清单

- [ ] 添加仓库描述（About）
- [ ] 添加 Topics 标签（12-15 个）
- [ ] 上传社交预览图（1280×640 px）
- [ ] 发布 v0.1.0 Release
- [ ] 启用 Issues & Discussions
- [ ] （可选）集成 Zenodo DOI
- [ ] （可选）提交到 Awesome 列表

---

**完成后效果：**
- 🔍 GitHub 搜索 "human activity recognition datasets" 可发现
- 🎓 学术搜索（Google Scholar）可通过 CITATION.cff 和 DOI 追踪引用
- 📈 社交分享（Twitter/Reddit）显示精美预览图
- ⭐ Stars 徽章与 Topics 吸引潜在贡献者

