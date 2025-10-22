# 人体活动识别数据集（Human Activity Recognition Datasets）

[**中文**](README.zh.md) | [English](../README.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md)

![datasets](https://img.shields.io/badge/datasets-40%2B-brightgreen) ![last-update](https://img.shields.io/badge/last_update-2024Q2-blue) ![awesome](https://img.shields.io/badge/list-awesome-critical)

一个覆盖视觉、可穿戴传感、骨架捕获、多模态等领域的人体活动与动作数据集的精选目录。每份数据集卡片都包含模态、许可协议、基准任务、代表性基线、工具生态以及权威论文，帮助你快速着手建模或对比评测。

- 针对机器学习研究者、产品团队以及运动科学实验室。
- 既展示最前沿的数据集，也保留构建现有基准的经典数据集。
- 配套贡献工作流、校验工具与发展路线图，便于社区协同维护。

> 目标：打造人体活动数据集的权威 GitHub 资源，参考 Papers with Code 的深度，同时保持“数据集优先”的视角。

## 快速入口
- 数据集卡片目录：[`datasets/`](../datasets/)
- 综述与基准论文：[`docs/surveys.md`](../docs/surveys.md)
- 基准快照：[`docs/benchmarking.md`](../docs/benchmarking.md)
- 贡献指南：[`CONTRIBUTING.md`](../CONTRIBUTING.md)
- 自动化路线图：[`docs/roadmap.md`](../docs/roadmap.md)

## 分类概览

| 数据集 | 模态 | 主要任务 | 规模 | 获取方式 |
| --- | --- | --- | --- | --- |
| [Kinetics-700](../datasets/vision/kinetics-700.md) | RGB 视频 | 动作识别 | 65 万视频片段 / 700 类别 | 公共 (CC BY) |
| [NTU RGB+D 120](../datasets/vision/ntu-rgbd-120.md) | RGB + 深度 + 骨架 | 3D 动作识别 | 11.4 万序列 / 120 类别 | 公共 (科研协议) |
| [Something-Something V2](../datasets/vision/something-something-v2.md) | RGB 视频 | 精细交互识别 | 22 万片段 / 174 标签 | 公共 (Apache 2.0) |
| [AMASS](../datasets/skeleton/amass.md) | 参数化人体姿态 | 动作生成、姿态估计 | 1.6 万分钟 / 344 名受试者 | 公共 (AMASS 许可) |
| [Human3.6M](../datasets/skeleton/human36m.md) | 动捕 + RGB | 姿态估计、3D 重建 | 360 万帧 3D 数据 | 科研许可 |
| [BABEL](../datasets/skeleton/babel.md) | SMPL + 文本标签 | 动作-语言对齐 | 43 小时 / 3.7k 序列 | 科研许可 (非商业) |
| [PAMAP2](../datasets/wearable/pamap2.md) | IMU + 心率 | 可穿戴 HAR | 3 人 / 18 种活动 | 公共 (CC BY-SA) |
| [WISDM](../datasets/wearable/wisdm.md) | 手机 + 手表传感器 | HAR、手势识别 | 51 人 / 百万级样本 | 公共 (知识共享协议) |
| [OPPORTUNITY](../datasets/wearable/opportunity.md) | 可穿戴 + 环境传感 | 场景识别 | 4 人 / 72 通道 | 公共 (科研许可) |
| [HAPT](../datasets/wearable/hapt.md) | 智能手机 IMU | 活动与姿态转换 | 30 人 / 12 种活动 | 公共 (CC BY) |
| [RealWorld HAR](../datasets/wearable/realworld-har.md) | 手机 + 手表 IMU | 真实场景 HAR | 60 人 / 15 种活动 | 公共 (CC BY) |
| [EPIC-Kitchens-100](../datasets/multimodal/epic-kitchens-100.md) | Ego RGB + 音频 | 长时 egocentric 行为 | 700 小时 / 90 厨房 | 公共 (科研许可) |
| [Ego4D](../datasets/multimodal/ego4d.md) | Ego RGB + 立体 + 音频 | 4D 行为、问答、视听任务 | 3300 小时 / 74 场景 | 公共 (非商业) |
| [Charades](../datasets/multimodal/charades.md) | 室内 RGB + 剧本 | 多标签动作 | 9800 视频 / 157 标签 | 公共 (CC BY-NC) |
| [BEHAVE](../datasets/emerging/behave.md) | RGB-D + 姿态 | 人-物交互建模 | 321 序列 / 20 人 | 公共 (BEHAVE 许可) |
| [Motion-X](../datasets/emerging/motion-x.md) | 多传感动捕 | 全身+手部骨架 | 10 人 / 200 万帧 | 公共 (科研许可) |
| [Ego-Exo4D](../datasets/emerging/ego-exo4d.md) | Ego + Exo RGB + 动捕 | 视角互译、Cross-view | 1400 序列 / 20 小时 Ego | 公共 (科研许可) |

详细信息请查阅对应数据集卡片，包括下载方法、引用信息、基线结果与已知挑战。

## 为什么要做这个仓库
- **问题优先导航：** 按任务或模态检索数据集，而不仅仅是字母排序。
- **结合研究语境：** 每个数据集卡片都链接到权威论文、基准与最新跟进工作。
- **可执行工具：** 提供数据格式转换提示、链接检查动作（路线图中）和计划中的下载脚本。
- **质量保障：** 贡献模板、评审清单与自动化校验让目录可靠可信。

## 仓库结构
```
.
 datasets/               # 按模态划分的数据集卡片
   vision/
   skeleton/
   wearable/
   multimodal/
   emerging/
 docs/                   # 综述、路线图、研究背景
 tools/                  # 脚本与工具（校验器、目录生成）
 .github/workflows/      # 自动化（链接检查、目录生成）
```

## 精选论文与综述
- Aggarwal & Ryoo，《Human Activity Analysis: A Review》，ACM Computing Surveys，2011。
- Lara & Labrador，《A Survey on Human Activity Recognition using Wearable Sensors》，IEEE Communications Surveys，2013。
- Li 等，《A Systematic Survey on Deep Learning for Human Activity Recognition》，ACM Computing Surveys，2022。
- Grauman 等，《Ego4D: Around the World in 2,250 Hours of Egocentric Video》，CVPR 2022。（数据集 + 基准）
- Pavlakos 等，《BABEL: Bodies, Actions and Behavior with English Labels》，CVPR 2022。

扩展阅读请见 [`docs/surveys.md`](../docs/surveys.md)。

## 如何使用本目录
1. **定位数据集：** 先查分类表，或按目录浏览。
2. **阅读数据集卡片：** 在下载前了解许可、任务、基准协议和数据特点。
3. **快速原型：** 利用“快速上手”提示，完成格式转换或接入 PyTorch / TensorFlow 数据加载器。
4. **持续跟进：** Watch 仓库或关注 Discussions，我们会在每次发布时总结新增数据集与 SOTA 动态。

### 引用
若本仓库对你的研究或产品有所帮助，请引用：

```bibtex
@misc{har_datasets_2025,
  title   = {Human Activity Recognition Datasets: A Curated Catalog},
  author  = {Wenxuan Huang},
  year    = {2025},
  url     = {https://github.com/intelli-cave/human-activity-recognition-datasets},
  note    = {GitHub repository}
}
```

## 贡献方式
- 阅读 [`CONTRIBUTING.md`](../CONTRIBUTING.md)，获取数据集卡片模板、评审标准与写作规范。
- 使用 Issue 请求新数据集或报告失效链接。我们按模态使用标签（如 `modality:wearable`）。
- Pull Request 将接受数据质量评审与自动化链接校验，力争 5-7 天内完成。

## 发展路线
- 每周自动链接校验与数据集徽章更新。
- 发布可穿戴与视频基线的 Jupyter 入门笔记。
- 社区焦点：每季度发布新数据集与排行榜动态摘要。
- 长期目标：基于 MkDocs 构建可搜索的静态站点。

## 致谢
感谢所有数据集作者、标注团队与基准维护者，正是他们推动了人体活动理解领域的开放研究。我们希望通过易用的目录放大他们的成果。
