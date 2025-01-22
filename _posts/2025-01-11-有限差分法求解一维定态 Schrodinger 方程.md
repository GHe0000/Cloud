---
title: 有限差分法求解一维定态 Schrodinger 方程
toc: true
categories:
  - 数值计算
tags:
  - 薛定谔方程
  - 计算机模拟
  - 数值计算
---

有限差分法的简单介绍，以及在求解一维定态 Schrodinger 方程中的应用.

<!-- more -->

（此笔记是 2021-8-11 的笔记的重新整理和完善，同时将原本的 Matlab 程序用 Python 重新实现）

## 有限差分法

### 简要介绍

有限差分的基本思想非常简单：在一些微积分教材中，我们常常将 $\Delta y / \Delta x$ 取极限得到 $\mathrm{d} y / \mathrm{d} x$，因此，在计算 $\mathrm{d} y / \mathrm{d} x$ 时，我们可以通过如下式子进行数值计算：

$$ 
\begin{aligned}
y'(x) &= \lim_{\Delta x \to 0} \frac{y(x+\Delta x) - y(x)}{\Delta x} \\
      &\approx \frac{y(x+\Delta x)-y(x)}{\Delta x}
\end{aligned}
$$

这里的 $\Delta x$ 即为**步长**，其影响了微分近似的精确程度，步长越小，近似越精确.

### 差分公式推导

一般地，对于函数 $y(x)$，若在求解域内连续可导，由 Taylor 展开我们可以得到：

$$
y(x+h) = y(x) + y'(x) h + \frac{1}{2} y''(x) h^2 + \cdots + \frac{1}{n!} y^{(n)} (x) h^n + \frac{1}{(n+1)!} y^{(n+1)} (x+\xi) h^{n+1}
$$

对上面 Taylor 展开进行适当的截断，我们就可以得到各阶微分的近似表达式，下面主要对一阶、二阶进行讨论：

对于一阶，我们可以写为：

$$
y(x+h) \approx y(x) + y'(x) h + \frac{1}{2} y''(x+\xi) h^2
$$

因此，可以解得一阶微分的向前差分公式：

$$y'_F(x) \approx \frac{y(x+h)-y(x)}{h}$$

将上式中 $h$ 替换成 $-h$，便可以得到一阶微分的向后差分公式：

$$y'_B(x) \approx \frac{y(x)-y(x-h)}{h}$$

联立上面两式，便可以得到一阶差分的中心差分形式：

$$ y'_C(x) \approx \frac{y(x+h)-y(x-h)}{2h}$$

类似地，对于高阶导数的差分近似，我们也可以用类似的方法得到，若我们保留到 Taylor 展开的二次项，便可以得到：

$$y''(x) \approx \frac{2(y(x+h)-y(x)-y'(x) h)}{h^2}$$

将 $h$ 替换成 $-h$，并同上式联立，我们就可以得到二阶差分的中心差分形式：

$$ y''(x) \approx \frac{y(x+h)-2y(x)+y(x-h)}{h^2} $$

对于更高阶导数的差分近似，也可以用类似的方法求解.

另外，不同的差分公式会带来不同的求解误差，从而产生不一样的求解效果. 一般而言，中心差分的精度较高，误差较小，因此我们一般选择使用中心差分.

## 求解一维定态 Schrodinger 方程

### 理论推导

求解一维定态 Schrodinger 方程，也就是求解下面的方程：

$$H \psi(x) = E \psi(x)$$

其中算符 $H$ 为：

$$H = -\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d} x^2}+V$$ 

而能量 $E$ 为一个标量. 上式可以发现其很像特征方程的形式（实际上在教材的计算中我们常常将函数当成 Hilbert 空间中的一个向量，然后还是通过特征方程那一套来分析），因此我们可以考虑将坐标 $x$ 离散化成一个一维向量：

$$ x=(x_1,x_2,x_3,\dots,x_n)^T $$

其中，记 $\Delta x = x_{i+1} - x_i$，为步长. 因此，波函数 $\psi(x)$ 就可以表示为：

$$\psi = (\psi(x_1),\psi(x_2),\psi(x_3),\dots,\psi(x_n))^T$$

根据前文，通过二阶差分的中心差分形式来代替算符 $H$ 中的的二阶导，故有：

$$
\begin{aligned}
\frac{\mathrm{d}^2 \psi(x_i)}{\mathrm{d}x^2} \approx& \frac{\psi(x_i+\Delta x) - 2 \psi(x_i) + \psi(x_i - \Delta x)}{\Delta x^2} \\
\approx& \frac{\psi(x_{i+1}-2\psi(x_i)+\psi(x_{i-1}))}{\Delta x^2}
\end{aligned}
$$

对每一个 $\psi(x_i)$ 都使用上式来计算其二阶导，其可以用如下矩阵表示：

$$
D = \frac{1}{\Delta x^2}
\begin{bmatrix}
-2 & 1 & 0 & 0 & \cdots & 0 \\
1 & -2 & 1 & 0 & \cdots & 0 \\
0 & 1 & -2 & 1 & \cdots & 0 \\
\vdots&\vdots&\vdots&\vdots&\ddots & \vdots \\
0 & 0 & 0 & 0 & \cdots & -2
\end{bmatrix}
$$

因此，整个算符 $H$ 可以用如下矩阵表示：

$$H = -\frac{\hbar^2}{2m \Delta x^2} D + V$$

这里 $V$ 也要改写为矩阵的形式.

  
上式可改为矩阵形式，则定态薛定谔方程可改写为

通过上述方法，该问题简化为求解特征值和特征向量的问题，其中特征值为该能级能量，特征向量为（离散后的）波函数.

### 程序实现

上述算法的具体程序实现是非常简单的，下面用 Python 具体实现.

首先我们先导入一些计算库，并定义一些常量：

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, spdiags
from scipy.sparse.linalg import eigsh

hbar = 1
m = 1
X = 10
N = 200
dx = 2 * X / N
En = 9
```

然后，我们离散化坐标，得到 $x$，并计算每一个坐标的势能，构造出矩阵 $V$（这里以谐振子势为例子）：

```python
# 离散化空间坐标
x = np.linspace(-X, X, N)

v = 0.5 * x**2
V = diags(v, 0)
```

之后，我们根据前文的公式来构造对角的差分矩阵，并以此进一步构造算符 $H$：

```python
A = np.ones(N)
D = spdiags([1 * A, -2 * A, 1 * A], [-1, 0, 1], N, N)
D = (-(hbar**2) / (2 * m)) * (1 / dx**2) * D

H = D + V
```

然后，我们计算特征值及特征向量，这里由于矩阵中大部分为 $0$，为减小计算量，我们使用针对稀疏矩阵优化的计算特征值和特征向量的函数：

```python
Val, Vec = eigsh(H, k=En, which='SA')
```

后面绘图，显示结果：

```python
for i in range(En):
    psi = Vec[:, i]
    E = Val[i]
    ax1 = plt.subplot(3, 3, i + 1)
    ax1.plot(x, psi**2 / np.sum(psi**2 * dx), label=r'$|\Psi(x)|^2$', color='g')
    ax1.set_xlabel('x')
    ax1.set_ylabel(r'$|\Psi(x)|^2$', color='g')
    ax1.tick_params(axis='y', labelcolor='g')
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(x, v, label='V(x)', color='b')
    ax2.set_ylabel('V(x)', color='b')
    ax2.tick_params(axis='y', labelcolor='b')
    
    plt.title(f'n={i+1} E={E:.3f}')

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
```
