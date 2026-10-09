# 从光力类比、波阵面与最小作用量原理推导哈密顿–雅可比方程

## 1. 核心思想

哈密顿–雅可比理论可以从几何光学的类比来理解.

几何光学中，一个波可以用两种互补的方式描述：

- 用**光线**描述传播轨迹
- 用**波阵面**描述相位相同的面

光线总是沿着波阵面的法线方向传播.

经典力学也存在类似的结构：

- 粒子的经典轨迹类似于光线
- 作用量函数的等值面类似于波阵面

如果定义 Hamilton 主函数

$$
S(\mathbf q,t)
$$

那么

$$
S(\mathbf q,t)=\mathrm{const}
$$

可以看成力学中的“波阵面”.

不同的经典轨迹穿过这些等作用量面，而作用量函数 \(S\) 的梯度给出共轭动量：

$$
\mathbf p=\nabla_{\mathbf q}S
$$

同时

$$
\frac{\partial S}{\partial t}=-H
$$

因此 \(S\) 满足

$$
\frac{\partial S}{\partial t}
+
H\left(
\mathbf q,
\frac{\partial S}{\partial \mathbf q},
t
\right)
=0
$$

这就是哈密顿–雅可比方程.

下面从光学类比和作用量原理一步一步说明这一结构是怎样出现的.

---

# 2. 几何光学中的光线与波阵面

考虑一个短波长极限下的波，可以写成

$$
\psi(\mathbf r,t)
=
A(\mathbf r,t)
e^{i\Phi(\mathbf r,t)}
$$

其中 \(\Phi\) 是相位.

在某一固定时刻，相位相同的点构成一个曲面：

$$
\Phi(\mathbf r,t)=\mathrm{const}
$$

这就是波阵面.

由于梯度总是垂直于函数的等值面，因此

$$
\nabla\Phi
$$

垂直于波阵面.

定义波矢

$$
\mathbf k=\nabla\Phi
$$

于是波矢方向就是波传播方向.

因此几何光学中有

$$
\text{波阵面}
\quad\longleftrightarrow\quad
\Phi=\mathrm{const}
$$

以及

$$
\text{光线方向}
\quad\longleftrightarrow\quad
\nabla\Phi
$$

也就是说，光线可以看成一族等相位面的正交轨线.

---

# 3. Fermat 原理与程函方程

在折射率为 \(n(\mathbf r)\) 的介质中，光线满足 Fermat 原理：

$$
\delta\int_A^B n(\mathbf r)\,ds=0
$$

严格地说，这里要求的是光程取**驻值**，并不一定总是最小值.

定义光程函数

$$
W(\mathbf r)
=
\int_A^{\mathbf r}n(\mathbf r')\,ds
$$

那么

$$
W(\mathbf r)=\mathrm{const}
$$

就是一族等光程面，也就是几何光学中的波阵面.

因为沿着光线方向增加一个距离 \(ds\) 时，

$$
dW=n\,ds
$$

而

$$
dW=\nabla W\cdot d\mathbf r
$$

光线又垂直于 \(W=\mathrm{const}\) 的曲面，所以沿光线方向有

$$
\nabla W\parallel d\mathbf r
$$

从而得到

$$
|\nabla W|=n
$$

也就是几何光学的程函方程

$$
(\nabla W)^2=n^2
$$

这个方程已经具有哈密顿–雅可比方程的形式.

它告诉我们：

> 不必逐条追踪所有光线，只要先求出一个标量函数 \(W(\mathbf r)\)，光线方向就可以由 \(\nabla W\) 恢复出来.

哈密顿–雅可比理论对经典力学所做的事情完全类似.

---

# 4. 光力类比

考虑一个经典粒子，其 Hamiltonian 为

$$
H(\mathbf q,\mathbf p)
=
\frac{\mathbf p^2}{2m}
+
V(\mathbf q)
$$

如果能量固定为 \(E\)，则

$$
\frac{\mathbf p^2}{2m}+V(\mathbf q)=E
$$

所以

$$
|\mathbf p|
=
\sqrt{2m[E-V(\mathbf q)]}
$$

另一方面，几何光学中有

$$
|\nabla W|=n(\mathbf r)
$$

如果在力学中取

$$
\mathbf p=\nabla W
$$

就得到

$$
|\nabla W|
=
\sqrt{2m[E-V(\mathbf q)]}
$$

即

$$
\frac{(\nabla W)^2}{2m}+V(\mathbf q)=E
$$

这就是定能量情况下的哈密顿–雅可比方程.

因此可以作如下类比：

| 几何光学 | 经典力学 |
|---|---|
| 光线 | 经典轨迹 |
| 波阵面 | 等作用量面 |
| 光学程函数 \(W_{\rm opt}\) | 约化作用量 \(W\) |
| 折射率 \(n\) | 动量大小 \(p\) |
| \(\nabla W_{\rm opt}\) | \(\nabla W=\mathbf p\) |
| Fermat 原理 | Maupertuis 原理 |
| 程函方程 | 定态 Hamilton–Jacobi 方程 |

对于自然 Hamiltonian

$$
H=\frac{\mathbf p^2}{2m}+V
$$

可以形式上定义一个“力学折射率”

$$
n_{\mathrm{eff}}(\mathbf q)
\propto
\sqrt{2m[E-V(\mathbf q)]}
$$

势能越低，允许的动量越大，对应的“力学折射率”也越大.

---

# 5. 从作用量定义 Hamilton 主函数

现在考虑一般的 Lagrangian

$$
L(\mathbf q,\dot{\mathbf q},t)
$$

经典轨迹满足作用量驻值原理

$$
\delta I=0
$$

其中

$$
I[\mathbf q]
=
\int_{t_0}^{t}L(\mathbf q,\dot{\mathbf q},t')\,dt'
$$

固定初始点

$$
(\mathbf q_0,t_0)
$$

对于任意终点

$$
(\mathbf q,t)
$$

取连接初始点与终点的那条经典轨迹，并沿这条经典轨迹计算作用量.

定义

$$
S(\mathbf q,t)
=
\int_{t_0}^{t}
L(\mathbf q_{\mathrm{cl}},\dot{\mathbf q}_{\mathrm{cl}},t')
\,dt'
$$

这里的 \(S\) 称为 Hamilton 主函数.

需要注意：

$$
S
$$

已经不是“任意轨迹的泛函”，而是在经典轨迹上取值之后得到的一个普通函数.

也就是说

$$
I[\mathbf q(t)]
$$

是一个泛函，而

$$
S(\mathbf q,t)
$$

是终点坐标与终止时刻的函数.

---

# 6. 为什么 \(S=\mathrm{const}\) 可以看成力学波阵面

对于固定的初始事件 \((\mathbf q_0,t_0)\)，考虑所有可能的经典轨迹.

经过某一作用量值 \(S_0\) 的终点组成曲面

$$
S(\mathbf q,t)=S_0
$$

这就是作用量的等值面.

在固定时刻 \(t\) 下，它在构型空间中形成

$$
S(\mathbf q,t)=\mathrm{const}
$$

的一族曲面.

这与光学中的

$$
\Phi(\mathbf r,t)=\mathrm{const}
$$

或

$$
W_{\rm opt}(\mathbf r)=\mathrm{const}
$$

具有相同的几何结构.

因此可以把

$$
S(\mathbf q,t)=\mathrm{const}
$$

称为力学中的“波阵面”.

如果能够证明

$$
\mathbf p=\nabla_{\mathbf q}S
$$

那么动量方向就由作用量面的法线决定.

这正对应于几何光学中的

$$
\mathbf k=\nabla\Phi
$$

于是有

$$
\text{光线垂直于波阵面}
$$

对应

$$
\text{经典运动由等作用量面的法向信息决定}
$$

对于

$$
H=\frac{\mathbf p^2}{2m}+V
$$

还有

$$
\dot{\mathbf q}
=
\frac{\mathbf p}{m}
=
\frac{1}{m}\nabla S
$$

所以此时经典轨迹确实沿着等作用量面的法线方向前进.

更一般地，如果 Hamiltonian 不是简单的二次动能形式，则

$$
\dot q_i=\frac{\partial H}{\partial p_i}
$$

而

$$
p_i=\frac{\partial S}{\partial q_i}
$$

仍然成立，但速度不一定与 \(\nabla S\) 平行.

---

# 7. 作用量的端点变分

哈密顿–雅可比方程最关键的一步，是考察经典作用量随终点变化如何变化.

定义

$$
S(\mathbf q,t)
=
\int_{t_0}^{t}L\,dt'
$$

现在把终点从

$$
(\mathbf q,t)
$$

改变为

$$
(\mathbf q+d\mathbf q,t+dt)
$$

需要求

$$
dS
$$

对于作用量的一般变分，

$$
\delta I
=
\int_{t_0}^{t}
\left(
\frac{\partial L}{\partial q_i}
-
\frac{d}{dt}
\frac{\partial L}{\partial \dot q_i}
\right)
\delta q_i\,dt
+
\left[
\frac{\partial L}{\partial\dot q_i}
\delta q_i
\right]_{t_0}^{t}
$$

对于经典轨迹，Euler–Lagrange 方程成立：

$$
\frac{d}{dt}
\frac{\partial L}{\partial\dot q_i}
-
\frac{\partial L}{\partial q_i}
=0
$$

因此积分中的体项消失.

如果初始端点固定，则只剩终点项.

但是当终止时间本身也发生变化时，需要同时考虑时间端点的移动.

最终得到经典作用量的端点微分

$$
dS
=
\sum_i p_i\,dq_i
-
H\,dt
$$

其中

$$
p_i=\frac{\partial L}{\partial\dot q_i}
$$

以及

$$
H
=
\sum_i p_i\dot q_i-L
$$

这是推导 Hamilton–Jacobi 方程的核心公式.

---

# 8. 端点变分公式的直接推导

也可以更直观地推导

$$
dS=\mathbf p\cdot d\mathbf q-Hdt
$$

先假设终止时刻不变，只改变终点坐标.

沿经典轨迹，作用量的一阶变化只剩边界项：

$$
dS
=
\sum_i p_i\,dq_i
$$

因此

$$
\frac{\partial S}{\partial q_i}=p_i
$$

这已经说明了作用量梯度就是共轭动量.

然后只改变终止时间.

终点沿经典轨迹前进 \(dt\)，则

$$
dq_i=\dot q_i\,dt
$$

新增加的一小段作用量为

$$
L\,dt
$$

但从 \(S(\mathbf q,t)\) 作为终点函数的全微分来看，

$$
dS
=
\sum_i
\frac{\partial S}{\partial q_i}dq_i
+
\frac{\partial S}{\partial t}dt
$$

利用

$$
\frac{\partial S}{\partial q_i}=p_i
$$

以及

$$
dq_i=\dot q_i\,dt
$$

得到

$$
L\,dt
=
\sum_i p_i\dot q_i\,dt
+
\frac{\partial S}{\partial t}dt
$$

所以

$$
\frac{\partial S}{\partial t}
=
L-\sum_i p_i\dot q_i
$$

根据 Legendre 变换

$$
H
=
\sum_i p_i\dot q_i-L
$$

因此

$$
\frac{\partial S}{\partial t}=-H
$$

于是同时得到

$$
p_i=\frac{\partial S}{\partial q_i}
$$

和

$$
H=-\frac{\partial S}{\partial t}
$$

---

# 9. 哈密顿–雅可比方程

Hamiltonian 本来是

$$
H(\mathbf q,\mathbf p,t)
$$

而刚才已经得到

$$
p_i=\frac{\partial S}{\partial q_i}
$$

所以可以把所有动量替换为作用量的梯度：

$$
\mathbf p
=
\nabla_{\mathbf q}S
$$

同时

$$
H=-\frac{\partial S}{\partial t}
$$

因此

$$
H\left(
\mathbf q,
\frac{\partial S}{\partial\mathbf q},
t
\right)
=
-\frac{\partial S}{\partial t}
$$

整理得到

$$
\frac{\partial S}{\partial t}
+
H\left(
\mathbf q,
\frac{\partial S}{\partial\mathbf q},
t
\right)
=0
$$

这就是一般形式的 Hamilton–Jacobi 方程.

它把原来的 Hamilton 正则方程

$$
\dot q_i=\frac{\partial H}{\partial p_i}
$$

$$
\dot p_i=-\frac{\partial H}{\partial q_i}
$$

转换成一个关于标量函数 \(S(\mathbf q,t)\) 的一阶偏微分方程.

---

# 10. 单粒子情况下的形式

对于

$$
H
=
\frac{\mathbf p^2}{2m}
+
V(\mathbf q,t)
$$

代入

$$
\mathbf p=\nabla S
$$

得到

$$
\frac{\partial S}{\partial t}
+
\frac{(\nabla S)^2}{2m}
+
V(\mathbf q,t)
=0
$$

这就是最常见的 Hamilton–Jacobi 方程.

可以把它直接与几何光学的程函方程比较.

光学：

$$
(\nabla W_{\rm opt})^2=n^2
$$

经典力学：

$$
\frac{(\nabla S)^2}{2m}
+
V
+
\frac{\partial S}{\partial t}
=0
$$

二者都通过一个标量函数的梯度来编码轨线的方向信息.

---

# 11. 时间无关问题与约化作用量 \(W\)

如果 Hamiltonian 不显含时间，

$$
H(\mathbf q,\mathbf p)
$$

则能量守恒：

$$
H=E
$$

可以尝试分离变量

$$
S(\mathbf q,t)
=
W(\mathbf q)-Et
$$

其中 \(W(\mathbf q)\) 称为 Hamilton 特征函数或约化作用量.

代入 Hamilton–Jacobi 方程：

$$
-E
+
H\left(
\mathbf q,
\nabla W
\right)
=0
$$

因此

$$
H\left(
\mathbf q,
\nabla W
\right)
=E
$$

对于

$$
H=\frac{\mathbf p^2}{2m}+V(\mathbf q)
$$

得到

$$
\frac{(\nabla W)^2}{2m}+V(\mathbf q)=E
$$

即

$$
|\nabla W|
=
\sqrt{2m[E-V(\mathbf q)]}
$$

这和光学中的

$$
|\nabla W_{\rm opt}|=n
$$

几乎完全同构.

因此真正与几何光学“空间波阵面”最直接对应的，其实是定能量情况下的

$$
W(\mathbf q)=\mathrm{const}
$$

而完整的时空相位面则对应

$$
S(\mathbf q,t)=\mathrm{const}
$$

---

# 12. Maupertuis 原理与 Fermat 原理

定能量经典力学中，可以把通常的作用量原理改写为 Maupertuis 原理：

$$
\delta\int_A^B\mathbf p\cdot d\mathbf q=0
$$

定义约化作用量

$$
W
=
\int_A^B\mathbf p\cdot d\mathbf q
$$

对于自然力学系统

$$
\mathbf p
=
m\dot{\mathbf q}
$$

并且

$$
|\mathbf p|
=
\sqrt{2m(E-V)}
$$

所以

$$
W
=
\int_A^B
\sqrt{2m(E-V)}
\,ds
$$

与 Fermat 原理

$$
\delta\int_A^B n(\mathbf r)\,ds=0
$$

完全相似.

因此有

$$
n(\mathbf r)
\quad\longleftrightarrow\quad
\sqrt{2m[E-V(\mathbf q)]}
$$

从这个角度看，经典粒子在势场中的运动可以类比为光线在空间变化的折射率介质中传播.

势能 \(V(\mathbf q)\) 改变了粒子的局域动量，从而类似于折射率改变了局域波矢.

---

# 13. 为什么作用量的等值面能决定轨迹

假设已经求出了

$$
S(\mathbf q,t)
$$

那么在任意位置都知道

$$
p_i
=
\frac{\partial S}{\partial q_i}
$$

也就是说，\(S\) 的梯度场给出了整个构型空间中的动量场.

再利用 Hamilton 方程

$$
\dot q_i
=
\frac{\partial H}{\partial p_i}
$$

代入

$$
p_i=\frac{\partial S}{\partial q_i}
$$

得到

$$
\dot q_i
=
\left.
\frac{\partial H}{\partial p_i}
\right|_{\mathbf p=\nabla S}
$$

于是可以从 \(S\) 重建经典轨迹.

对于简单的单粒子 Hamiltonian

$$
H=\frac{\mathbf p^2}{2m}+V
$$

有

$$
\dot{\mathbf q}
=
\frac{\nabla S}{m}
$$

因此轨迹方向就是等 \(S\) 面的法向方向.

所以 Hamilton–Jacobi 理论所做的事情是：

> 从“逐条求粒子轨迹”转变为“先求一族作用量波阵面，再由这些波阵面的法线恢复轨迹”.

这就是它与几何光学之间最核心的类比.

---

# 14. 从最小作用量到 Hamilton–Jacobi 方程的逻辑链

整个推导可以压缩为下面的逻辑.

首先，经典轨迹使作用量驻值：

$$
\delta
\int_{t_0}^{t}
L\,dt
=0
$$

因此固定初始点后，可以把经典作用量定义成终点函数：

$$
S(\mathbf q,t)
=
\int_{\mathrm{cl}}L\,dt
$$

对终点作微小变化，有

$$
dS
=
\mathbf p\cdot d\mathbf q
-
Hdt
$$

另一方面，作为普通函数 \(S(\mathbf q,t)\)，其全微分是

$$
dS
=
\nabla_{\mathbf q}S\cdot d\mathbf q
+
\frac{\partial S}{\partial t}dt
$$

逐项比较得到

$$
\mathbf p
=
\nabla_{\mathbf q}S
$$

以及

$$
\frac{\partial S}{\partial t}
=
-H
$$

将

$$
\mathbf p=\nabla S
$$

代入 Hamiltonian：

$$
H
=
H(\mathbf q,\nabla S,t)
$$

于是

$$
\frac{\partial S}{\partial t}
+
H(\mathbf q,\nabla S,t)
=0
$$

即 Hamilton–Jacobi 方程.

---

# 15. 光学类比下的统一图像

可以把两套理论写成完全平行的结构.

## 几何光学

存在一个相位或程函

$$
W_{\rm opt}(\mathbf r)
$$

其等值面

$$
W_{\rm opt}=\mathrm{const}
$$

是波阵面.

波矢为

$$
\mathbf k=\nabla W_{\rm opt}
$$

光线沿着由 \(\mathbf k\) 决定的方向传播.

程函满足

$$
|\nabla W_{\rm opt}|=n
$$

---

## 经典力学

存在一个作用量函数

$$
S(\mathbf q,t)
$$

其等值面

$$
S=\mathrm{const}
$$

可以类比为力学波阵面.

动量为

$$
\mathbf p=\nabla_{\mathbf q}S
$$

经典轨迹由这个动量场决定.

作用量满足

$$
\frac{\partial S}{\partial t}
+
H(\mathbf q,\nabla S,t)
=0
$$

在定能量情况下

$$
S=W-Et
$$

于是

$$
H(\mathbf q,\nabla W)=E
$$

对于

$$
H=\frac{\mathbf p^2}{2m}+V
$$

进一步得到

$$
|\nabla W|
=
\sqrt{2m(E-V)}
$$

与光学程函方程直接对应.

---

# 16. 一个更深的观点：Hamilton–Jacobi 方程描述的是“作用量波”的传播

普通的 Newton 或 Hamilton 力学关注的是单条轨迹：

$$
\mathbf q(t),\mathbf p(t)
$$

Hamilton–Jacobi 理论则把视角提升到整个构型空间，研究一个标量场：

$$
S(\mathbf q,t)
$$

在每一个时刻，方程

$$
S(\mathbf q,t)=C
$$

给出一族等作用量面.

随着时间变化，这些曲面不断向前传播.

因此 Hamilton–Jacobi 方程也可以理解为：

> 描述“等作用量波阵面”如何在构型空间中传播的方程.

单条经典轨迹则是从这个波阵面族中重新提取出来的特征曲线.

从偏微分方程的角度说，Hamilton 方程正是 Hamilton–Jacobi 方程的特征线方程.

所以

$$
\text{Hamilton–Jacobi PDE 的特征线}
=
\text{Hamilton 经典轨迹}
$$

这正对应于几何光学中

$$
\text{程函方程的特征线}
=
\text{光线}
$$

---

# 17. 与量子力学的进一步联系

这种光力类比并不仅仅是形式上的巧合.

量子力学中令

$$
\psi
=
A e^{iS/\hbar}
$$

代入 Schrödinger 方程

$$
i\hbar\frac{\partial\psi}{\partial t}
=
\left[
-\frac{\hbar^2}{2m}\nabla^2+V
\right]\psi
$$

分离实部后可以得到

$$
\frac{\partial S}{\partial t}
+
\frac{(\nabla S)^2}{2m}
+
V
-
\frac{\hbar^2}{2m}
\frac{\nabla^2A}{A}
=0
$$

最后一项

$$
-\frac{\hbar^2}{2m}
\frac{\nabla^2A}{A}
$$

是量子修正项.

在短波长或半经典极限

$$
\hbar\to0
$$

下，这一项可以忽略，于是恢复

$$
\frac{\partial S}{\partial t}
+
\frac{(\nabla S)^2}{2m}
+
V
=0
$$

也就是经典 Hamilton–Jacobi 方程.

因此可以形成如下完整链条：

$$
\text{波动光学}
\rightarrow
\text{几何光学}
$$

对应

$$
\text{量子力学}
\rightarrow
\text{经典力学}
$$

而两边的短波长极限分别由程函方程与 Hamilton–Jacobi 方程描述.

这也是为什么“作用量等值面类似于波阵面”并不是单纯的数学比喻，而具有更深的物理来源.

---

# 18. 总结

Hamilton–Jacobi 方程可以从光力类比非常自然地理解.

几何光学中，光的传播并不一定要逐条追踪光线，也可以先求相位函数或程函

$$
W_{\rm opt}
$$

然后利用

$$
\mathbf k=\nabla W_{\rm opt}
$$

恢复光线.

经典力学中也可以不直接求每一条轨迹，而先求 Hamilton 主函数

$$
S(\mathbf q,t)
$$

其梯度给出动量：

$$
\mathbf p=\nabla_{\mathbf q}S
$$

作用量的等值面

$$
S=\mathrm{const}
$$

因此可以类比为力学中的波阵面.

从作用量驻值原理出发，对经典作用量做端点变分得到

$$
dS
=
\mathbf p\cdot d\mathbf q
-
Hdt
$$

因此

$$
\mathbf p
=
\nabla_{\mathbf q}S
$$

以及

$$
\frac{\partial S}{\partial t}=-H
$$

最终得到

$$
\frac{\partial S}{\partial t}
+
H(\mathbf q,\nabla_{\mathbf q}S,t)
=0
$$

这就是 Hamilton–Jacobi 方程.

在定能量情形下，

$$
S=W-Et
$$

从而有

$$
H(\mathbf q,\nabla W)=E
$$

对于

$$
H=\frac{\mathbf p^2}{2m}+V
$$

则变为

$$
|\nabla W|
=
\sqrt{2m(E-V)}
$$

它与几何光学中的

$$
|\nabla W_{\rm opt}|=n
$$

完全平行.

因此最简洁的理解是：

> Hamilton–Jacobi 理论把经典力学从“轨迹动力学”改写成了“作用量波阵面的传播理论”，而经典轨迹就是这些等作用量面的特征线.
