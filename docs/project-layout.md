# 项目文件导航与整理记录

更新：2026-10-27。整理目录与引用，保留既有学习记录、数据和仿真算法。

## 常用入口

| 要找什么 | 位置 |
|---|---|
| 当前学习安排 | [复习与实践计划](handoff/2026-10-27-review-and-practice-plan.md) |
| 理论复习 | [知识地图](review/00-foundation-knowledge-map.md)、[理论笔记](theory/) |
| 文献带读 | [文献首页](../references/README.md)、[正式带读](../references/guided-reading/) |
| 历史学习记录 | [按日期日志](../research-log/)、[Zemax 学习日志](../research-log/zemax-learning-log.md) |
| Python 程序、依赖与运行方式 | [Python 首页](../simulation/python/README.md) |
| Zemax 原生模型 | [模型说明](../simulation/zemax/README.md) |
| Zemax 截图 | [按日期截图](../results/zemax/) |
| 四帧强度、相位图和计算结果 | [本次分析](../simulation/python/results/zemax_four_step_2026-10-26/README.md) |
| 导出 PDF 与教学插图 | [导出资料](../output/README.md) |
| Antigravity 阶段交接与旧计划 | [历史归档](../archive/antigravity/README.md) |

## 文件约定

- `docs/theory/`：原理与推导；`docs/review/`：复习、技术对照和阶段总结；`docs/handoff/`：当前安排和带日期的历史交接。
- `research-log/`：学习经过和操作记录，保留日期、证据和未决问题。
- `references/guided-reading/` 与 `references/ai-preread/` 分别保存正式带读与 AI 预读，不混记完成状态。
- `simulation/python/scripts/` 是运行入口，`src/` 是复用算法，`results/<工况>/` 保留原始输入、图和指标。
- `simulation/zemax/models/` 放 `.zmx` 等原生工程；Zemax 分析截图继续保存在 `results/zemax/<日期>/`。
- `output/` 保存供阅读的导出件。它与 `simulation/python/results/` 中的数值结果用途不同。
- `archive/` 保留旧阶段资料；当前执行安排从项目 README 进入。
- `tmp/`、`_docx_review/`、Python 缓存和本地环境不参加版本管理；VS Code 隐藏这些临时项目。

## 本次移动对照

| 原位置 | 当前位置 |
|---|---|
| `antigravity-Research Training/` | `archive/antigravity/` |
| 根目录 `single_lens_F4.zmx` | `simulation/zemax/models/single_lens_F4.zmx` |
| 根目录 `single_lens_F4.ZDA` | `simulation/zemax/models/single_lens_F4.ZDA`，本地保留并忽略 |
| 根目录 `zemax_learning_log.md` | `research-log/zemax-learning-log.md` |

此前已把本轮新增分析脚本、结果和学习计划分别移至主项目的 `simulation/python/` 与 `docs/handoff/`。原有仿真程序及结果目录保持现有运行路径；本次仅调整分析脚本的默认输入，使其使用仓库内保存的四帧数据。

没有删除论文、原始数据、模型或历史笔记，没有改写 Git 历史或自动提交。原文件移动时先校验内容，再更新文档中的路径。现有归档中的过时技术说法以其后技术评审及当前计划为准。
