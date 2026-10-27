# 动态干涉测量科研训练

指导教师：李建欣。围绕动态干涉测量、同步偏振相移、波前与面形恢复，结合论文带读、Python 仿真和 Zemax 学习开展训练。

## 从这里开始

- **当前学习计划**：[复习已有仿真，接入 Zemax 数据并扩展偏振与曝光](docs/handoff/2026-10-27-review-and-practice-plan.md)。
- **当前练习**：[旧静态四步仿真](simulation/python/scripts/simulate_static_four_step.py)与 [Zemax 四帧数据分析](simulation/python/scripts/analyze_zemax_four_step.py)对照。
- **本次数据与结果**：[Zemax 四步分析说明、相位图和原始数据](simulation/python/results/zemax_four_step_2026-10-26/README.md)。
- **理论复习入口**：[第一阶段知识地图](docs/review/00-foundation-knowledge-map.md)。
- **论文阅读入口**：[文献目录与阅读状态](references/README.md)。日期进度文件是历史快照，更新的阅读位置以相应对话和日志为准。

## 文件放在哪里

```text
Research Training/
├── README.md                 项目入口
├── docs/                     理论、阶段复习与当前计划
│   ├── theory/
│   ├── review/
│   └── handoff/
├── research-log/             按日期的学习记录、Zemax 操作日志
├── references/               文献计划、正式带读、AI 预读、本地原文
├── simulation/
│   ├── python/               scripts 源程序、src 公用算法、results 数据与结果
│   └── zemax/                原生模型与模型说明
├── results/zemax/            Zemax 操作与分析截图，按日期保存
├── output/                   可阅读的导出 PDF 和教学插图
├── archive/antigravity/      Antigravity 阶段历史交接资料
└── tmp/                      本地临时缓存，Git 忽略
```

新增代码放 `simulation/python/`，Zemax 模型放 `simulation/zemax/models/`，当前笔记和计划放 `docs/` 或 `research-log/`。`archive/` 用于历史查阅；归档文档里的旧隔离约定不再决定新增文件的位置。

目录详情与整理记录见 [文件导航](docs/project-layout.md)。

## 已有工作与当前边界

| 部分 | 已有记录或结果 | 仍需推进 |
|---|---|---|
| 基础理论 | 双光束干涉、相干性、四步解调、相位展开、Jones 与偏振相移 | 根据实践中的疑问复习 |
| 静态仿真 | 已知高斯面形生成四帧，恢复相位与高度并对照真值 | 接入光学仿真导出数据时的坐标、有效区和评价 |
| 偏振仿真 | 直接构造正交圆偏振后的理想四通道 | 显式加入传感 QWP 及元件对照 |
| 动态仿真 | 整体正弦相位、顺序与理想同步采样、中心时刻真值 | 有限曝光积分、空间采样及其他非理想因素 |
| Zemax | 顺序模式练习；当前对话中的 NSC 双臂与四帧强度导出、解调结果 | 现有模型记录完善及后续偏振联系 |

这些是理论学习与数值仿真成果，不代表实物仪器精度、完整论文复现或真实动态测量完成。

## 运行与版本管理

使用 VS Code 打开整个 `Research Training` 目录。[Python 运行说明](simulation/python/README.md)列出依赖和各程序入口。

- 提交代码、学习笔记、必要模型、可复现的小型数据和代表性结果。
- 本地论文原文、虚拟环境、缓存和 Zemax `.ZDA` 伴随文件按忽略规则保留在本机。
- 保存文件后，Git 提交记录本地版本，推送再同步到 GitHub。仓库身份通过本地 Git 配置管理，不写入项目配置文件。
