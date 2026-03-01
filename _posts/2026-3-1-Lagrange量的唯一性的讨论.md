---
title: Lagrange 量的唯一性的讨论
toc: true
categories:
  - 物理
tags:
  - 理论力学
---


本文简单讨论的 Lagrange 量的唯一性.

<!--more-->

## Goldstein 中的原题
在 Goldstein 的理论力学习题中有如下一道题：

<div class="notice--info" markdown="1">
一质量为 $m$ 的质点作一维运动，其 Lagrange 量为

$$\mathcal{L} = \frac{m^2 \dot{x}^4}{12} + m \dot{x}^2 V - V^2$$

式子中 $V$ 是 $x$ 的某一可微函数。求 $x(t)$ ，并描述其物理意义。
</div>

其解答如下：

$$
\begin{aligned}
    \frac{\partial \mathcal{L}}{\partial \dot{x}} &= \frac{1}{3} m^2 \dot{x}^3 + 2m \dot{x} V \\
    \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) &= m^2 \dot{x}^2 \ddot{x} + 2m \ddot{x} V + 2m \dot{x}^2 \frac{\partial V}{\partial x} \\
    \frac{\partial \mathcal{L}}{\partial x} &= (m \dot{x} - 2V) \frac{\partial V}{\partial x}
\end{aligned}
$$

上式带入 E-L 方程，可得

$$
\begin{aligned}
    \frac{\partial \mathcal{L}}{\partial x} - \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) &= 0 \\
    -2(T+V) \left( m \ddot{x} + \frac{\partial V}{\partial x} \right) &= 0
\end{aligned}
$$

其中 $T = \frac{1}{2} m \dot{x}^2$。 

由于 $(T+V)$ 等于能量为定值，因此上面方程等价于

$$m \ddot{x} = - \frac{\partial V}{\partial x}$$

即牛顿体系下经典的运动方程。

另外，我们还可以构造其 Hamilton 量，对上面 Lagrange 量做 Legendre 变换，有

$$\mathcal{H} = p \dot{q} - \mathcal{L} = (T+V)^2$$

可见其 Hamilton 量为能量 $E$ 的平方。

## 借助 Hamilton 量构造等价的 Lagrange 量

从上面的例题中可以看出，满足 $m \ddot{x} = - \partial_x V$ 的 Lagrange 量不单是 $\mathcal{L} = T - V$，还存在有其他的等价的形式[^1]。由前文的 Hamilton 量为能量 $E$ 的平方我们可以猜想，要构造其他的等价的 Lagrange 量，只需要让 Hamilton 量为能量 $E$ 的不同次方即可。

我们假设：

$$\mathcal{H} = (T+V)^n,\quad \mathcal{L} = \sum_{i=0}^{n} a_i T^i V^{n-i}$$

则其广义动量为（注意到 $\frac{\partial T}{\partial \dot{q}} = m \dot{q}$）：

$$p = \frac{\partial \mathcal{L}}{\partial \dot{q}} = \sum_{i=0}^{n} \left[ i \cdot a_i V^{n-i} T^{i-1} m \dot{q} \right]$$

对上面的 Lagrange 量做 Legendre 变换，有：

$$
\begin{aligned}
  \mathcal{H} &= p \dot{q} - \mathcal{L} \\
    &= \sum_{i=0}^{n} \left[ i a_i m \dot{q}^2 V^{n-i} T^{i-1} - a_i T^i V^{n-i} \right] \\
    &= \sum_{i=0}^{n} \left[ (2i-1) a_i T^i V^{n-i} \right]
\end{aligned}
$$

又由于：

$$\mathcal{H} = (T+V)^n = \sum_{i=0}^{n} C^i_n T^i V^{n-i}$$

因此有：

$$a_i = \frac{C_n^i}{2i-1}$$

于是，我们可以得到一系列的等价的 Lagrange 量：

* 当 $n=1$ 时，$\mathcal{L} = T-V$
* 当 $n=2$ 时，$\mathcal{L} = \frac{1}{3}T^2 + 2TV -V^2$
* 当 $n=3$ 时，$\mathcal{L} = \frac{1}{5}T^3 + T^2 V + 3 T V^2 - V^3$

不难验证，上面的式子都等价于牛顿体系下经典的运动方程。

## 借助牛顿第二定律构造等价的 Lagrange 方程

在最开始的例题中，通过 Lagrange 方程所得到的运动学方程为：

$$2(T+V) \left( m \ddot{x} + \frac{\partial V}{\partial x} \right) = 0$$

因此，我们猜测，通过在牛顿第二定理（$m \ddot{x} + \partial_x V = 0$）乘上一些守恒量后反解出对应的 Lagrange 量便可以得到其他等价的 Lagrange 量。根据例题的形式，我们可以猜测其他等价的运动学方程满足：

$$c_1 (T+V)^{n-1} \left( m \ddot{x} + \frac{\partial V}{\partial x} \right) = c_1 \left( m \ddot{q} + V' \right) \sum_{i=0}^{n-1} C^i_{n-1} T^i V^{n-i-1} = 0$$

其中 $c_1$、$n$ 均为常数。由于直接反解出对应的 Lagrange 量较为复杂[^2]。因此我们同样通过待定系数法来得到对应的 Lagrange 量。假设

$$\mathcal{L} = \sum_{i=0}^{n} a_i T^i V^{n-i}$$

因此有（注意到 $\frac{\partial T}{\partial \dot{q}} = \frac{\partial}{\partial \dot{q}} \frac{1}{2} m \dot{q}^2 = m \dot{q}$）：

$$
\begin{aligned}
  \frac{\partial \mathcal{L}}{\partial \dot{q}} &= \sum_{i=0}^{n} i a_i m \dot{q} T^{i-1} V^{n-i} \\
  \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial \mathcal{L}}{\partial \dot{q}} \right) &= \sum_{i=0}^{n} i a_i m \left[ \dot{q} T^{i-1} (n-i) V^{n-i-1} V' \dot{q} + \ddot{q} T^{i-1} V^{n-i} + \dot{q} V^{n-i} (i-1) T^{i-2} m \dot{q} \ddot{q} \right] \\
                        &= \sum_{i=0}^{n} i a_i m \left[ (n-i) \dot{q}^2 V' T^{i-1} V^{n-i-1} + (2i-1) \ddot{q} T^{i-1} V^{n-i} \right] \\
  \frac{\partial \mathcal{L}}{\partial q} &= \sum_{i=0}^{n} a_i T^i (n-i) V^{n-i-1} V'
\end{aligned}
$$

上面的 $V'$ 表示 $\partial_x V$。带入 E-L 方程，得到运动学方程为：

$$
\begin{aligned}
   & \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial \mathcal{L}}{\partial \dot{q}} \right) - \frac{\partial \mathcal{L}}{\partial q} \\
  =& \sum_{i=0}^{n} \left[ i a_i m \left[ (n-i) \dot{q}^2 V' T^{i-1} V^{n-i-1} + (2i-1) \ddot{q} T^{i-1} V^{n-i} \right] - a_i T^i (n-i) V^{n-i-1} V' \right] \\
  =& \sum_{i=0}^{n} \left[ a_i (2i-1) (n-i) V' T^i V^{n-i-1} + a_i (2i-1) i m \ddot{q} T^{i-1} V^{n-i} \right] \\
  =& a_0 (2 \cdot 0 -1) \cdot 0 \cdot m \ddot{q} T^{-1} V^n + a_n (2n-1)(n-n) V' T^n V^{-1} \\ 
   &+ \sum_{i=0}^{n-1} \left[ a_i (2i-1) (n-i) V' T^i V^{n-i-1} + a_{i+1} (2i+1) (i+1) m \ddot{q} T^i V^{n-i-1} \right] \\ 
  =& \sum_{i=0}^{n-1} \left[ a_i (n-i) (2i-1) V' + a_{i+1} (2(i+1)-1) (i+1) m \ddot{q} \right] T^i V^{n-i-1}
\end{aligned}
$$

上面的运动学方程中如果我们想继续化简从而凑出 $(m \ddot{q} +V')$ 的因子，就要求有：

$$a_i (2i-1)(n-i) = a_{i+1} [2(i+1)-1] (i+1)$$

记 $b_i = a_i (2i-1)$，因此有 $b_i (n-i) = b_{i+1} (i+1)$，因此：

$$b_i = \frac{b_{i-1}}{n} = \frac{(1 \cdot 2) b_{i-2}}{n(n-1)} \cdots$$

因此 $b_i = C^i_n$，$a_i = \frac{C^i_n}{2i-1}$。因此

$$
\begin{aligned}
  \frac{\mathrm{d}}{\mathrm{d}t} \left( \frac{\partial \mathcal{L}}{\partial \dot{q}} \right) &= \sum_{i=0}^{n-1} C^i_n (n-i) (m \ddot{q} +V') T^i V^{n-i-1} \\
                             &= \sum_{i=0}^{n-1} n (m \ddot{q} +V') C^i_{n-1} T^i V^{n-i-1} \\
                             &= n(m \ddot{q} + V') \sum_{i=0}^{n-1} C^i_{n-1} T^i V^{n-i-1} \\
                             &= n(m \ddot{q} + V')(T+V)^{n-1}
\end{aligned}
$$

此形式与我们所假设的形式相同，因此，我们可以得到我们所假设的运动方程的常数 $c_1 = n$，其对应的 Lagrange 量为：

$$\mathcal{L} = \sum_{i=0}^{n} a_i T^i V^{n-i}, \quad a_i = \frac{C^i_n}{2i-1}$$

这与我们借助 Hamilton 量构造的等价的 Lagrange 量相同[^3]。 

[^1]: 那这里自然会有一个问题，即为什么经典的 Lagrange 量都选取为 $T-V$ 的形式？笔者认为是因为其形式简单且易从经典的矢量力学中得到。
[^2]: 这类问题也被称作“变分问题的反问题”，参考梅凤翔《微分方程的分析力学方法》。
[^3]: 通过 Hamilton 量得到的 Lagrange 量的过程严格来说其实并不能说明其等价，但通过解 E-L 方程得到运动学方程的方式则可以严格说明其等价。
