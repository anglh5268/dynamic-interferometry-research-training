# 第一课：双光束干涉与干涉图基本模型

## 1. 本课在项目中的作用

动态干涉测量的核心任务，是根据相机记录的干涉光强恢复物光与参考光之间的相位差，再由相位差求出光程差、波前或表面形貌。本课建立后续相移干涉、偏振干涉和相位解调所使用的基础模型。

## 2. 模型假设

在最基础的标量模型中，暂时假设两束光：

- 频率和波长相同；
- 偏振方向相同；
- 相位关系在曝光时间内稳定；
- 在相机像面上空间重叠。

光的电场本质上是矢量。满足上述条件时，两束光具有相同的电场方向，可以先用标量形式推导。研究偏振相移干涉时，需要恢复到矢量或 Jones 矩阵描述。

## 3. 双光束干涉公式

两束同频光的电场写为

$$
E_1(t)=a_1\cos(\omega t+\varphi_1),
$$

$$
E_2(t)=a_2\cos(\omega t+\varphi_2).
$$

电场满足叠加原理：

$$
E(t)=E_1(t)+E_2(t).
$$

相机不能分辨光场的快速振荡，记录的是与电场平方的时间平均成正比的光强：

$$
I\propto\left\langle E^2(t)\right\rangle.
$$

展开可得

$$
I\propto
\left\langle E_1^2\right\rangle+
\left\langle E_2^2\right\rangle+
2\left\langle E_1E_2\right\rangle.
$$

利用

$$
\left\langle\cos^2(\omega t+\varphi)\right\rangle=\frac{1}{2}
$$

和

$$
\left\langle
\cos(\omega t+\varphi_1)
\cos(\omega t+\varphi_2)
\right\rangle
=\frac{1}{2}\cos(\varphi_1-\varphi_2),
$$

得到

$$
\boxed{
I=I_1+I_2+2\sqrt{I_1I_2}\cos\phi
},
$$

其中

$$
\phi=\varphi_1-\varphi_2
$$

是两束光的相位差。交叉项

$$
2\sqrt{I_1I_2}\cos\phi
$$

使光强随相位差变化，是干涉测量能够获取相位信息的基础。

## 4. 明暗条纹的条件

当

$$
\phi=2m\pi,\quad m\in\mathbb Z
$$

时，$\cos\phi=1$，形成亮条纹：

$$
I_{\max}=I_1+I_2+2\sqrt{I_1I_2}.
$$

当

$$
\phi=(2m+1)\pi
$$

时，$\cos\phi=-1$，形成暗条纹：

$$
I_{\min}=I_1+I_2-2\sqrt{I_1I_2}.
$$

两束光强相等时，理论条纹对比度最高。

## 5. 光程差与相位差

光程定义为

$$
\mathrm{OPL}=nL,
$$

其中 $n$ 为介质折射率，$L$ 为几何传播距离。两条光路的光程差为

$$
\Delta=\mathrm{OPL}_1-\mathrm{OPL}_2.
$$

对波长为 $\lambda$ 的单色光：

$$
\boxed{
\phi=\frac{2\pi}{\lambda}\Delta
}.
$$

折射率通常与波长有关，因此更严谨地写为

$$
\phi(\lambda)=\frac{2\pi}{\lambda}\Delta(\lambda).
$$

对于反射式表面测量，表面高度变化 $h$ 使光多传播一个往返距离：

$$
\Delta=2h,
$$

所以

$$
\boxed{
\phi=\frac{4\pi h}{\lambda}
}.
$$

该式是将测得相位转换为反射表面高度的基础，但实际系统还需考虑入射角、折射率和参考面误差。

## 6. 干涉图的空间模型

实际像面上，两束光的强度和相位随像素位置变化：

$$
I(x,y)=I_1(x,y)+I_2(x,y)
+2\sqrt{I_1(x,y)I_2(x,y)}\cos\phi(x,y).
$$

定义

$$
A(x,y)=I_1(x,y)+I_2(x,y),
$$

$$
B(x,y)=2\sqrt{I_1(x,y)I_2(x,y)},
$$

可写为干涉图的通用表达式：

$$
\boxed{
I(x,y)=A(x,y)+B(x,y)\cos\phi(x,y)
}.
$$

各量的物理意义如下：

- $I(x,y)$：相机实际记录的像素光强；
- $A(x,y)$：背景光强或直流分量，决定局部平均亮度；
- $B(x,y)$：调制度，决定局部条纹明暗变化幅度；
- $\phi(x,y)$：物光与参考光在各像素位置的相位差。

空间相位可以表示为

$$
\phi(x,y)=\varphi_{\mathrm{obj}}(x,y)-\varphi_{\mathrm{ref}}(x,y)
=\frac{2\pi}{\lambda}\Delta(x,y).
$$

因此，测量结果通常是物光波前相对于参考光波前的差，而不是绝对相位。

## 7. 矢量与偏振的影响

两束线偏振光的偏振方向夹角为 $\theta$ 时，理想相干条件下有

$$
I=I_1+I_2+2\sqrt{I_1I_2}\cos\theta\cos\phi.
$$

- $\theta=0$：偏振方向相同，干涉项最大；
- $\theta=\pi/2$：偏振方向正交，直接叠加时干涉项为零；
- 其他夹角：条纹调制度降低。

更一般的复矢量形式为

$$
I\propto
|\boldsymbol E_1|^2+|\boldsymbol E_2|^2
+2\mathrm{Re}
\left(\boldsymbol E_1\cdot\boldsymbol E_2^*\right).
$$

该结论与本课题直接相关：同步偏振干涉正是通过控制和分析偏振分量，得到具有不同相移的干涉信号。

## 8. 不同波长的情况

若两束光的角频率不同，干涉项随时间变化：

$$
I_{\mathrm{cross}}(t)\propto
\cos\left[(\omega_1-\omega_2)t+(\varphi_1-\varphi_2)\right].
$$

频率差较大时，该项在相机曝光期间快速振荡，时间平均后趋近于零，难以形成稳定条纹。频率非常接近且探测器足够快时，可以检测拍频，这是外差干涉的基础。

宽光谱光源包含多个波长，各波长对应不同相位。只有在较小光程差范围内，各波长的干涉信号才能较好重合，因此宽光谱光源的相干长度通常较短。本项目初期采用单色光模型。

## 9. 为什么不能由一幅普通干涉图直接唯一求相位

单幅干涉图模型

$$
I=A+B\cos\phi
$$

同时包含 $A$、$B$ 和 $\phi$ 等未知量，而且

$$
\cos\phi=\cos(-\phi)=\cos(\phi+2m\pi).
$$

因此，仅凭单个像素的光强通常无法唯一确定相位。相移干涉通过引入多个已知相移建立多组方程，从而分离背景、调制度和相位。

## 10. 与后续研究的连接

本课建立了动态干涉测量的基础链条：

$$
\text{被测形貌或波前}
\rightarrow\text{光程差}
\rightarrow\text{相位差}
\rightarrow\text{干涉光强}
\rightarrow\text{相机图像}.
$$

后续相位解调要完成逆过程：

$$
\text{干涉图}
\rightarrow\text{相位}
\rightarrow\text{光程差}
\rightarrow\text{波前或表面形貌}.
$$

下一步需要学习相干条件、条纹对比度以及四步相移法。

## 11. 本课结论

1. 光场进行矢量叠加；偏振方向相同时可用标量模型简化。
2. 干涉项来自总电场平方中的交叉项，并包含两束光的相位差。
3. 对单色光，光程差通过 $\phi=2\pi\Delta/\lambda$ 转化为相位差。
4. 干涉图可写成 $I=A+B\cos\phi$，其中 $A$ 是背景，$B$ 是调制度，$\phi$ 是待恢复的空间相位。
5. 干涉测量得到的是物光与参考光的相对相位；相移算法用于从光强中恢复该相位。
