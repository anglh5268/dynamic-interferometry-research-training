# Python 仿真与 Zemax 数据分析

## 目录

```text
python/
├── scripts/           可运行的学习与分析程序
├── src/               相位、偏振、动态和面形公用函数
├── results/           按工况保存的输入、图像和指标
└── requirements.txt   Python 依赖
```

## 程序与结果对应

| 程序 | 用途 | 结果目录 |
|---|---|---|
| [simulate_static_four_step.py](scripts/simulate_static_four_step.py) | 800 nm 高斯反射面、理想四步生成/解调、展开与高度恢复 | [case_b_ideal/](results/case_b_ideal/) |
| [simulate_ideal_jones_four_channel.py](scripts/simulate_ideal_jones_four_channel.py) | 单点 Jones 投影与标量四通道核对 | 终端输出 |
| [simulate_jones_case_b.py](scripts/simulate_jones_case_b.py) | 理想 Jones 四通道及二维恢复 | [case_b_jones_ideal/](results/case_b_jones_ideal/) |
| [simulate_dynamic_global.py](scripts/simulate_dynamic_global.py) | 整体正弦动态下顺序/同步比较与参数扫描 | [dynamic_global_ideal/](results/dynamic_global_ideal/) |
| [analyze_zemax_four_step.py](scripts/analyze_zemax_four_step.py) | 读取 Zemax 四帧文本，解调、选择有效区与解析对照 | [zemax_four_step_2026-10-26/](results/zemax_four_step_2026-10-26/README.md) |

## 环境与运行

使用已配置的 Python 环境。从项目根目录安装依赖时使用：

```sh
python -m pip install -r simulation/python/requirements.txt
```

从项目根目录分析已保存的 Zemax 数据：

```sh
python simulation/python/scripts/analyze_zemax_four_step.py
```

默认读取仓库内 `results/zemax_four_step_2026-10-26/inputs/` 中的四份文本，不依赖下载目录。更换数据或输出目录：

```sh
python simulation/python/scripts/analyze_zemax_four_step.py --inputs /path/to/four-frames --output /path/to/results
```

运行旧仿真时，先进入本目录，再以模块方式运行：

```sh
cd simulation/python
python -m scripts.simulate_static_four_step
python -m scripts.simulate_jones_case_b
python -m scripts.simulate_dynamic_global
```

这些是独立程序，按学习任务选择一个运行；会写入各自的结果目录。

## 理解与证据边界

- 静态流程：已知高度 → 相位 → 四帧强度 → 包裹相位 → 展开与对齐 → 高度和误差。
- Jones 程序直接指定相反旋向圆偏振，尚未显式加入传感 QWP。
- 动态程序已定义中心时刻真值与顺序/同步比较，尚未加入曝光积分。
- 公用逐轴 `numpy.unwrap` 适用于相应的平滑、采样充分工况，不是通用二维展开算法。
- Zemax 分析只对连续有效中心剖面展开；载频残差和帧和一致性不等于绝对面形精度。此处的倾斜相位不能直接称作高斯面形恢复。
- [当前复习与实践计划](../../docs/handoff/2026-10-27-review-and-practice-plan.md)规定接下来的学习范围。
