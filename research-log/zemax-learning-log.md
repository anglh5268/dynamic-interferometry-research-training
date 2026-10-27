# Zemax 学习记录

## 2026-10-14：交接核对与恢复学习

### 本次目标

依据当前 Windows 软件界面，读懂已有单透镜的表面、介质和传播距离；确认实际进度后继续操作。

### 已核对的资料

- `docs/handoff/2026-10-14-zemax-learning-handoff.md`。
- 用户提供的 `Zemax_AI学习交接文档.md`。
- 本地 `single_lens_F4.zmx`：AI 读取了文件，未运行 OpticStudio。
- Ansys 官方顺序模式、非顺序模式和单透镜分析教程。

### 本地模型参数

| 参数 | 文件记录 |
|---|---|
| 模式与长度单位 | Sequential；mm |
| 入瞳直径字段 | 25 mm |
| 视场 | X=0；Y=0、3.5、5；角度视场 |
| 主波长 | 编号 1，0.6328 μm；活动波长数量待界面核对 |
| 物面 | 无穷远 |
| 表面 1 | STOP；平面；之后为 4 mm N-BK7 |
| 表面 2 | 半径约 −51.509 mm；曲率带解算字段；之后为 100 mm 空气 |
| 像面 | 平面 |

### 证据与学习状态

- 软件已安装：来自用户交接资料；当前版本、Edition、可用功能待用户确认。
- Windows 当前模型是否与本地文件一致：待核对。
- AI 本次说明：顺序/非顺序追迹的区别，以及单透镜中表面与实体镜片的区别。
- 用户本次操作、理解反馈和分析结果：尚未收到；不记作完成练习。
- 本地原模型未修改；本次没有生成新的追迹、点列图或波前结果。

### 下一步

用户打开 Windows 中的当前模型，提供主界面和 Lens Data Editor 截图，并说明上次停在哪一步。根据实际界面继续；若已有点列图，优先结合 Layout 解释像面位置，再决定是否做离焦对照。

### 后续记录方式

每次记录用户实际操作、模型版本、参数与解算、分析设置、对照结果、用户自己的解释、AI 的补充和未验证事项。

### 用户补充与计划更新

- 用户确认通过 UU 远程控制 Windows，并明确要求先制定学习计划、开始学习。
- 计划保存为 `docs/handoff/2026-10-14-zemax-learning-plan.md`：单透镜恢复与重建 → 焦点和像差 → 波前/OPD → 反射往返 → 简化干涉光路与 Python 连接。
- 官方 Student 版不支持非顺序模式及 ZPL/ZOS-API；用户当前 Edition 仍待核对，主线先按顺序模式安排。
- 当前阅读记录比交接说明进一步推进了徐晨论文 §2.3.3；本次以实际阅读记录为背景，不重复展开文献教学。
- 今日第一节入口：通过 UU 打开 OpticStudio，提供当前主界面，再读懂已有单透镜。尚未收到用户操作结果。

### Windows 界面首次核对

- 用户通过截图确认当前软件为 Ansys Zemax OpticStudio 2026 R1.00 Student；顺序模式已选中，文件标题为 `single_lens_F4.ZMX`。
- Lens Data Editor 显示 OBJECT、STOP、表面 2、IMAGE 四行；STOP 为平面，之后 4.000 mm N-BK7；表面 2 半径显示截断的负值，带 F 解算标记，之后为 100.000 mm 空气。可见参数与本地文件一致，完整半径与解算对话框尚未核对。
- 状态栏显示 EFFL=100、ENPD=25；未据此确认全部系统设置或分析结果。
- 顶部 Setup 页可见 Cross-Section 按钮。下一步让用户打开二维光路图，对应前后表面及像面；尚未修改参数或完成对照。

### 用户已打开 Layout

- 用户提供当前二维 Layout 截图：左侧为平凸单透镜，右侧为像面；显示蓝、绿、红三组光线，Total Axial Length=104.00000 mm。
- 用户实际完成操作：打开光路图。尚未收到用户自己的物理解释。
- AI 说明：像面是选定的观察位置，不由绘图本身保证处于最佳焦点；不同组光线的交叉区不同，同组光线也未必在一个点相交，定量判断需后续点列图。
- 本地文件有三个视场，预计当前颜色用于区分视场；活动波长与 Layout 着色设置尚未在 Windows 核对，不把颜色直接认作激光波长。
- 下一步：展开 System Explorer 的 Fields 和 Wavelengths，核对入射方向与活动波长。暂未改变模型参数。

### 视场与活动波长核对

- 用户展开了 Fields 和 Wavelengths 并提供截图：三个视场 X 均为 0，Y 分别为 0、3.500、5.000，权重均为 1；当前仅一个活动波长，界面四舍五入显示 0.633 μm，权重为 1。
- 波长显示与本地文件的 0.6328 μm 一致。当前 Fields 展开区未显示视场类型；本地文件记录角度视场，下一步在 Field Data Editor 核对 Angle。
- AI 本节说明：无穷远物体的不同物点对应不同入射方向；同一视场的光线从入瞳不同位置进入；Layout 三种颜色用于区分三组视场光线，不能认作三种波长。
- 布置练习（尚未完成）：先在 Windows 另存副本 `single_lens_field_test.zmx`，核对角度视场后只将第三视场 Y 从 5 改为 2.5，观察 Layout 中该组光线和像面落点的变化。其余参数保持原设置，修改后核对镜片曲率及解算有无变化。

### 视场修改后的用户反馈

- 用户提供新的 Layout，文件名显示 `single_lens_field_test.ZMX`，确认已另存练习副本；Total Axial Length 仍为 104.00000 mm。
- 用户观察：“绿色的光线应该是更靠近蓝色光线了”，并询问修改了什么、影响了什么。
- 图上像面附近红色光线落在蓝色与绿色之间，符合第三视场从 5° 改为 2.5°、小于第二视场 3.5° 的预期；新参数表未显示，具体修改行与 Angle 类型仍待核对。
- AI 本次重点解释：角度视场指定无穷远物点方向；减小视场角使输入光束方向更接近光轴，像的位置随之靠近轴上像点。近轴理想成像的 h≈fθ（θ 用弧度）用于说明趋势，实际落点和光斑大小需追迹分析。
- 下次核对 Field Data Editor 的实际三行数值，避免只凭颜色或线条交叉判断修改对象；用户尚未完成聚焦质量的定量对照。

### Field Data Editor 参数确认

- 用户提供完整视场表：Field Type=Angle；三行 (X Angle, Y Angle) 分别为 (0°,0°)、(0°,3.5°)、(0°,2.5°)，Weight 全为 1，截图可见 VDX 全为 0。
- 第三视场 Y 从原始 5° 改成 2.5° 已得到界面确认。当前三行编号不按角度大小排序。
- AI 解释截图中的 Comment、X/Y Angle、Weight、VDX 和右侧视场坐标图。Weight 为计算/优化中的相对权重；VDX 为该视场表观入瞳的归一化 X 偏移，属于渐晕因子，保持零值即可。
- 官方依据：Ansys 单透镜设置教程、OpticStudio Vignetting Factors 定义。用户目前询问参数意义，本轮先解释当前表，不追加新的参数修改。

### 视场角的交互示意

- 用户请求更直观的表示，AI 制作可调 X/Y 角度的理想薄透镜教学示意，固定 f=100 mm，包含光路投影、像面正视图及原始 5°/当前 2.5° 切换。
- 第一、第二视场固定，第三视场可调；用同色多条平行入射光线表示一个物点经不同入瞳位置的光路。
- 这是独立教学近似，未读取或运行 Windows Zemax 追迹，不代表实际镜片像差和点列图。
- 已验证预设切换、X 角调整、投影切换及窄屏显示；尚未收到用户基于示意的理解反馈。

### 孔径界面与教学方式补充

- 用户明确要求：后续每遇到新界面，介绍英文名称、中文含义和参数作用。按当前练习解释，不要求预先熟悉英文术语。此偏好记录在项目日志，未写入全局记忆。
- 用户截图确认 Aperture Type=Entrance Pupil Diameter、Aperture Value=25.0、Apodization Type=Uniform；两种通光半径余量均为 0，全局坐标参考面为 1。
- 复选框状态：Telecentric Object Space 灰色未勾选；Afocal Image Space、Iterate Solves When Updating、Check GRIN Apertures 未勾选；Fast Semi-Diameters 已勾选。
- AI 逐项翻译并解释该界面。孔径缩小对照尚未执行。
- 操作前发现需处理的联动：此前后表面 Radius 带 F 标记，本地曲率解算为 F/#=4。直接改变入瞳直径可能触发曲率变化。下一步先打开该曲率解算确认，在新练习副本中固定当前半径，再做只改变入瞳直径的对照。
- 官方依据：2026 R1 孔径类型、切趾、半直径余量、坐标参考、远心、无焦、迭代、GRIN 帮助，以及单透镜教程的 F Number 解算说明；Fast Semi-Diameters 参考可访问的 2025 R1 官方说明。

### 曲率解算窗口确认

- 用户成功打开 `Curvature solve on surface 2`：Solve Type=F Number，F/#=4。确认后表面存在 F 数曲率解算。
- AI 解释窗口标签及当前空气中无穷远成像的近轴关系 N=f/D：当前 D=25 mm、f≈100 mm，N=4；若保留该解算而把 D 减半，软件会调整曲率以维持 N=4，焦距也会随之变化。
- 下一步操作要求：在 Windows 另存孔径练习副本，再将解算类型改为 Fixed、按 Enter 确认，核对 F 标记消失且半径数值保持原值。此步骤尚未收到完成截图，入瞳直径仍按 25 mm 记录。

### 固定曲率完成，进入孔径减半对照

- 用户提供新的 Lens Data Editor 截图：后表面 Radius 旁的 F 标记已消失，数值仍显示截断的 −51.5…；玻璃厚度为 4.000 mm、后表面到像面为 100.000 mm，STOP 通光半径仍为 12.500 mm。符合将曲率解算改为 Fixed 并保留当前值的预期；完整半径与另存文件名未在此截图中显示。
- 下一步：保存当前 25 mm 基准版本，另存 `single_lens_aperture_12p5.zmx`，仅将 Aperture Value 从 25.0 改为 12.5，再查看 Layout 和状态栏。
- 预期：入射光束宽度减半、近轴焦距保持约 100 mm；自动 Clear Semi-Dia 可能随追迹光束范围减小，Layout 透镜轮廓也可能缩小。自动口径变化不等于曲率改变。
- 12.5 mm 操作与对应分析结果尚未收到，不记为已完成。

### 12.5 mm 孔径对照已操作

- 用户提供截图确认当前 Layout 文件名为 `single_lens_aperture_12p5.ZMX`，Aperture Value=12.5，类型仍为 Entrance Pupil Diameter。
- STOP 自动通光半径为 6.250 mm，后表面自动通光半径为 6.395 mm，像面为 6.364 mm；总轴向长度仍为 104.00000 mm。三视场 Y=0、3.5、2.5，活动波长显示 0.633 μm。
- 光路图显示通光范围缩小，符合入瞳直径减半的预期。图窗口遮住曲率与厚度列，截图未包含 EFFL 状态栏，未在本张截图重新确认完整半径与有效焦距。
- 用户询问 Save As 之后操作哪个文件。AI 说明：另存成功后当前工作文件切换为新文件，后续 Save 保存到新文件；另存后继续修改的参数还需要再次保存。原文件保留另存之前已保存的状态。
- 待用户保存当前 12.5 mm 修改；后续用 Spot Diagram 定量观察像面光斑，不仅凭 Layout 判断像质。

### 下一节：打开标准点列图

- 用户要求继续操作。AI 根据 2026 R1 官方菜单说明引导 Analyze → Image Quality → Rays and Spots → Standard Spot Diagram。
- 本节先认识一条追迹光线的像面落点与一个物点的点列图，暂不使用 Quick Focus 或改变分析设置。
- 待用户提供包含各视场、RMS/GEO 半径及单位的完整点列图，随后记录 12.5 mm 结果并与 25 mm 基准比较。

### 12.5 mm 标准点列图结果

- 用户成功打开 Standard Spot Diagram，并询问界面的用途；截图文件名为 `single_lens_aperture_12p5.ZMX`。
- Surface=IMA，Reference=Chief Ray；Units are μm；Scale bar=1000.00 μm。图例按波长，当前显示约 0.633 μm，所有追迹落点呈同一种颜色。
- 各视场结果（半径单位 μm）：

| Field | OBJ 角度 | IMA 参考像高 / mm | RMS radius / μm | GEO radius / μm |
|---|---:|---:|---:|---:|
| 1 | 0° | 0.000 | 66.424 | 107.739 |
| 2 | 3.5° | 6.115 | 101.091 | 249.108 |
| 3 | 2.5° | 4.366 | 85.020 | 200.260 |

- AI 解释：每个小十字为一条追迹光线的像面落点，每个小图对应一个物点；各图围绕自身主光线参考点显示，不能把三图中心的位置当作实际像点位置。IMA 像高表示像的位置，RMS/GEO 表示该位置周围光斑的大小。
- 同条件下当前 RMS 为轴上最小、3.5° 最大；未仅凭形状判定具体像差，也未宣布当前像面为最佳焦点。
- 点列图是几何追迹落点；环状采样分布不直接作为衍射环、干涉条纹或真实光强分布。当前记录为用户软件截图读数，AI 未独立运行 Windows 模型。
- 后续比较应保持视场、波长、像面位置、采样及 Chief Ray 参考一致，读取 25 mm 基准的实际结果，不引用旧截图数值代替本次对照。

### 点列图设置已核对

- 用户展开 Settings，截图确认：Ray Density=6，Pattern=Hexapolar，Color Rays By=Waves，Refer To=Chief Ray；Wavelength=All、Field=All、Surface=Image。
- Show Scale=Scale Bar，Plot Scale=0（自动）。Use Polarization、Direction Cosines、Show Airy Disk 未勾选；Use Symbols、Auto Apply 已勾选。
- 当前 RMS/GEO 数值与上次截图一致。Hexapolar 的 Ray Density=6 表示 6 圈采样，不是 6 条光线；点列图环状排列与入瞳采样相关。
- 比较阶段保留 Plot Scale=0，先比较数值；自动绘图缩放可能导致图上大小不能直接比较，后续如制作并排图再统一尺度。
- 下一步：保存当前模型，打开 `single_lens_aperture_test.zmx`，确认入瞳直径为 25 mm；按上述设置读取实际点列图。该基准文件的实际加载与新结果尚未确认。
- 本设置窗中的 Save/Load 是保存/加载分析设置；模型文件仍通过 File 菜单 Save/Save As 保存。

### 25 mm 基准点列图与孔径对照完成

- 用户已打开 `single_lens_aperture_test.ZMX`，提供实际点列图及 Settings：Ray Density=6、Hexapolar、Waves、Chief Ray、Wavelength/Field=All、Surface=Image；复选框状态与 12.5 mm 对照一致。
- 图后方 STOP 的通光半径显示 12.500 mm，符合 25 mm 入瞳；曲率列被窗口遮住，未从本张截图重新读取完整半径或 EFFL。
- 两组主光线参考像高相同：0.000、6.115、4.366 mm。原始截图已复制到 `results/zemax/2026-10-14/`，分别为 `aperture-25-spot-settings.png` 和 `aperture-12p5-spot-settings.png`。

| 视场角 | 25 mm RMS / μm | 12.5 mm RMS / μm | RMS 缩小倍数 | 25 mm GEO / μm | 12.5 mm GEO / μm |
|---|---:|---:|---:|---:|---:|
| 0° | 562.738 | 66.424 | 8.47 | 918.136 | 107.739 |
| 3.5° | 649.544 | 101.091 | 6.43 | 1471.00 | 249.108 |
| 2.5° | 607.794 | 85.020 | 7.15 | 1291.69 | 200.260 |

- 25 mm 图自动比例尺为 4000 μm，12.5 mm 图为 1000 μm；不能直接用图上显示大小作比较。
- 此对照支持：在当前像面位置和上述分析设置下，缩小入瞳使几何落点分布更集中。没有做像差分解、最佳焦面搜索或衍射分析，不能推广为所有系统孔径越小越好，也不能据此声称仪器精度。
- AI 物理解释：缩小孔径使光线更多通过镜片中心附近；边缘光线在球面单透镜中与近轴光线会聚位置不同（球差），离轴还可能有其他像差；像面位置与孔径共同影响本次点列图，尚未定量分离各项。
- 后续目标：固定孔径和镜片形状，单独改变像面距离以认识离焦，再按需要用 Quick Focus。新的调焦模型与结果尚未产生。

### 95 mm 像面距离练习与圈状落点问题

- 用户提供 `single_lens_focus_95.ZMX` 的 Layout 与点列图。Layout 的 Total Axial Length=99.00000 mm，与玻璃厚度 4 mm、后表面到像面 95 mm 相符（原始总长 104 mm）。图后方 STOP 通光半径仍为 12.500 mm，符合 25 mm 孔径。
- 用户观察：“像点好像差不多落在了右边的像面上，并且 Total Axial Length 这个值变了”；对离轴点列图中大小圈的相交表示疑惑。
- 本次 Surface=IMA、Reference=Chief Ray、波长约 0.633 μm、单位 μm、自动比例尺 2000 μm；没有提供新的 Settings 展开图，按前面保持设置的练习流程记录，采样尚未在这张截图重新展示。

| 视场角 | 100 mm 距离 RMS / μm | 95 mm 距离 RMS / μm | 95 mm GEO / μm | 95 mm 参考像高 / mm |
|---|---:|---:|---:|---:|
| 0° | 562.738 | 184.001 | 257.403 | 0.000 |
| 3.5° | 649.544 | 291.307 | 784.303 | 5.818 |
| 2.5° | 607.794 | 243.019 | 613.472 | 4.154 |

- 原始截图保存到 `results/zemax/2026-10-14/focus-95-layout.png` 和 `focus-95-spot.png`。
- AI 解释：Total Axial Length 是此直通模型从首个透镜表面到像面的轴向总长，当前为 4+95=99 mm；不是修改焦距的操作。
- 圈状落点源于 Hexapolar 入瞳分圈采样经光学系统映射到像面。同一物点的不同入瞳采样圈，在像差和离焦影响下可以变形、偏移并交叠；落点圈的大小不能直接反推采样圈的内外顺序。不是多个物点或艾里斑参考圈。
- 轴上与离轴的形状差异可用旋转对称性、球差与离轴非对称像差作定性说明；本次没有逐条光线标记或像差分解，不从图形直接定量确认各项。
- 本次数据支持 95 mm 比 100 mm 的几何光斑更集中；未完成最佳焦面搜索。

### 下一节：快速调焦

- 用户要求继续学习。AI 核对 2026 R1 官方 Quick Focus 说明：Optimize → Manual Adjustment → Quick Focus；该工具调整像面前一面的 Thickness，以指定 RMS 标准、所有视场/波长及其权重寻找焦面。
- 计划在保存 95 mm 模型后另存 `single_lens_quick_focus.zmx`，保持入瞳 25 mm、镜片曲率固定、玻璃厚度及视场/波长不变。
- 本轮拟用 Spot Size Radial，Use Centroid 先不勾选，以保持与前面 Chief Ray 参考的点列图一致；实际选项待用户打开对话框核对，再执行。
- 说明“最佳”依赖评价标准，综合焦面不保证每个视场分别达到最小光斑。运行及结果尚未完成。

### Quick Focus 评价标准界面确认

- 用户已打开 Quick Focus 下拉列表，截图显示 Spot Size Radial、Spot Size X Only、Spot Size Y Only、RMS Wavefront 四项。
- AI 逐项翻译：二维径向光斑 RMS、仅 X 向光斑 RMS、仅 Y 向光斑 RMS、波前误差 RMS。
- 引导选择 Spot Size Radial；收起列表后核对 Use Centroid（使用落点重心），本轮保持未勾选以采用 Chief Ray 参考，再运行并记录第 2 行新 Thickness 与各视场 RMS。
- 此截图只显示下拉菜单，Use Centroid 状态、当前模型文件名及运行后结果尚未确认。

### Quick Focus 运行结果：当前点列图略变差

- 用户提供 `single_lens_quick_focus.ZMX` 的 Layout 与点列图，并判断“没有改善很多”。原始截图保存为 `results/zemax/2026-10-14/quick-focus-layout.png` 和 `quick-focus-spot.png`。
- Total Axial Length=99.10258 mm；在玻璃厚度仍为 4 mm 的设置下，推算后表面到像面约 95.10258 mm（Thickness 列被遮挡，未直接读取）。与 95 mm 基准相比只移动约 0.10258 mm。
- 点列图 Surface=IMA、Reference=Chief Ray、波长约 0.633 μm、比例尺 2000 μm。Use Centroid 的实际运行状态尚未在截图中确认。

| 视场角 | 95 mm 基准 RMS / μm | Quick Focus 后 RMS / μm | RMS 增幅 | Quick Focus 后 GEO / μm |
|---|---:|---:|---:|---:|
| 0° | 184.001 | 186.311 | 1.25% | 270.959 |
| 3.5° | 291.307 | 294.579 | 1.12% | 798.392 |
| 2.5° | 243.019 | 245.871 | 1.17% | 627.387 |

- 按等权视场 RMS 平方平均再开方，综合值从约 243.430 μm 变为 246.266 μm；这是 AI 对截图数值计算的汇总，不是软件报告的 Quick Focus 内部目标值。
- 本次不能记为像质改善或已验证最佳焦点：所有已显示的 Chief Ray RMS 均略增大，不能用不同视场间的综合折中解释本次变化。
- 原因尚未确定；参考点实际设置或采样差异仅为待检查方向，未证实。下一步重新打开完整 Quick Focus 对话框，核对 Spot Size Radial 与 Use Centroid，先不重复运行。

### Quick Focus 设置核对完成，布置三点手动扫描

- 用户完整截图确认 Spot Size Radial 已选中、Use Centroid 未勾选；第 2 行 Thickness 显示 95.103 mm，Radius 旁无 F 标记，STOP 通光半径 12.500 mm、玻璃厚度 4.000 mm。
- 排除当前对话框与目标设定的明显参考点不一致；前次运行时设置按用户操作流程推定，不再把重心勾选作为已发生原因。
- 设置截图保留为 `results/zemax/2026-10-14/quick-focus-settings-confirmed.png`。
- 原因仍未确定；采样差异只是可能性。本节不继续猜测 Quick Focus 内部算法。
- 下一步 Close 关闭工具，在新副本 `single_lens_focus_scan.zmx` 中固定其他条件，分别读取像面距离 94.5、95.0、95.5 mm 的三个视场 RMS。Ray Density=6、Hexapolar、Chief Ray 等分析设置保持一致。
- 95.0 mm 现有读数可作参考，但让用户在新副本中实际刷新核对；三点只能比较这三个位置，不能宣称已求出精确最佳焦点。

### 三点焦面比较与练习用途反馈

- 用户提供两张 `single_lens_focus_scan.ZMX` 点列图，并询问“给你这些有什么用呢”。AI 承认前面未先说明实验要回答的问题，后续先给验证问题、控制变量和结果判断标准，再布置操作。
- 两张图未显示 Thickness，也未由用户文字标注距离；按前面布置的操作顺序，暂将第一张对应 94.5 mm、第二张对应 95.5 mm。距离映射是流程推定，不能当作截图直接读取。
- 原始截图保留为 `results/zemax/2026-10-14/focus-scan-first-spot.png` 和 `focus-scan-second-spot.png`，以顺序命名，避免假定未经显示的距离。

| 位置（前两项按流程推定） | 0° RMS / μm | 3.5° RMS / μm | 2.5° RMS / μm |
|---|---:|---:|---:|
| 第一张，预计 94.5 mm | 180.702 | 280.206 | 235.042 |
| 已确认 95 mm 基准 | 184.001 | 291.307 | 243.019 |
| 第二张，预计 95.5 mm | 199.957 | 310.127 | 260.426 |

- 第一张 GEO 半径依次为 240.611、715.634、545.650 μm，参考像高为 0.000、5.788、4.132 mm；第二张 GEO 半径为 323.476、852.972、681.294 μm，参考像高为 0.000、5.847、4.174 mm。
- 两张图均 Surface=IMA、Reference=Chief Ray、波长约 0.633 μm、比例尺 2000 μm，STOP 通光半径背景显示与 25 mm 孔径一致。新的采样设置未展开，按保持不变的操作要求理解。
- 用途与结论：在三组已记录结果中，第一张三个视场 RMS 都最小；若实际距离与操作顺序一致，94.5 mm 是这三个位置中较好的位置，像面应朝透镜方向调整。未验证精确最佳焦点，也未确认 Quick Focus 与点列图产生差异的原因。
- 学习成果是单变量对照与按实际数值选择设置；与实验成像系统中调整镜头到相机的间距相关。本轮无需继续追求更小数值，下一阶段按既定计划进入波前/OPD。

### 今日结束与总结

- 用户明确要求今天学习到此结束，并总结本次 Zemax 学习；不再开展新的软件操作。
- 总结保存为 `docs/review/2026-10-14-zemax-learning-summary.md`，包含界面词汇、物理场景、视场/孔径/焦面三类练习、实际 RMS 对照、Quick Focus 未改善结果、文件证据及下次入口。
- 今日进度：完成已有单透镜上的有指导操作与基础分析；从空白独立建立模型、OPD、反射与干涉仪练习尚未完成。
- 下次先核对保存模型及扫描截图距离映射，再进入波前/OPD；Windows 修改模型尚未同步到 Mac。

## 2026-10-15：波前与 OPD 入门（开始）

### 今日目标与用途

先读懂单透镜轴上视场的一张 OPD 图，认识瞳坐标、光程差单位和参考波前；条件核对后，再只改变像面距离观察 OPD 变化。用途是把昨天的几何光线落点分析连接到相位与干涉测量。

### 开始前核对

- 已重读 2026-10-14 总结与逐步日志。昨日完成视场、孔径、像面位置等有指导对照，尚未开始 OPD。
- 本地项目目前仍仅有原始 `single_lens_F4.zmx`，Windows 修改模型尚未同步；当前 Windows 文件与界面需重新查看。
- 昨日两张扫描图的距离按操作顺序推定为 94.5/95.5 mm，尚未通过截图直接读取，不默认今天载入文件就处于 94.5 mm。
- 今日第一步请用户通过 UU 打开 `single_lens_focus_scan.ZMX`，提供含文件标题、Lens Data Editor、Aperture 的截图；先读取实际孔径、曲率解算和像面距离，再设置今天的练习副本。

### 本节物理说明与证据状态

- 同一物点的光经透镜不同入瞳位置传播；在成像分析中，相对于指定理想参考波前的光程偏差用于描述波前误差。具体参考方式待查看当前模型设置。
- 单透镜 OPD 分析的参考波前需与未来干涉仪两臂比较的坐标和光程基准分别明确。
- 今日尚未收到软件截图、运行新的 OPD 分析或取得数值，不记作已完成练习。
- 官方依据：[2026 R1 Optical Path Difference](https://ansyshelp.ansys.com/public/Views/Secured/Zemax/v261/en/OpticStudio_User_Guide/OpticStudio_Help/topics/Optical_Path_Difference.html)、[Reference OPD](https://ansyshelp.ansys.com/public/Views/Secured/Zemax/v261/en/OpticStudio_User_Guide/OpticStudio_Help/topics/Reference_OPD.html)。

## 2026-10-18：恢复模型，准备打开 OPD 分析

- 用户重新提供 Windows 界面，当前文件在点列图页脚显示为 `single_lens_focus_scan.ZMX`；Aperture Type=Entrance Pupil Diameter，Value=25.0，Apodization=Uniform。
- 参数表直接确认：物面无穷远；前表面为 STOP、平面，之后 4.000 mm N-BK7；后表面 Radius 显示截断的 −51.5…，旁边没有 F 标记，之后 95.500 mm 空气；像面平面。
- 当前点列图 RMS=199.957、310.127、260.426 μm，与 10 月 14 日第二张扫描图一致。本次恢复状态直接证实 95.500 mm 对应这组读数，支持此前对第二张扫描图的距离推定；第一张扫描图的 94.5 mm 对应关系仍未直接核对。
- 结果截图保留在 `results/zemax/2026-10-18/resume-spot-aperture.png` 与 `resume-lens-data-95p5.png`。
- 今天以实际读取的 95.500 mm 为 OPD 起点，不把该位置称为最佳焦面。
- 下一步：用户另存 `single_lens_opd_95p5.zmx`，保持模型参数，进入 Analyze → Image Quality → Aberrations → Optical Path Difference；先提供完整 OPD 图，随后核对坐标、单位、参考与分析设置。
- 尚未收到另存后的文件名或 OPD 结果，不记作已完成分析。

### 第一张 OPD Fan 已打开

- 用户提供 OPD Fan 图，页脚文件名为 `single_lens_opd_95p5.ZMX`，确认已另存并打开 OPD 分析。原图保留为 `results/zemax/2026-10-18/opd-95p5-all-fields.png`。
- 图中三个视场为 0°、3.5°、2.5°；每组有 Py 和 Px 两个入瞳方向的切线图；蓝色波长图例为 0.633 μm，Surface=Image，Maximum Scale=±50.000 Waves。
- 本节先读轴上 0°：左右两条曲线形状相同且关于瞳中心对称；在参考零线外存在明显非零 OPD。未从截图提取精确峰谷值或 RMS，也未按曲线形状定量拆分像差。
- AI 解释：横轴为归一化入瞳位置，标准全瞳范围 −1 至 +1；当前入瞳直径 25 mm，对应直径两端约 −12.5 与 +12.5 mm。Py/Px 是同一物点光束的两个正交瞳方向，不代表两条干涉臂。
- 纵轴 W 的单位为 waves，即 OPD/λ；用界面近似波长 0.633 μm，1 wave 对应约 0.633 μm 光程差。±50 Waves 为显示量程，不是测得的波前 RMS 或 PV。零值表示相对所选参考的光程偏差为零。
- 下一步打开 Settings，先核对与翻译分析设置，拟将 Field 从 All 改为 1（轴上 0°），其余值先保持，简化为两个方向的曲线；实际设置截图尚未收到，参考 OPD 模式尚未在 System Explorer > Advanced 中查看。

### OPD 设置初次核对

- 用户展开 OPD Fan 设置。Plot Scale=0（自动）、Number Of Rays=20、Wavelength=All、Field=All、Surface=Image；Use Dashes 未勾选，Vignetted Pupil、Check Apertures、Auto Apply 已勾选。
- 截图保存为 `results/zemax/2026-10-18/opd-95p5-settings-initial.png`。
- AI 解释：Number Of Rays 为每个扫描方向原点每侧的光线采样数，区别于点列图 Hexapolar 的圈数；Vignetted Pupil 控制归一化瞳范围的处理，Check Apertures 控制是否排除未通过表面孔径的光线。
- 下一步仅将 Field 选为 1、Plot Scale 设为 50（显示 ±50 waves），其余维持，点击 OK 收起并查看两幅轴上切线图。该设置作为后续像面距离对照的统一显示条件。
- 模型仍以入瞳 25 mm、像面距离 95.500 mm 为起点；本轮尚未修改物理参数。实际参考 OPD 模式与修改后显示仍待核对。

### 轴上 OPD 图含义讲解

- 用户提供简化后的 OPD Fan 并问“这个图显示的是什么意义呢”。当前仅显示 OBJ=0° 的 Py/Px 两幅图，Maximum Scale=±50 waves，文件名 `single_lens_opd_95p5.ZMX`；图片保存为 `results/zemax/2026-10-18/opd-95p5-field1-scale50.png`。
- AI 用入瞳中心与靠近边缘的位置解释曲线：每个入瞳坐标对应一条采样光线；纵轴是参考波前下以波长计的光程偏差，不是传播轨迹或像面高度。
- 曲线中心约为零，两侧谷底从网格粗读约 −20 waves；该数仅为视觉估读，没有从 Text 导出精确值。按图例约 0.633 μm 换算，偏差量级约 −12.7 μm。中心归零与参考定义有关，不能据此判断整个系统无波前误差。
- 两图形状相同且对称，符合轴上轴对称模型；当前所选参考下波前偏差随瞳位置变化，没有做像差分解。
- 图左上灰框 `Pupil=-0.424X, Data=43.41` 为活动鼠标坐标读数；当前数值不在蓝色曲线上，不能当作该处曲线值、最大 OPD 或 RMS。
- 先解释曲线意义，再进行像面距离的单变量对照；用户尚未完成精确读数或新的物理参数修改。
