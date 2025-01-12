---
title: 有限差分法求解一维定态 Schrodinger 方程
categories:
  - 物理
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
y'(x) &= \lim_{\Delta x \to 0} \frac{y(x+\Delta x) - y(x)}{\Delta x}
      &\approx \frac{y(x+\Delta x)-y(x)}{\Delta x}
\end{aligned}
$$

这里的 $\Delta x$ 即为**步长**，其影响了微分近似的精确程度，步长越小，近似越精确.

### 高阶差分近似

一般地，对于函数 $y(x)$，若在求解域内连续可导，由 Taylor 展开我们可以得到：

$$
y(x+h) = y(x) + y'(x) h + \frac{1}{2} y''(x) h^2 + \cdots + \frac{1}{n!} y^{(n)} (x) h^n + \frac{1}{(n+1)!} y^{(n+1)} (x+\ksi) h^{n+1}
$$

对上面 Taylor 展开进行适当的截断，我们就可以得到各阶微分的近似表达式，下面主要对一阶、二阶进行讨论：

对于一阶，我们可以写为：

$$
y(x+h) \approx y(x) + y'(x) h + \frac{1}{2} y''(x+\ksi) h^2
$$

因此，可以解得一阶微分的向前差分公式


对于高阶导数，我们也可以用类似的方法进行近似：对于 $\Delta^x y / \Delta x^2$，其可以通过如下式子进行近似：

$$
\begin{aligned}
y''(x) &= \
\end{aligned}
$$

## 求解一维定态 Schrodinger 方程

对于定态薛定谔方程

$$H\psi=E\psi$$

其中

$$H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V$$  

记

$$C_1 = -\frac{\hbar^2}{2m}$$

对$$\frac{d^2}{dx^2}$$差分得  

$$
\frac{d^2}{dx^2} \approx \frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}{\Delta x^2}
$$  

上式可改为矩阵形式，则定态薛定谔方程可改写为$$H\Psi = E\Psi$$  

其中

$$
\Psi = 
\begin{bmatrix}
\psi_1\\
\psi_2\\
\vdots
\end{bmatrix}
$$

$$
H = A + V
$$

$$
A = \frac{C_1}{\Delta x^2} * 
\begin{bmatrix}
-2 & 1 & 0 & 0 & \cdots \\
1 & -2 & 1 & 0 & \cdots \\
0 & 1 & -2 & 1 & \cdots \\
\vdots&\vdots&\vdots&\vdots&\vdots\ \\
\end{bmatrix}
$$  

则该问题简化为求解特征值和特征向量的问题，其中特征值为该能级能量，特征向量为薛定谔方程离散值  

