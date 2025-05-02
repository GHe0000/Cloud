---
title: 从 Hamilton 原理及对称性导出低速弱场下 Lagrange 量
toc: true
categories:
  - 物理
tags:
  - 理论力学
---

本文给出从 Hamilton 原理及对称性导出低速弱场下 Lagrange 量的方法.

<!-- more -->

一般而言，我们介绍分析力学是从我们所熟悉的 Newton 定律通过虚功原理和 d'Alembert 原理从而得到 Eular-Lagrange 方程以及对应的 Lagrange 量.
在此我们通过另外一种方法，将 Hamilton 原理作为某种"公理"，从最简单最基础的角度进行分析和推导，经过低速近似和弱场近似，得到相同的
Lagrange 量. 此方法相比原本的方法更为现代，同时也体现了对称性在现代物理学研究范式中的重要地位.


（注：本文中均使用 Einstein 求和约定）

# Hamilton 原理

如果一个力学体系可以完全由一系列变量 $q_{1},q_{2},\cdots,q_{i}$
来描述，则称这一组变量为该力学体系的广义坐标.一个力学体系的所有广义坐标
$q_{i}$
构成一个"空间"，称为该力学体系的**位形空间**.需要注意，力学体系的位形空间一般不是一个平直的空间，而且其拓扑结构往往也不是平庸的.一个力学体系的所有广义速度
$\dot{q}_{i}$
也构成一个"空间".对于位形空间中的一点，其所有的广义速度构成的"空间"称为位形空间（流形）的**切丛**[^1].

在整个经典力学乃至整个物理学中，有如下极其重要的定理[^2]

$\mathbf{Theorem} 1:$ (Hamilton 原理).
任意力学体系中都存在一个与运动相关的量，称为**最小作用量**，记作
$S$，其为一个 Lorentz 标量.如果一个力学体系在 $t_{1}$ 和 $t_{2}$
时刻分别由广义坐标 $q_{i}^{(1)}$，$q_{i}^{(2)}$ 描写，则作用量 $S$
可以描述为在这两个位形中各种可能轨道的泛函.

$$S=\int_{t_{1}}^{t_{2}}\mathrm{d}t\,\mathcal{L}(q_{i},\dot{q}_{i},t)$$

这里的被积函数 $\mathcal{L}$ 被称为 Lagrange 量.该力学体系从 $t_{1}$ 到
$t_{2}$ 的实际轨迹满足作用量 $S$ 取极值.[^3]

要得到一个特定力学体系的作用量，最常用的方法是从体系的对称性出发，从而构建出相应的
Lorentz 标量. 从最小作用量出发，要求解出力学体系的运动方程，则可以通过变分法得到.

$\mathbf{Theorem} 2:$ (Euler-Lagrange 方程).
对于一个泛函

$$S=\int_{t_{1}}^{t_{2}}\mathrm{d}t\,\mathcal{L}(q_{i},\dot{q}_{i},t)$$

若使得上述泛函能取到极值，则其一阶变分为 $0$，其内部的 $\mathcal{L}$
满足：

$$\frac{\partial\mathcal{L}}{\partial\dot{q}_{i}}-\frac{\partial\mathcal{L}}{\partial q_{i}}=0$$

此即 Euler-lagrange 方程.

一旦给定了一个力学体系的 Lagrange 量（作用量），根据 Hamilton
原理和变分法可知，体系的运动方程由 E-L 方程决定.
因此，经典力学体系的性质完全由 Lagrange
量（作用量）决定，其包含了体系所有的力学信息.

我们定义该力学体系中与某个广义坐标 $q_{i}$ 共轭的**广义动量**[^4] $p_{i}$:

$$p_{i}=\frac{\partial\mathcal{L}}{\partial\dot{q}_{i}}$$

因此，前文的 E-L 方程又可以写为:

$$\frac{\mathrm{d}p_{i}}{\mathrm{d}t}=\frac{\partial\mathcal{L}}{\partial q_{i}}$$

由于与牛顿力学中的方程类似，方程的右边又被称为**广义力**.

# 相对论下自由粒子的运动方程

由于作用量是一个 Lorentz 标量，在相对论中我们所能想到的最简单的 Lorentz
标量就是世界线长度，因此，对于一个相对论下的自由粒子，其作用量可以写成如下形式

$$S=\alpha\int\mathrm{d}s$$

其中 $\mathrm{d}s=\sqrt{\mathrm{d}x^{\mu}\mathrm{d}x_{\mu}}$
为世界线线元，$\alpha$ 则是一个常量.为了兼容传统的牛顿力学，可以得到[^5]
$\alpha=-mc$，因此有

$$S=-mc\int\mathrm{d}s$$ 

对上式做变分，有

$$\begin{aligned}
\delta S & =-mc\int\delta(\mathrm{d}s)=-mc\int\mathrm{d}\tau\,\delta\left(\sqrt{\frac{\mathrm{d}x^{\mu}}{\mathrm{d}\tau}\frac{\mathrm{d}x_{\mu}}{\mathrm{d}\tau}}\right)\\
 & =-mc\int\mathrm{d}\tau\,\delta\left(\sqrt{u_{\mu}u^{\mu}}\right)\quad\left(u_{\mu}=\frac{\mathrm{d}x_{\mu}}{\mathrm{d}\tau},\ u^{\mu}=\frac{\mathrm{d}u^{\mu}}{\mathrm{d}\tau}\right)\\
 & =-mc\int\mathrm{d}\tau\frac{u_{\mu}\delta u^{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\\
 & =-mc\int\mathrm{d}\tau\left[\frac{u_{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\frac{\mathrm{d}}{\mathrm{d}\tau}(\delta x^{\mu})\right]\\
 & =mc\int\mathrm{d}\tau\,\delta x^{\mu}\frac{\mathrm{d}}{\mathrm{d}\tau}\left(\frac{u_{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\right)-mc\left[\delta x^{\mu}\frac{u_{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\right]_{\text{start}}^{\text{finish}}
\end{aligned}$$

上式由于为固定起点到终点的变分，因此第二项恒为
$0$. 因此可以得到自由粒子的运动方程为

$$\frac{\mathrm{d}^{2}x_{\mu}}{\mathrm{d}\tau^{2}}=0 \quad \left(\sqrt{u_{\mu}u^{\mu}}=c\right)$$

也就是匀速直线运动.

# 相对论下与标量场相互作用粒子的运动方程

如果一个外场本身是一个无量纲的 Lorentz
标量（也就是标量场[^6]），一个相对论性粒子与其相互作用的作用量可以写成[^7]

$$S=-mc\int\mathrm{d}s\,e^{\Phi(x)}$$

同样，对上式做变分

$$\begin{aligned}
\delta S & =-mc\int\mathrm{d}\tau\,\delta\left(e^{\Phi}\sqrt{u_{\mu}u^{\mu}}\right)\\
 & =-mc\int\mathrm{d}\tau\left[\sqrt{u_{\mu}u^{\mu}}e^{\Phi}\delta\Phi+\frac{e^{\Phi}u_{\mu}\delta u^{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\right]\\
 & =-mc\int\mathrm{d}\tau\left[\sqrt{u_{\mu}u^{\mu}}e^{\Phi}\frac{\partial\Phi}{\partial x^{\mu}}\delta x^{\mu}+\frac{e^{\Phi}u_{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\frac{\mathrm{d}}{\mathrm{d}\tau}(\delta x^{\mu})\right]
\end{aligned}$$

对第二项使用分部积分并同样由于为固定起点和终点的变分，因此丢掉边界项，得到

$$\int\mathrm{d}\tau\frac{e^{\Phi}u_{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\frac{\mathrm{d}}{\mathrm{d}\tau}(\delta x^{\mu})=-\int\delta x^{\mu}\mathrm{d}\tau\frac{\mathrm{d}}{\mathrm{d}\tau}\left(\frac{e^{\Phi}u_{\mu}}{\sqrt{u_{\mu}u^{\mu}}}\right)$$

带入回原式，由变分学基本引理，可得

$$c^{2}e^{\Phi}\frac{\partial\Phi}{\partial x^{\mu}}=\frac{\mathrm{d}}{\mathrm{d}\tau}(e^{\Phi}u_{\mu})=e^{\Phi}\left(\frac{\mathrm{d}^{2}x_{\mu}}{\mathrm{d}\tau^{2}}+\frac{\mathrm{d}x_{\mu}}{\mathrm{d}\tau}\frac{\partial\Phi}{\partial x^{\nu}}\frac{\mathrm{d}x_{\nu}}{\mathrm{d}\tau}\right)$$

进一步化简，注意到 $\mathrm{d}s=c\mathrm{d}\tau$，可得

$$\frac{\mathrm{d}^{2}x_{\mu}}{\mathrm{d}s^{2}}+\frac{\mathrm{d}x_{\mu}}{\mathrm{d}s}\frac{\partial\Phi}{\partial x^{\nu}}\frac{\mathrm{d}x_{\nu}}{\mathrm{d}s}=\frac{\partial\Phi(x)}{\partial x^{\mu}}$$

此即为相对论性粒子与标量场相互作用下的运动方程.

# 非相对论极限与弱场近似

对于一个在标量场中的粒子，其作用量为：

$$S=-mc\int\mathrm{d}s\,e^{\Phi(x)}=-mc^{2}\int\mathrm{d}t\,\sqrt{1-\frac{\boldsymbol{v}^{2}}{c^{2}}}\,e^{\Phi(\boldsymbol{x},t)}$$

因此其 Lagrange 量为：

$$\mathcal{L}=-mc^{2}\sqrt{1-\frac{\boldsymbol{v}^{2}}{c^{2}}}\,e^{\Phi(\boldsymbol{x},t)}$$

若粒子速度 $v\ll c$ 且标量场 $\Phi(\boldsymbol{x},t)=\frac{V(\boldsymbol{x},t)}{mc^{2}}$ 同时 $V(\boldsymbol{x},t)\ll mc^{2}$，分别对
$\sqrt{1-\frac{\boldsymbol{v}^{2}}{c^{2}}}$ 和
$e^{\Phi(\boldsymbol{x},t)}$ 展开，有： 

$$\begin{aligned}
\sqrt{1-\frac{\boldsymbol{v}^{2}}{c^{2}}} & \approx1-\frac{1}{2}\frac{v^{2}}{c^{2}},\\
e^{\Phi(\boldsymbol{x},t)} & \approx1+\frac{V}{mc^{2}}
\end{aligned}$$ 

因此： 

$$\begin{aligned}
\mathcal{L} & \approx-mc^{2}\left(1-\frac{1}{2}\frac{v^{2}}{c^{2}}\right)\left(1+\frac{V}{mc^{2}}\right)\\
 & =-mc^{2}\left(1-\frac{1}{2}\frac{v^{2}}{c^{2}}+\frac{V}{mc^{2}}-\frac{1}{2}\frac{v^{2}}{c^{2}}\frac{V}{mc^{2}}\right)\\
 & =-mc^{2}\left(1-\frac{1}{2}\frac{v^{2}}{c^{2}}+\frac{V}{mc^{2}}\right)\quad\text{（略去高阶小量）}\\
 & =\frac{1}{2}mv^{2}-V-mc^{2}
\end{aligned}$$

上式中的 $mc^{2}$ 为常量，可略去.
因此在非相对论极限和弱场近似下的 Lagrange 量为：

$$\mathcal{L}=T-V,\quad T=\frac{1}{2}mv^{2}$$

这与从 Newton 定律通过虚功原理和 d'Alembert 原理得到的 Lagrange 量是一致的.

[^1]: 这里与微分几何有很大关联，更详细的内容需要查阅微分几何有关书籍

[^2]: "Hamilton 原理"也被称为"最小作用量原理"

[^3]: 由于自由粒子的质量为正值，故一般而言作用量 $S$ 取的是最小值.

[^4]: 又称为正则动量

[^5]: 此处可以参考 Landau 的场论第二章.

[^6]: 比如高能物理中的 Higgs 场

[^7]: 这么写是为了在非相对论极限下退化成经典的势能. 

