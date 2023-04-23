---
layout: entry
changelog:
  - summary: 記事作成
    authors: noshi91
    reviewers: []
    date: 2021-09-15T21:46:53+09:00
algorithm:
  input: >
    体 $\mathbb{K}$ 上の長さ $n$ の列 $v$、$a, q \in \mathbb{K} \setminus \lbrace 0 \rbrace$。
    ただし $q ^ i \neq 1 ~ (0 \leq i \lt n)$ とする。
  output: すべての $0 \leq i \lt n$ に対して $f(aq ^ i) = v _ i$ を満たす高々 $n$ 次の多項式 $f$
  time_complexity: $\Theta(n \log(n) )$
  space_complexity: $\Theta(n)$
  aliases: ["inverse chirp z transform", "ICZT"]
  level: red
description: >
    標本点が等比数列を成す場合に補間多項式を $\Theta(n \log(n) )$ の時間計算量で計算する。
    ただし、$\mathbb{K}$ 上の長さ $n$ の列の畳み込みの時間計算量を $\Theta(n \log(n))$、空間計算量を $\Theta(n)$ としている。
    標本点が任意の数列である場合と比べて、およそ $\Theta(\log(n))$ 倍の改善となる。
draft: true
draft_urls: []
---

# 標本点が等比数列を成す場合に補間多項式を計算するアルゴリズム

## 概要

標本点が等比数列を成す場合に補間多項式を $\Theta(n \log(n) )$ の時間計算量で計算する。
ただし、$\mathbb{K}$ 上の長さ $n$ の列の畳み込みの時間計算量を $\Theta(n \log(n))$、空間計算量を $\Theta(n)$ としている。
標本点が任意の数列である場合と比べて、およそ $\Theta(\log(n))$ 倍の改善となる。

本ページでは、Alin Bostan による説明[^Bostan] をもとに、定数倍を改善した計算方法を説明する。

## 詳細

まず、$a = 1$ の場合の計算方法を示す。
求める補間多項式は以下の式で与えられる。

$$ \begin{equation}
  f(x) = \sum _ {i = 0} ^ {n - 1} v _ i \frac{\prod _ {j \neq i} \left( x - q ^ j \right)}{\prod _ {j \neq i} \left( q ^ i - q ^ j \right)}
\end{equation} $$

$\displaystyle s _ i \coloneqq \prod _ {j = 1} ^ {i} \left( 1 - q ^ j \right)$ と定義すれば、$(1)$ の分母は以下のように表される。

$$ \begin{equation} \begin{aligned}
  \prod _ {j \neq i} \left( q ^ i - q ^ j \right)
  &= \left( \prod _ {j \lt i} \left( q ^ i - q ^ j \right) \right) \left( \prod _ {j \gt i} \left( q ^ i - q ^ j \right) \right) \cr
  &= \left( \prod _ {j \lt i} q ^ j \left( q ^ {i - j} - 1 \right) \right) \left( \prod _ {j \gt i} q ^ i \left( 1 - q ^ {j - i} \right) \right) \cr
  &= \left( (- 1) ^ {i} q ^ {i(i - 1) / 2} \prod _ {j \lt i} \left( 1 - q ^ {i - j} \right) \right) \left( q ^ {i(n - i - 1)} \prod _ {j \gt i} \left( 1 - q ^ {j - i} \right) \right) \cr
  &= (- 1) ^ {i} q ^ {i(i - 1) / 2} q ^ {i(n - i - 1)} s _ {i} s _ {n - i - 1}
\end{aligned} \end{equation} $$

$q ^ {(i + 1)i / 2} q ^ {(i + 1)(n - (i + 1) - 1)} = q ^ {n - i - 2} q ^ {i(i - 1) / 2} q ^ {i(n - i - 1)}$ に注意すると、時間計算量 $\Theta(n)$ ですべての $i$ に対して $(2)$ を計算できる。
$\displaystyle w _ i \coloneqq \frac{v _ i}{\prod _ {j \neq i} \left( q ^ i - q ^ j \right)}$ と定義すれば、残る課題は以下の値を計算することである。

$$ \begin{equation} \begin{aligned}
  f(x) &= \sum _ {i = 0} ^ {n - 1} w _ i \prod _ {j \neq i} \left( x - q ^ j \right) \cr
  &= \left(\prod _ {i = 0} ^ {n - 1} \left (x - q ^ j \right) \right) \left( \sum _ {i = 0} ^ {n - 1} \frac{w _ i}{x - q ^ i} \right)
\end{aligned} \end{equation} $$

### $\displaystyle \prod _ {i = 0} ^ {n - 1} \left (x - q ^ j \right)$ の計算

証明なしに、以下の事実を認める。

#### Cauchy Binomial Theorem [^q-binomial]

$$
  \prod _ {i = 1} ^ {n} \left( 1 + yq ^ i \right) = \sum _ {k = 0} ^ {n} q ^ {k(k + 1) / 2} \binom{n}{k} _ q y ^ k
$$

$y = - 1 / qx$ を代入し両辺に $x ^ n$ を掛けることで、以下の式を得る

$$
  \prod _ {i = 0} ^ {n - 1} \left( x - q ^ i \right) = \sum _ {k = 0} ^ {n} (- 1) ^ {k} q ^ {k(k - 1) / 2} \binom{n}{k} _ q x ^ {n - k}
$$

$q ^ {(k + 1)k / 2} = q ^ k q ^ {k(k - 1) / 2}$ と $\displaystyle \binom{n}{k} _ q = \frac{s _ n}{s _ k s _ {n - k}}$ を用いると、$\displaystyle \prod _ {i = 0} ^ {n - 1} \left( x - q ^ i \right)$ は $\Theta(n)$ で計算できる。

### $\displaystyle \sum _ {i = 0} ^ {n - 1} \frac{w _ i}{x - q ^ i}$ の計算

$\mathbb{K}\lbrack \lbrack x \rbrack \rbrack$ において上の式を $\bmod x ^ n$ で計算できればよい。

$$ \begin{aligned}
  \sum _ {i = 0} ^ {n - 1} \frac{w _ i}{x - q ^ i}
  &= \sum _ {i = 0} ^ {n - 1} \sum _ {j = 0} ^ {\infty} - w _ i q ^ {-i(j + 1)} x ^ j \cr
  &= \sum _ {j = 0} ^ {\infty} \left( \sum _ {i = 0} ^ {n - 1} - w _ i \left( q ^ {- (j + 1)} \right) ^ i \right) x ^ j
\end{aligned} $$

であるから、多項式 $g$ を $\displaystyle g(y) \coloneqq \sum _ {i = 0} ^ {n - 1} - w _ i y ^ i$ と定義すれば、$g(q ^ {- (j + 1)})$ が $0 \leq j \lt n$ に対して求まればよい。
これは [chirp z-transform](/algorithm-encyclopedia/chirp-z-transform) を用いて $\Theta(n \log(n) )$ で計算できる。


以上より、$(3)$ の計算を $\Theta(n \log(n) )$ で行うことができる。
$a \neq 1$ の場合は、上記の方法で $f(q ^ i) = v _ i$ を満たす多項式 $f$ を計算したのち、その $k$ 次の係数を $a ^ {-k}$ 倍することで求める多項式が得られる。

## 参考文献

1.  [Bostan, A. (2010). Fast algorithms for polynomials and matrices. JNCF 2010. Algorithms Project, INRIA.](https://specfun.inria.fr/bostan/publications/exposeJNCF.pdf)<sup>[archive.org](https://web.archive.org/web/20221220161514/https://specfun.inria.fr/bostan/publications/exposeJNCF.pdf)</sup>

1.  Bostan, A., & Schost, É. (2005). Polynomial evaluation and interpolation on special sets of points. Journal of Complexity, 21(4), 420-446.
    -   Newton basis を経由することで、同じく $\Theta(n \log(n) )$ の時間計算量をもつアルゴリズムを導出している。

## 注釈

[^Bostan]: [Bostan, A. (2010). Fast algorithms for polynomials and matrices. JNCF 2010. Algorithms Project, INRIA.](https://specfun.inria.fr/bostan/publications/exposeJNCF.pdf)<sup>[archive.org](https://web.archive.org/web/20221220161514/https://specfun.inria.fr/bostan/publications/exposeJNCF.pdf)</sup> pp. 48-49

[^q-binomial]: [Cauchy Binomial Theorem -- from Wolfram MathWorld](https://mathworld.wolfram.com/CauchyBinomialTheorem.html)<sup>[archive.org](https://web.archive.org/web/20211112150455/https://mathworld.wolfram.com/CauchyBinomialTheorem.html)</sup>
