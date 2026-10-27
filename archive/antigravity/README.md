> 历史归档：本目录保留 2026-10-22/23 的交接记录。2026-10-27 起，新增工作统一写入主项目；下文隔离规则为历史记录，当前入口见[项目首页](../../README.md)。

# antigravity-Research Training 工作与交接说明

## 一、目录创建背景与隔离规则

本目录 `archive/antigravity/` 创建于 **2026-10-22**。

- **创建原因**：由于 Codex 平台使用额度暂时用尽，科研训练的后续学习、讨论、推导及代码扩展转移至 Antigravity 辅助进行。
- **严格隔离原则（Strict Isolation Policy）**：
  1. **禁止修改原项目文件**：Antigravity 在此工作空间期间，**绝不修改、删除或重命名**父目录 `Research Training/` 中的任何既有文件（包括但不限于 `docs/`、`references/`、`research-log/`、`simulation/`、`results/`、`zemax_learning_log.md`、`README.md` 以及 `.zmx`/`.ZDA` 文件等）。
  2. **所有输出仅限本目录**：Antigravity 产生的所有学习笔记、对话记录、辅助仿真代码、阶段性图表与交付总结，**一律仅写入** `archive/antigravity/` 内部。
  3. **便于 Codex 无缝接轨**：Codex 恢复额度并重新接管该项目时，可以直接通过本目录下的文档了解 Antigravity 期间的所有进展、讨论结论与代码成果，无需担心原版本库被污染或产生非预期的 git conflict。

---

## 二、子目录结构规范

```text
archive/antigravity/
├── README.md                  # 本说明文档（给 Codex 和用户参考）
├── learning-log/              # 在 Antigravity 中的日常学习与对话记录（按日期命名）
├── docs/                      # 理论推导、光路分析与交接计划
│   ├── theory/                # 理论补充与物理模型推导
│   └── handoff/               # 阶段性总结与面向 Codex 的交接文档
├── scripts/                   # 在 Antigravity 中新建的 Python 辅助脚本 / 仿真工具
└── results/                   # 对应 scripts 生成的图像、数据与指标 JSON
```

---

## 三、接续自 Codex 的项目基线状态（截至 2026-10-22）

为了让后续接手的 Codex 或其他助手能快速对齐上下文，以下整理自接手时的项目现状：

### 1. 项目基本信息
- **指导教师**：李建欣
- **研究主题**：动态干涉测量技术（Dynamic Interferometry）
- **核心方向**：同步偏振相移干涉成像、微偏振片阵列（MPA/PPM）、动态抗微振波前测量与解调算法、Zemax 光学建模与物理参数映射。

### 2. 既有已完成成果（位于原项目，只读引用）
- **理论体系** (`docs/theory/`)：
  - 课程 1~5：双光束干涉基础、相干度与可见度、四步相移法与包裹相位、二维相位展开与最小二乘法、Jones 矩阵与同步偏振相移原理。
- **文献阅读** (`references/`)：
  - Novak 2005 (微偏振片阵列)、Bai 2023 (单幅偏振相移综述)、Zhang 2023 (抗微振综述)、Xu 2009 (动态干涉技术框架)、Qian 2001 (实时偏振相移)、Millerd 2005 (像素化相位掩模动态干涉仪)。
- **Python 理想基线** (`simulation/python/`)：
  - `simulate_static_four_step.py`：静态标准四步相移算法与评价。
  - `simulate_ideal_jones_four_channel.py` / `simulate_jones_case_b.py`：偏振 Jones 四通道解调。
  - `simulate_dynamic_global.py`：正弦动态振动下顺序四步（存在显著动态相移误差，RMSE≈0.2637 rad）与理想同步偏振（瞬时冻结动态，误差接近浮点极限）对比。
- **Zemax 实践记录** (`research-log/zemax-learning-log.md`, `simulation/zemax/models/single_lens_F4.zmx`)：
  - 环境：Windows OpticStudio 2026 R1.00 Student。
  - 进度：单透镜光斑/像差/波前/OPD Fan 分析已完成；平面镜往返光路（`plane_mirror_round_trip.zmx`）已建立，完成带符号 Thickness、Coordinate Break 倾斜追迹与光程变化（$\lambda=632.8\text{ nm}$，倾斜 0.1° 返回偏移验证）。

### 3. 接续计划（依据 `docs/handoff/2026-10-22-zemax-progress-and-next-plan.md`）
后续教学与研究的主线任务是**将 Zemax 光学建模与 Python 相位程序打通**：
1. **阶段 1：完整简化泰曼–格林光路场景与模型边界**
   - 梳理光源、准直、分束、参考臂、测试臂、合束与成像系统。
   - 明确共同参考截面、光程差 $\Delta\mathrm{OPD}$ 正负号约定与物理量映射。
2. **阶段 2：轴向位移、波前与条纹的衔接**
   - 轴向微位移 $d$ 产生 $\Delta\mathrm{OPD} \approx 2d$，$\Delta\phi = \frac{4\pi d}{\lambda}$（统一使用 $\lambda = 632.8\text{ nm}$，$\lambda/2 \approx 316.4\text{ nm}$ 对应 $2\pi$ 相位变化）。
3. **阶段 3：已有正弦动态基线的参数化复核**。
4. **阶段 4~5：新增非理想动态因素——有限曝光时间积分效应分析**。

---

## 四、对 Codex / 后续使用的说明与交接建议

1. **如需合入原项目**：Codex 恢复额度后，若认为 `archive/antigravity/` 中的某些脚本、文档或学习日志应纳入主工程，可在用户确认的前提下手动将其复制或移动到 `docs/`、`simulation/` 或 `research-log/` 中。
2. **环境一致性**：在 Antigravity 中编写的 Python 脚本一律遵循原项目规范（NumPy、SciPy、Matplotlib，无额外重型依赖），保证原 Python 虚拟环境即可直接运行。
