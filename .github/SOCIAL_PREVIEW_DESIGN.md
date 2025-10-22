# 社交预览图设计指南 | Social Preview Image Design Guide

用于 GitHub 仓库设置中的 Social Preview（在 Twitter、LinkedIn、Slack 等平台分享时显示）。

---

## 📐 技术规格 | Technical Specs

- **尺寸：** 1280 × 640 px（2:1 比例）
- **格式：** PNG（推荐，支持透明）或 JPG
- **文件大小：** < 1 MB
- **安全区域：** 四周留 40px 边距（部分平台会裁剪）

---

## 🎨 设计方案 A：极简科技风

### 布局
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   🎯 Human Activity Intelligence Atlas             │
│                                                     │
│   40+ HAR & Action Recognition Datasets            │
│   ─────────────────────────────────────────         │
│   📊 Vision · Skeleton · Wearable · Multimodal     │
│                                                     │
│   ✓ Benchmarks  ✓ Citations  ✓ Tooling            │
│                                                     │
│                      github.com/wh1g19/human_activaty │
└─────────────────────────────────────────────────────┘
```

### 颜色方案
- **背景：** 深蓝渐变 (#0D1117 → #161B22，GitHub Dark 主题色)
- **标题：** 白色 (#FFFFFF，60pt 粗体)
- **副标题：** 亮蓝色 (#58A6FF，36pt)
- **关键词：** 灰白色 (#C9D1D9，28pt)
- **装饰线：** 蓝色渐变 (#1F6FEB)

### 字体
- **标题：** Inter Black / Montserrat Bold
- **正文：** Inter Regular / SF Pro

---

## 🎨 设计方案 B：数据可视化风格

### 布局
```
┌─────────────────────────────────────────────────────┐
│  📊 [简化骨架图标]                                  │
│                                                     │
│  Human Activity Intelligence Atlas                 │
│  ─────────────────────────────────────             │
│  40+ Datasets Across 5 Modalities                  │
│                                                     │
│  [进度条图示]                                       │
│  Vision ████████░░  80%                            │
│  Skeleton ██████░░░░  60%                          │
│  Wearable ████████░░  80%                          │
│  Multimodal ████░░░░░░  40%                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 颜色方案
- **背景：** 白色或浅灰 (#F6F8FA)
- **图标：** 多色渐变（蓝→紫→橙）
- **标题：** 深灰 (#24292F)
- **进度条：** 彩色分段（Vision=蓝, Skeleton=紫, Wearable=绿, Multimodal=橙）

---

## 🎨 设计方案 C：学术海报风格

### 布局
```
┌─────────────────────────────────────────────────────┐
│  Human Activity Intelligence Atlas                 │
│  ═══════════════════════════════════════           │
│                                                     │
│  A Curated Catalog of HAR Datasets                 │
│                                                     │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  │ Vision  │ │Skeleton │ │Wearable │ │ Multi-  │ │
│  │  🎥     │ │  🦴     │ │  ⌚     │ │ modal   │ │
│  │ 4 sets  │ │ 4 sets  │ │ 5 sets  │ │ 3 sets  │ │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ │
│                                                     │
│  📚 Benchmarks | 📖 Citations | 🛠 Open Source      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 颜色方案
- **背景：** 学术风白底 + 浅灰网格
- **标题：** 深蓝 (#1F3A93)
- **卡片：** 白色带阴影，边框彩色编码
- **图标：** Emoji 或简化矢量图标

---

## 🛠 在线设计工具

### 1. Canva（最简单，推荐新手）
- 访问：https://www.canva.com/
- 搜索模板："GitHub Social" 或 "GitHub Repository"
- 自定义尺寸：1280 × 640 px
- 免费素材库丰富

### 2. Figma（专业，可复用）
- 访问：https://www.figma.com/
- 社区模板：搜索 "GitHub OG image"
- 优势：矢量编辑、团队协作、导出高质量 PNG

### 3. Pablo by Buffer（快速生成）
- 访问：https://pablo.buffer.com/
- 预设社交媒体尺寸
- 快速添加文字叠加层

### 4. 终端方案（程序员专属）
使用 ImageMagick 批量生成：
```bash
convert -size 1280x640 xc:"#0D1117" \
  -font Inter-Bold -pointsize 60 -fill white \
  -annotate +100+200 "Human Activity Intelligence Atlas" \
  -font Inter-Regular -pointsize 36 -fill "#58A6FF" \
  -annotate +100+280 "40+ HAR & Action Recognition Datasets" \
  -font Inter-Regular -pointsize 28 -fill "#C9D1D9" \
  -annotate +100+340 "Vision · Skeleton · Wearable · Multimodal" \
  social-preview.png
```

---

## 📝 文案建议

### 标题（必选其一）
1. **Human Activity Intelligence Atlas** （当前官方名称）
2. **HAR Dataset Catalog** （简短直接）
3. **Activity Recognition Datasets** （关键词优先）

### 副标题
1. **40+ Datasets Across Vision, Skeleton, Wearable & Multimodal**
2. **Curated Catalog for ML Researchers & Engineers**
3. **From RGB Video to IMU Sensors: Complete HAR Collection**

### 关键词行（选 3-5 个）
- 📊 Vision · Skeleton · Wearable · Multimodal
- ✓ Benchmarks · Citations · Open Source
- 🎯 40+ Datasets · 5 Modalities · 8 Languages
- 📚 SOTA Baselines · Paper Links · Code Examples

### 底部标注
- `github.com/wh1g19/human_activaty`
- `⭐ Star on GitHub`
- `Licensed under MIT`

---

## ✅ 设计检查清单

- [ ] 尺寸正确：1280 × 640 px
- [ ] 文件格式：PNG 或 JPG
- [ ] 文件大小：< 1 MB
- [ ] 关键信息可读（在缩略图下仍清晰）
- [ ] 品牌一致性（与 README 徽章色调协调）
- [ ] 测试预览：在 Twitter Card Validator 或 LinkedIn Inspector 测试
- [ ] 无版权问题（使用免费字体与图标）

---

## 🔗 预览测试工具

上传到仓库后，使用以下工具测试效果：

1. **Twitter Card Validator**
   - https://cards-dev.twitter.com/validator
   - 输入：`https://github.com/wh1g19/human_activaty`

2. **LinkedIn Post Inspector**
   - https://www.linkedin.com/post-inspector/
   - 检查链接预览效果

3. **Facebook Sharing Debugger**
   - https://developers.facebook.com/tools/debug/
   - 查看 Open Graph 元数据

---

## 📤 上传步骤

1. 设计完成后导出为 PNG（推荐）或 JPG
2. 前往仓库 Settings → General → Social preview
3. 点击 "Upload an image"
4. 选择文件上传（拖拽或点击）
5. 保存后等待 5-10 分钟缓存刷新
6. 在社交平台分享仓库链接测试效果

---

## 💡 快速启动方案

**如果没有设计经验，使用此最小化方案：**

1. 访问 Canva → 创建自定义设计（1280×640）
2. 背景选择深蓝渐变（#0D1117 → #161B22）
3. 添加文字：
   - 标题："Human Activity Intelligence Atlas"（白色，60pt，粗体）
   - 副标题："40+ HAR & Action Recognition Datasets"（亮蓝，36pt）
   - 关键词："Vision · Skeleton · Wearable · Multimodal"（灰白，28pt）
4. 添加简单装饰元素（可选）：
   - 几何线条、圆点矩阵、渐变条纹
5. 导出为 PNG，上传到 GitHub

**预计耗时：** 10-15 分钟

---

**完成后，你的仓库在社交平台分享时将显示专业预览图，显著提升点击率！** 🚀

