# 2026-10-23 面向 Codex 的规划审视与交接简报（Codex Review Briefing）

> **致 Codex**：
> 本简报梳理了在 Antigravity 辅助期间完成的关键环境升级、理论与光路衔接推导，以及面向 **OpticStudio 2024 Premium 旗舰版** 所制定的**三阶段动态干涉研究路线**。
> 整个过程严格执行“**零污染原工程原则**”——原工程 `Research Training/` 下的所有既有文件保持绝对只读未受任何改动，所有新增产出严格封闭在 `archive/antigravity/` 内部。请审视以下规划并给出你的评审意见。

---

## 一、本次会话完成的核心进展与里程碑

1. **工业级工具环境成功升级（重大里程碑）**：
   - 用户已在 Windows 环境成功部署并激活 **`Ansys Zemax OpticStudio® 2024 R1.00 Premium (64-位)`**（编译日期：2023-12-05，账户：A20120530，授权有效期至 2035-12-31）。
   - 之前受限于 2026 Student 版而缺失的 **非顺序模式（NSC 3D 实体光路）**、**相干探测器（Coherent Detector）**、**偏振追迹** 与 **ZOS-API** 已全量解锁。
2. **泰曼–格林光路边界与物理映射梳理完毕**：
   - 明确了 Windows 原模型 `plane_mirror_round_trip.zmx` 在干涉仪中的确切物理定位（双程测试臂往返）；
   - 梳理了参考臂与测试臂的光程关系：$\Delta\mathrm{OPD} = 2d \iff \Delta\phi = \frac{4\pi}{\lambda} d$（$\lambda = 632.8\,\mathrm{nm}$，$\lambda/4 \approx 158.2\,\mathrm{nm}$ 亮暗反转，$\lambda/2 \approx 316.4\,\mathrm{nm}$ 条纹平移一整周期）；
   - 明确了镜面倾斜 $0.1^\circ \implies$ 返回光偏转 $0.2^\circ \implies$ 空间载频条纹 $f_x = \sin(0.2^\circ)/\lambda$。
3. **澄清了 Zemax 与 Python 的科学分工边界**：
   - 澄清了无论学生版还是旗舰版，Zemax 均为“正向光机追迹软件”，缺乏四步相移解调、二维解包裹和动态时序误差分析工具链；
   - 确立了以“Zemax 负责真实 3D 光机与像差 $\leftrightarrow$ Python 负责波动探测与逆向解相”的标准科研范式。

---

## 二、提交 Codex 审视的【三阶段递进式研究路线】

详细技术文档见：[`archive/antigravity/docs/handoff/2026-10-23-zemax-premium-research-roadmap.md`](2026-10-23-zemax-premium-research-roadmap.md)

### 阶段一：3D 实体标量干涉基线（NSC 物理分束与相干条纹）
- **目标**：在统一 3D 空间中搭建实体双臂泰曼–格林干涉仪。
- **配置**：准直激光源（$632.8\,\mathrm{nm}$，束宽 $10\,\mathrm{mm}$）+ 50:50 分束立方体（NPBS）+ 参考镜 M1（$102\,\mathrm{mm}$）+ 待测镜 M2（$102\,\mathrm{mm}$）+ 相干探测器（`Detector Surface`, Coherent 模式）。
- **物理验证**：
  - 开启 Ray Splitting 后的真实空间能量物理分束；
  - 倾斜 $0.1^\circ$ 时相干探测器渲染出的平行直条纹间距验算（$p \approx 181.3\,\mu\mathrm{m}$）；
  - 轴向微移 $158.2\,\mathrm{nm}$ 亮暗互换与 $316.4\,\mathrm{nm}$ 整周期滑移。

### 阶段二：实体偏振动态干涉全光路（实体对齐课题核心 SPSI 仪器模型）
- **目标**：对齐 Millerd 2005 / Novak 2005 与李建欣老师课题组核心光路，建立偏振态空间演化模型。
- **配置**：将分束立方体升级为 PBS（偏振分束器），两臂各加一块 $45^\circ$ 四分之一波片（QWP），合束出射正交圆偏振光。
- **突破点**：探测器前配置 $2\times 2$ 微偏振片阵列（MPA/PPM，四通道检偏角度：$0^\circ, 45^\circ, 90^\circ, 135^\circ$），实现单次曝光同时采集 4 个相移干涉通道。

### 阶段三：ZOS-API 闭环与动态微振动/曝光积分评估（论文级核心创新）
- **目标**：利用 Premium 版 ZOS-API 接口，由 Python 脚本驱动 Zemax 进行时序动态微振动仿真。
- **实验设计**：
  - 注入连续正弦微振动 $d(t) = H\sin(2\pi ft)$（$f \in [10, 500]\,\mathrm{Hz}, H \in [10, 200]\,\mathrm{nm}$）；
  - 引入探测器有限曝光时间 $T$（$1\sim 10\,\mathrm{ms}$）的时间连续数值积分；
  - 量化对比传统顺序法（相位跳变崩溃，RMSE 激增）与同步偏振法（瞬时冻结波前），输出纳米级形貌复原 RMSE 演化曲线，沉淀高质量期刊论文数据与图表。

---

## 三、请 Codex 重点审视与确认的事项

1. **阶段衔接合理性**：从“阶段一（标量 3D NSC 验证）”到“阶段二（偏振 SPSI 建模）”再到“阶段三（API 动态微振动闭环）”的技术递进梯度是否稳健？
2. **光路参数物理量**：工作波长统一为 $\lambda = 632.8\,\mathrm{nm}$、参考/测试双程间距取 $102\,\mathrm{mm}$、倾斜角 $0.1^\circ$（偏转 $0.2^\circ$）等参数设定是否与原课题仿真完全契合？
3. **下一步执行建议**：Codex 审视通过后，是直接从阶段一的 NSC 新建文件开始操作，还是有需优先补充或微调的物理前置条件？

---

## 四、交接文件索引

- **本次简报**：`archive/antigravity/docs/handoff/2026-10-23-codex-review-briefing.md`
- **详细规划路线**：`archive/antigravity/docs/handoff/2026-10-23-zemax-premium-research-roadmap.md`
- **全量学习日志**：`archive/antigravity/learning-log/zemax_learning_log.md`
- **隔离说明文档**：`archive/antigravity/README.md`
