# 第五课：偏振光、Jones矩阵与同步偏振相移

## 1. 本课在项目中的作用

同步偏振干涉利用偏振状态编码不同相移，并在一次曝光中获得多通道干涉图。理解该方法需要掌握：

- Jones矢量如何由真实电场得到；
- 复数模平方和光强如何计算；
- 线偏振片为什么是矢量投影；
- 波片如何改变两个正交分量的相对相位；
- 四个检偏方向如何形成四步相移。

## 2. 从真实电场到Jones矢量

设光沿 $z$ 方向传播，电场位于 $x-y$ 平面：

$$
\boldsymbol E(z,t)=
\begin{bmatrix}
E_x(z,t)\\
E_y(z,t)
\end{bmatrix}.
$$

两个正交分量写成

$$
E_x=A_x\cos(\omega t-kz+\varphi_x),
$$

$$
E_y=A_y\cos(\omega t-kz+\varphi_y).
$$

利用复数表示：

$$
E_x=\mathrm{Re}
\left[A_xe^{i\varphi_x}e^{i(\omega t-kz)}\right],
$$

$$
E_y=\mathrm{Re}
\left[A_ye^{i\varphi_y}e^{i(\omega t-kz)}\right].
$$

两个分量具有相同的时间和传播因子 $e^{i(\omega t-kz)}$。研究偏振状态时，保留两个方向的复振幅，得到Jones矢量：

$$
\boxed{
\boldsymbol J=
\begin{bmatrix}
A_xe^{i\varphi_x}\\
A_ye^{i\varphi_y}
\end{bmatrix}
}.
$$

Jones矢量的第一项记录 $x$ 分量的振幅和相位，第二项记录 $y$ 分量的振幅和相位。它不是某个时刻的真实电场，而是两个电场分量的复振幅表示。

提取公共相位后：

$$
\boldsymbol J
=e^{i\varphi_x}
\begin{bmatrix}
A_x\\
A_ye^{i\delta}
\end{bmatrix},
\qquad
\delta=\varphi_y-\varphi_x.
$$

只研究偏振形状时，公共相位可以忽略；干涉测量涉及两束光的整体相位差时，不能随意忽略它。

## 3. 复数模平方与Jones矢量归一化

复数的普通平方与模平方不同：

$$
i^2=-1,
\qquad
|i|^2=i^*i=(-i)i=1.
$$

Jones矢量的模平方使用共轭转置：

$$
\boxed{
\|\boldsymbol J\|^2
=\boldsymbol J^\dagger\boldsymbol J
=|J_x|^2+|J_y|^2
}.
$$

例如：

$$
\boldsymbol J=
\frac1{\sqrt2}
\begin{bmatrix}
1\\
i
\end{bmatrix},
$$

其共轭转置为

$$
\boldsymbol J^\dagger
=\frac1{\sqrt2}
\begin{bmatrix}
1&-i
\end{bmatrix}.
$$

所以

$$
\boldsymbol J^\dagger\boldsymbol J
=\frac12[1+(-i)i]
=\frac12(1+1)=1.
$$

不能使用 $1^2+i^2$ 计算光强，因为复数相位不应改变该分量携带的能量。

## 4. 常见偏振态的Jones矢量

### 4.1 任意方向的线偏振

线偏振方向与 $x$ 轴夹角为 $\alpha$ 时，电场沿该方向振动：

$$
\boxed{
\boldsymbol J_\alpha=
\begin{bmatrix}
\cos\alpha\\
\sin\alpha
\end{bmatrix}
}.
$$

常见情况为：

$$
\boldsymbol J_H=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\boldsymbol J_V=
\begin{bmatrix}0\\1\end{bmatrix},
$$

$$
\boldsymbol J_{45}=
\frac1{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\boldsymbol J_{-45}=
\frac1{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}.
$$

$1/\sqrt2$ 用于使两个分量的模平方和等于1。

### 4.2 两种相反旋向的圆偏振

当两个正交分量振幅相等、相位相差 $\pm\pi/2$ 时：

$$
\boxed{
\boldsymbol J_{C+}=
\frac1{\sqrt2}
\begin{bmatrix}1\\i\end{bmatrix},
\qquad
\boldsymbol J_{C-}=
\frac1{\sqrt2}
\begin{bmatrix}1\\-i\end{bmatrix}
}.
$$

其中 $i=e^{i\pi/2}$、$-i=e^{-i\pi/2}$，用于记录两个分量之间的相对相位。左旋和右旋的名称还取决于观察方向和时间因子约定，本课只区分两种相反旋向。

## 5. 为什么称为圆偏振

取

$$
\boldsymbol J=
\frac1{\sqrt2}
\begin{bmatrix}1\\i\end{bmatrix}
$$

并采用 $e^{i\omega t}$ 时间约定，真实电场为

$$
E_x(t)=\frac1{\sqrt2}\cos\omega t,
$$

$$
E_y(t)=-\frac1{\sqrt2}\sin\omega t.
$$

因此

$$
E_x^2+E_y^2
=\frac12\cos^2\omega t
+\frac12\sin^2\omega t
=\frac12.
$$

电场端点到原点的距离恒定，而方向随时间旋转，所以在固定空间位置观察，电场矢量端点的轨迹是圆。

“圆偏振”描述的是固定位置处电场端点随时间的轨迹，不是光沿圆形路径传播。

## 6. 线偏振片是矢量投影

设线偏振片的透振方向为

$$
\boxed{
\boldsymbol p(\theta)=
\begin{bmatrix}
\cos\theta\\
\sin\theta
\end{bmatrix}
}.
$$

入射Jones矢量为

$$
\boldsymbol J=
\begin{bmatrix}
E_x\\
E_y
\end{bmatrix}.
$$

入射电场在透振方向上的复投影振幅为

$$
\boxed{
a=\boldsymbol p^\dagger\boldsymbol J
}.
$$

这里使用共轭转置是因为Jones矢量可以包含复数。对线偏振方向矢量，$\boldsymbol p$ 为实数，所以

$$
\boldsymbol p^\dagger=\boldsymbol p^{\mathrm T}.
$$

展开后：

$$
a=E_x\cos\theta+E_y\sin\theta.
$$

$a$ 是标量，只给出投影的复振幅。出射电场还必须具有透振轴方向，因此

$$
\boxed{
\boldsymbol J_{\mathrm{out}}
=a\boldsymbol p
=\boldsymbol p
(\boldsymbol p^\dagger\boldsymbol J)
}.
$$

所以线偏振片的Jones矩阵为

$$
\boxed{
\boldsymbol P(\theta)
=\boldsymbol p\boldsymbol p^\dagger
=
\begin{bmatrix}
\cos^2\theta&\cos\theta\sin\theta\\
\cos\theta\sin\theta&\sin^2\theta
\end{bmatrix}
}.
$$

## 7. 水平线偏振通过 $60^\circ$ 偏振片

入射光为

$$
\boldsymbol J_{\mathrm{in}}=
\begin{bmatrix}1\\0\end{bmatrix},
$$

透振轴为

$$
\boldsymbol p=
\begin{bmatrix}
\cos60^\circ\\
\sin60^\circ
\end{bmatrix}
=
\begin{bmatrix}
1/2\\
\sqrt3/2
\end{bmatrix}.
$$

投影复振幅：

$$
a=\boldsymbol p^\dagger\boldsymbol J_{\mathrm{in}}=\frac12.
$$

出射Jones矢量：

$$
\boldsymbol J_{\mathrm{out}}
=a\boldsymbol p
=
\begin{bmatrix}
1/4\\
\sqrt3/4
\end{bmatrix}.
$$

出射光强比例：

$$
\frac{I_{\mathrm{out}}}{I_{\mathrm{in}}}
=\boldsymbol J_{\mathrm{out}}^\dagger
\boldsymbol J_{\mathrm{out}}
=\frac1{16}+\frac3{16}
=\frac14.
$$

## 8. 马吕斯定律

入射线偏振方向为 $\alpha$，偏振片方向为 $\theta$：

$$
\boldsymbol J_{\mathrm{in}}=
\begin{bmatrix}
\cos\alpha\\
\sin\alpha
\end{bmatrix}.
$$

投影振幅为

$$
a=\cos\theta\cos\alpha+
\sin\theta\sin\alpha
=\cos(\theta-\alpha).
$$

因为光强与复振幅模平方成正比：

$$
\boxed{
I_{\mathrm{out}}
=I_{\mathrm{in}}\cos^2(\theta-\alpha)
}.
$$

振幅获得一次余弦，光强计算模平方后变成余弦平方。

## 9. 圆偏振通过线偏振片

对

$$
\boldsymbol J=
\frac1{\sqrt2}
\begin{bmatrix}1\\i\end{bmatrix},
$$

投影复振幅为

$$
a=
\frac1{\sqrt2}
(\cos\theta+i\sin\theta)
=\frac1{\sqrt2}e^{i\theta}.
$$

所以

$$
|a|^2=\frac12.
$$

圆偏振通过任意方向的理想线偏振片时，透射光强均为入射光强的一半；改变偏振片方向会改变投影复振幅的相位。

## 10. 波片与偏振片的区别

偏振片选择电场在某一方向上的投影，会去除与透振轴正交的分量。

波片保留两个正交分量，但在它们之间引入相位延迟。若快轴沿 $x$、慢轴沿 $y$，理想波片可写为

$$
\boldsymbol W(\delta)=
\begin{bmatrix}
1&0\\
0&e^{i\delta}
\end{bmatrix}.
$$

四分之一波片对应

$$
\boldsymbol Q=
\begin{bmatrix}
1&0\\
0&i
\end{bmatrix},
$$

半波片对应

$$
\boldsymbol H=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}.
$$

基本区别是：

$$
\boxed{
\text{偏振片负责投影，波片负责相对相位延迟}
}.
$$

## 11. 正交偏振光与检偏器

两束正交偏振光直接探测时，其偏振内积为零，没有共同方向的干涉项。检偏器可以把两束光投影到同一个线偏振方向，使两个投影分量发生干涉。

这不是重新产生相干性，而是让原本正交的电场获得共同的探测方向。

## 12. 同步偏振四步相移的理想模型

设物光和参考光为两种相反旋向的圆偏振：

$$
\boldsymbol E_o
=\frac{A_oe^{i\varphi_o}}{\sqrt2}
\begin{bmatrix}1\\i\end{bmatrix},
$$

$$
\boldsymbol E_r
=\frac{A_re^{i\varphi_r}}{\sqrt2}
\begin{bmatrix}1\\-i\end{bmatrix}.
$$

待测相位为

$$
\phi=\varphi_o-\varphi_r.
$$

经过方向为 $\theta$ 的线偏振分析器后，物光投影复振幅为

$$
a_o
=\boldsymbol p^\dagger\boldsymbol E_o
=\frac{A_oe^{i\varphi_o}}{\sqrt2}
(\cos\theta+i\sin\theta)
=\frac{A_o}{\sqrt2}e^{i(\varphi_o+\theta)}.
$$

参考光投影复振幅为

$$
a_r
=\boldsymbol p^\dagger\boldsymbol E_r
=\frac{A_r}{\sqrt2}e^{i(\varphi_r-\theta)}.
$$

两束投影光的相位差为

$$
(\varphi_o+\theta)-(\varphi_r-\theta)
=\phi+2\theta.
$$

所以干涉光强可以写成

$$
\boxed{
I_\theta=A+B\cos(\phi+2\theta)
}.
$$

相移为检偏角的两倍，不是一般规律，而是由这两束相反旋向圆偏振光分别获得 $+\theta$ 和 $-\theta$ 投影相位推导出的结果。

选择

$$
\theta=0^\circ,45^\circ,90^\circ,135^\circ
$$

分别得到

$$
2\theta=0,\frac\pi2,\pi,\frac{3\pi}{2}.
$$

因此可形成四步相移干涉图，并使用

$$
\boxed{
\phi=
\mathrm{atan2}(I_{135}-I_{45},I_0-I_{90})
}
$$

恢复包裹相位。具体正负号仍取决于系统的旋向和相位约定。

## 13. 偏振相机的同步采集与误差

偏振相机的典型 $2\times2$ 微偏振单元包含 $0^\circ、45^\circ、90^\circ、135^\circ$ 四个方向，一次曝光即可同时采集四类数据，减小顺序采集的帧间运动误差。

但四个方向位于不同物理像素，并不是在完全相同位置测量同一物点，因此需要插值或配准。主要误差包括：

- 四方向空间采样位置不同；
- 微偏振片透过率和实际角度不同；
- 像素响应、暗电流和增益不同；
- 消光比有限；
- 插值与配准误差；
- 波片延迟偏离理想值；
- 条纹变化过快导致邻近像素差异明显。

实际通道可以表示为

$$
I_k=A_k+B_k\cos(\phi+\delta_k+\varepsilon_k)+n_k,
$$

其中 $A_k、B_k、\varepsilon_k、n_k$ 分别描述通道背景、调制度、相移误差和噪声。

## 14. 本课结论

1. Jones矢量由两个正交电场分量的复振幅组成。
2. Jones矢量的光强和归一化必须使用共轭转置与模平方。
3. 线偏振片的作用是把电场投影到透振方向，矩阵为 $\boldsymbol p\boldsymbol p^\dagger$。
4. 投影首先得到复振幅，再乘透振方向得到出射Jones矢量。
5. 圆偏振的两个正交分量等振幅且相差 $\pm\pi/2$，电场端点轨迹为圆。
6. 偏振片负责方向投影，波片负责相对相位延迟。
7. 相反旋向圆偏振经过线偏振分析后，可由四个检偏方向产生四步相移。
8. 偏振相机实现同时采集，但空间复用会引入插值、配准和通道不一致误差。
