# 2026-10-22 Zemax 学习迁移与交接备忘（面向 Codex 与新对话）

## 1. 迁移与隔离说明

- **当前状态**：因 Codex 额度用尽，Zemax 相关的后续科研训练转移至 Antigravity 进行。
- **文件隔离红线**：
  - Antigravity 内的所有新增文件、代码和学习日志**只存放在 `archive/antigravity/`**。
  - 原工程 `Research Training/` 下的所有既有文件（`zemax_learning_log.md`、`docs/`、`simulation/` 等）**保持原样、只读、不修改**。
- **记录追踪标准**：
  - 在 `archive/antigravity/learning-log/zemax_learning_log.md` 中延续原项目的高标准记录规范（问题导向、证据核对、参数追踪、用户理解与独立操作、物理纠偏、未决项）。
  - 后续切换回 Codex 时，Codex 只需要阅读 `archive/antigravity/` 即可全面了解期间发生的所有操作和推导，保障科研训练的连贯性。

## 2. 新对话启动指南（开新对话时直接使用）

用户在新开的 Zemax 专项对话中，只需输入以下内容作为首条指令即可无缝衔接：

```text
我们继续进行 Zemax 动态干涉学习任务。
请严格遵守以下规则：
1. 绝对不要修改原 Research Training 项目中的任何已有文件。
2. 所有学习记录、分析文档、代码脚本必须严格限制在 archive/antigravity/ 文件夹中。
3. 学习记录需实时追加到 archive/antigravity/learning-log/zemax_learning_log.md 中，保持严谨的参数、截图核对与物理意义记录，以便后续 Codex 接回。
4. 请先读取 archive/antigravity/README.md 和 docs/handoff/2026-10-22-zemax-progress-and-next-plan.md，然后开始第 1 次课内容：简化泰曼–格林光路场景与模型边界。
```

---

## 3. 即将开始的第 1 次课内容准备

- **课题**：完整光学场景与模型边界（现有平面镜属于干涉仪哪一段？参考光如何与它比较？）
- **任务目标**：
  1. 梳理一张标准简化泰曼–格林光路图；
  2. 明确参考臂与测试臂参数、共同截面与光程差 $\Delta\mathrm{OPD}$ 符号约定；
  3. 确定在 Zemax Student 顺序模式下如何为后续 Python 相位程序提供准确的光路输入。
