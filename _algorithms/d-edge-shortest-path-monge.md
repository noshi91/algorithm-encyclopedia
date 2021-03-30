---
layout: entry
changelog:
  - summary: ページ作成
    authors: noshi91
    reviewers:
    date: 2021-03-28T20:41:31+09:00
algorithm:
  input: >
    Monge 性を満たす整数の辺重み $c : E \to \mathbb{Z}$ 付き完全 DAG $G = (N, E = \lbrace (i, j) \mid i \lt j \rbrace)$ 及び正整数 $d$
  output: 辺を丁度 $d$ 本使う条件下での $0$-$(N - 1)$ 最短路長
  time_complexity: $\Theta (N \log(\max _ {e \in E} \lvert c(e) \rvert))$
  space_complexity: $\Theta (N)$
  aliases: ["Alien DP", "WQS binary search"]
  level: orange
description: >
    辺の重みが Monge 性を満たすような完全 DAG について、辺を丁度 $d$ 本使う条件下での $0$-$(N-1)$ 最短路長を $\Theta (N \log(\max _ {e \in E} \lvert c(e) \rvert))$ で計算するアルゴリズムが存在する。
    Monge 性からラグランジュ双対問題について強双対性が成立し、ラグランジュ緩和問題もまた Monge 性を利用して高速に解くことができる。
---

# Monge グラフ上の $d$-辺最短路長

## 概要

$G = (N, E = \lbrace (i, j) \mid i \lt j \rbrace)$ を $N$ 頂点の完全 DAG、$c : E \to \mathbb{Z}$ を Monge 性を満たす辺重み、$d$ を正整数とする。
辺を丁度 $d$ 本使う条件下での $0$-$(N-1)$ 最短路長を $\Theta (N \log(\max _ {e \in E} \lvert c(e) \rvert))$ で計算するアルゴリズムが存在する。

この問題は制約付き最適化であり、ラグランジュ双対問題を考えることで効率的に解くことができる。
$c$ の Monge 性はラグランジュ双対問題の強双対性を成立させる。

ラグランジュ緩和問題は、全ての辺の重みを $\lambda$ 大きくした場合の (辺の数の制約のない) 最短路問題となる。
$c$ が Monge なら、一様に $\lambda$ を加算したものもまた Monge である。
Monge 性を満たす辺重みについての最短路は $\Theta (N)$ で計算することができる。

Aliens[^Aliens] はこの問題に帰着することができる。それに由来して、特にラグランジュ双対問題を用いる発想を指して Alien DP と呼ぶことがある[^kort0n-alienDP]。また、WQS binary search とも呼ばれる[^WQS-binary-search]。

## Monge

この記事中では、辺重み $c : E \to \mathbb{Z}$ が Monge であるとは、
$$\forall i, j, k, l.\  0 \leq i \lt j \lt k \lt l \lt N \rightarrow c(i, l) + c(j, k) \geq c(i, k) + c(j, l)$$
を満たすことを言うこととする。

Monge は通常は $N \times M$ 行列に対して定義される概念であるが、ここでは $c$ が上三角部分のみについて定義されているので、制限した形で定義した。

## ラグランジュ双対問題

$\mathcal{P}$ を $G$ の $0$-$(N - 1)$ パス全体とする。
$P \in \mathcal{P}$ に対して、$\lVert P \rVert$ を $P$ の辺の本数、$c(P)$ を $P$ の辺の重みの和とする。

求めたい値は $\displaystyle \min _ {P \in \mathcal{P}, \lVert P \rVert = d} c(P)$ である。

任意の $\lambda \in \mathbb{Z}$ に対して、以下の式が成り立つ。
$$ \begin{equation} \begin{split}
  \min _ {P \in \mathcal{P}, \lVert P \rVert = d} c(P) & = \min _ {P \in \mathcal{P}, \lVert P \rVert = d} (c(P) + \lambda (\lVert P \rVert - d)) \cr
  & \geq \min _ {P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
\end{split} \end{equation}$$
このように制約の一部を除去し、除去した制約について違反した量を一次のペナルティ[^lagrangian-penalty] として目的関数に組み込んだ問題をラグランジュ緩和問題と呼ぶ[^lagrangian-relaxation]。
ラグランジュ緩和問題の解は、元の問題の解の下界を与えている。

$(1)$ から、さらに以下の式が成り立つ。
$$ \begin{equation}
  \min _ {P \in \mathcal{P}, \lVert P \rVert = d} c(P) \geq \max _ {\lambda \in \mathbb{Z}} \min _ {P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
  \tag{2}
\end{equation} $$
これは、$\lambda$ を調整することで得られる最もよい下界を考えていると解釈できる。
この最良の下界を求める問題をラグランジュ双対問題と呼ぶ。

### 強双対性

$(2)$ について、$\displaystyle P ^ {\ast} \in \argmin _ {P \in \mathcal{P}} (c(P) + \lambda ^ {\ast} (\lVert P \rVert - d)) \land \lVert P ^ {\ast} \rVert = d$ となる $\lambda ^ {\ast} \in \mathbb{Z}, P ^ {\ast} \in \mathcal{P}$ が存在したとする。
すると、$(2)$ の不等号が逆向きにも成立し、等号が成立する。
$$ \begin{align*}
  \min _ {P \in \mathcal{P}, \lVert P \rVert = d} c(P) & \leq c(P ^ {\ast}) \cr
  & = c(P ^ {\ast}) + \lambda ^ {\ast} (\lVert P ^ {\ast} \rVert - d) \cr
  & = \min _ {P \in \mathcal{P}} (c(P) + \lambda ^ {\ast}(\lVert P \rVert - d)) \cr
  & \leq \max _ {\lambda \in \mathbb{Z}} \min _ {P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
\end{align*} $$
主問題と双対問題の解が一致することを、強双対性と呼ぶ。

以降、$\displaystyle P ^ {\ast} \in \argmin _ {P \in \mathcal{P}} (c(P) + \lambda ^ {\ast} (\lVert P \rVert - d)) \land \lVert P ^ {\ast} \rVert = d$ となる $\lambda ^ {\ast} \in \mathbb{Z}, P ^ {\ast} \in \mathcal{P}$ の存在を示す。

$P _ k ^ {\ast}$ を、丁度 $k$ 本の辺を使う条件下の $0$-$(N-1)$ 最短路と定義する。複数存在する場合、任意に $1$ つとる。

#### 補題 $1$

$$\forall k.\ 2 \leq k \leq N - 2 \rightarrow c(P _ k ^ {\ast}) - c(P _ {k - 1} ^ {\ast}) \leq c(P _ {k + 1} ^ {\ast}) - c(P _ k ^ {\ast})$$

##### 証明

$\lVert P _ a \rVert = \lVert P _ b \rVert = k$ となるパス $P _ a, P _ b \in \mathcal{P}$ であって $c(P _ {k - 1} ^ {\ast}) + c(P _ {k + 1} ^ {\ast}) \geq c(P _ a) + c(P _ b)$ であるものの存在を示す。
もしそれが示されたならば、$c(P _ {k - 1} ^ {\ast}) + c(P _ {k + 1} ^ {\ast}) \geq c(P _ a) + c(P _ b) \geq c(P _ k ^ {\ast}) + c(P _ k ^ {\ast})$ を移項することで求める式を得る。

$P _ {k - 1} ^ {\ast} = s _ 0 s _ 1 \dots s _ {k - 1}, P _ {k + 1} ^ {\ast} = t _ 0 t _ 1 \dots t _ {k + 1}$ とする。$s _ 0 = t _ 0 = 0, s _ {k - 1} = t _ {k + 1} = N - 1$ である。
各 $0 \leq x \leq  k - 1$ について、$s _ x$ と $t _ {x + 1}$ の大小を比較する。
$s _ 0 \lt t _ 1$ かつ $s _ {k - 1} \gt t _ k$ であるから、$s _ x = t _ {x + 1}$ を満たす $x$ が存在するか、さもなくば $s _ x \lt t _ {x + 1} \land s _ {x + 1} \gt t _ {x + 2}$ を満たす $x$ が存在する。

-   $s _ x = t _ {x + 1}$ を満たす $x$ が存在する場合

    $$ \begin{align*}
      P _ a &\coloneqq s _ 0 s _ 1 \dots s _ x t _ {x + 2} t _ {x + 3} \dots t _ {k + 1} \cr
      P _ b &\coloneqq t _ 0 t _ 1 \dots t _ {x + 1} s _ {x + 1} s _ {x + 2} \dots s _ {k - 1}
    \end{align*} $$
    とすればよい。
    $c(P _ {k - 1} ^ {\ast}) + c(P _ {k + 1} ^ {\ast}) = c(P _ a) + c(P _ b)$ である。
-   $s _ x \lt t _ {x + 1} \land s _ {x + 1} \gt t _ {x + 2}$ を満たす $x$ が存在する場合

    整理すると、$s _ x \lt t _ {x + 1} \lt t _ {x + 2} \lt s _ {x + 1}$ である。
    $$ \begin{align*}
      P _ a &\coloneqq s _ 0 s _ 1 \dots s _ x t _ {x + 2} t _ {x + 3} \dots t _ {k + 1} \cr
      P _ b &\coloneqq t _ 0 t _ 1 \dots t _ {x + 1} s _ {x + 1} s _ {x + 2} \dots, s _ {k - 1}
    \end{align*} $$
    とすればよい。
    $c$ の Monge 性から $c(s _ x, s _ {x + 1}) + c(t _ {x + 1}, t _ {x + 2}) \geq c(s _ x, t _ {x + 2}) + c(t _ {x + 1}, s _ {x + 1})$ であり、$c(P _ {k - 1} ^ {\ast}) + c(P _ {k + 1} ^ {\ast}) \geq c(P _ a) + c(P _ b)$ が従う。

$\blacksquare$

補題 $1$ は $k \mapsto c(P _ k ^ {\ast})$ が下に凸であることを意味している。

#### 定理 $2$

$\displaystyle P ^ {\ast} \in \argmin _ {P \in \mathcal{P}} (c(P) + \lambda ^ {\ast} (\lVert P \rVert - d)) \land \lVert P \rVert = d$ となる $\lambda ^ {\ast} \in \mathbb{Z}, P ^ {\ast} \in \mathcal{P}$ が存在する。

##### 証明

補題 $1$ を用いて、$- (c(P _ {d + 1} ^ {\ast}) - c(P _ d ^ {\ast})) \leq \lambda ^ {\ast} \leq - (c(P _ d ^ {\ast}) - c(P _ {d - 1} ^ {\ast}))$ となるように $\lambda ^ {\ast}$ を取る。
$\forall k.\ c (P _ k ^ {\ast}) + \lambda ^ {\ast} (k - d) \geq c (P _ d ^ {\ast})$ を示せば、$\displaystyle P _ d ^ {\ast} \in \argmin _ {P \in \mathcal{P}} (c(P) + \lambda ^ {\ast} (\lVert P \rVert - d))$ であるから、$P ^ {\ast}$ として $P _ d ^ {\ast}$ を取ることができる。

-   $k \lt d$ の場合

    $$ \begin{align*}
      c (P _ k ^ {\ast}) + \lambda ^ {\ast} (k - d)
      & = c(P _ d ^ {\ast}) - \sum _ {i = k} ^ {d - 1} (c(P _ {i + 1} ^ {\ast}) - c(P _ i ^ {\ast})) + \lambda ^ {\ast} (k - d) \cr
      & \geq c(P _ d ^ {\ast}) - (c(P _ d ^ {\ast}) - c(P _ {d - 1} ^ {\ast})) (d - k) + \lambda ^ {\ast} (k - d) & & (\because \text{補題}\ 1) \cr
      & \geq c(P _ d ^ {\ast}) + \lambda ^ {\ast} (d - k) + \lambda ^ {\ast} (k - d) & & (\because \lambda ^ {\ast} \text{の定義}) \cr
      & = c (P _ d ^ {\ast})
    \end{align*} $$
-   $k \geq d$ の場合

    $$ \begin{align*}
      c(P _ k ^ {\ast}) + \lambda ^ {\ast} (k - d)
      & = c(P _ d ^ {\ast}) + \sum _ {i = d} ^ {k - 1} (c(P _ {i + 1} ^ {\ast}) - c(P _ i ^ {\ast})) + \lambda ^ {\ast} (k - d) \cr
      & \geq c(P _ d ^ {\ast}) + (c(P _ {d + 1} ^ {\ast}) - c(P _ d ^ {\ast})) (k - d) + \lambda ^ {\ast} (k - d) & & (\because \text{補題}\ 1) \cr
      & \geq c(P _ d ^ {\ast}) - \lambda ^ {\ast}(k - d) + \lambda ^ {\ast} (k - d) & & (\because \lambda ^ {\ast} \text{の定義}) \cr
      & = c (P _ d ^ {\ast})
    \end{align*} $$

$\blacksquare$

#### 系 $3$ (強双対性)

$$
  \min _ {P \in \mathcal{P}, \lVert P \rVert = d} c(P) = \max _ {\lambda \in \mathbb{Z}} \min _ {P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))
$$

## アルゴリズム

ラグランジュ双対問題 $\displaystyle \max _ {\lambda \in \mathbb{Z}} \min _ {P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))$ を解く。
$\displaystyle L: \lambda \mapsto \min _ {P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d))$ は $1$ 次関数群の $\min$ であるから、上に凸である。したがって、$L$ の最大値は三分探索を用いて計算することができる。
系 $3$ より、得られた $L$ の最大値が、求める出力 $\displaystyle \min _ {P \in \mathcal{P}, \lVert P \rVert = d} c(P)$ である。

残る問題は $\lambda$ が与えられたとき $L(\lambda)$ を計算することである。
辺重み $c _ {\lambda} : E \to \mathbb{Z}$ を $c _ {\lambda} (e) = c(e) + \lambda$ によって定義する。
すなわち、$c _ {\lambda}$ は全ての辺の重みを $c$ と比べて $\lambda$ 大きくした重みである。
すると、以下のように変形できる。
$$ \begin{align*}
  L (\lambda)
  & = \min _ {P \in \mathcal{P}} (c(P) + \lambda (\lVert P \rVert - d)) \cr
  & = \min _ {P \in \mathcal{P}} (c (P) + \lambda \lVert P \rVert - \lambda d) \cr
  & = - \lambda d + \min _ {P \in \mathcal{P}} c _ {\lambda} (P)
\end{align*} $$
よって、$c _ {\lambda}$ についての最短路長を計算することで $L(\lambda)$ の値を得ることができる。

$c$ が Monge であるから、$c _ {\lambda}$ もまた Monge である。
辺の重みが Monge 性を満たす完全 DAG の最短路の計算は LARSCH Algorithm[^LARSCH] を用いて $\Theta (N)$ で行うことができる。
Aliens[^Aliens] では $c$ の性質が Monge よりさらに良く、Convex Hull Trick を用いることで同じく $\Theta (N)$ で最短路を計算することができる。

$\displaystyle \lambda = - 3 \max _ {e \in E} \lvert c(e) \rvert$ とすると辺を $N - 1$ 本含むパスが最短となる。
$\lambda$ をそれ以上小さくすると $L(\lambda)$ は単調減少するため、$\displaystyle - 3 \max _ {e \in E} \lvert c(e) \rvert$ は三分探索の下界として用いることができる。
同様に、$\displaystyle 3 \max _ {e \in E} \lvert c(e) \rvert$ を上界に用いることができる。


時間計算量は全体で $\Theta (N \log (\max _ {e \in E} \lvert c(e) \rvert))$ となる。

## その他

-    $c(e)$ を全ての $e \in E$ について入力すると $\Theta(N ^ 2)$ となってしまうため、実際には $i, j$ を与えたときに $c(i, j)$ が $\mathrm{O}(1)$ で計算できると仮定して、アルゴリズムの時間計算量を評価している。
-    $c _ {\lambda} (P)$ を最小化する $P$ についての $\lVert P   \rVert$ が $\lambda$ について単調減少である[^tie-breaking] ことに着目し、丁度 $\lVert P \rVert = d$ となるような $\lambda$ を二分探索で求めるという方法も存在する。これは $L$ の最大化を傾きについての二部探索で行うことと概ね等価なアルゴリズムとなる。

-   $d$ 本以下の辺を使う条件下の最短路長も計算することができる。補題 $1$ より、$k \mapsto c(P _ k ^ {\ast})$ は下に凸である。したがって、$d$ 本以下の辺を使う条件下の最短路になり得るのは、条件なしでの最短路と $P _ d ^ {\ast}$ のみである。$d$ 本以上の辺を使う場合も同様に計算できる。

## 参考文献

-   Bein, W. W., Larmore, L. L., & Park, J. K. (1992). The d-edge shortest-path problem for a Monge graph (No. SAND-92-1724C; CONF-930194-1). Sandia National Labs., Albuquerque, NM (United States).

-   [双対性. JOI春合宿 2018. 岩田 陽一 (NII)](https://www.slideshare.net/wata_orz/ss-91375739) <sup>[archive.org](https://web.archive.org/web/20201101134907/https://www.slideshare.net/wata_orz/ss-91375739)</sup>

## 注釈

[^Aliens]: [IOI 2016 Aliens](https://ioinformatics.org/files/ioi2016problem6.pdf) <sup>[archive.org](https://web.archive.org/web/20191021104945/https://ioinformatics.org/files/ioi2016problem6.pdf)</sup>
[^kort0n-alienDP]: <a class="handle">kort0n</a> によるツイート <https://twitter.com/kyort0n/status/1260986271314227206><sup>[archive.org](https://web.archive.org/web/20200514195641/https://twitter.com/kyort0n/status/1260986271314227206)</sup>
[^WQS-binary-search]: [DP optimization - WQS Binary Search Optimization &#124; A Simple Blog](https://robert1003.github.io/2020/02/26/dp-opt-wqs-binary-search.html) <sup>[archive.org](https://web.archive.org/web/20210326063417/https://robert1003.github.io/2020/02/26/dp-opt-wqs-binary-search.html)</sup>　<https://codeforces.com/blog/entry/49691?#comment-402636> <sup>[archive.org](https://web.archive.org/web/20210326064207/https://codeforces.com/blog/entry/49691)</sup>
[^lagrangian-penalty]: $\lambda (\lVert P \rVert - d)$ は負にもなり得るため、ペナルティとしての解釈が難しい部分もある。厳密な議論は式変形を参照せよ。
[^lagrangian-relaxation]: [ラグランジュ緩和問題 - 数理計画用語集](http://www.msi.co.jp/nuopt/glossary/term_c4995faa151e2d66d8ea36c8eaff94885d60c19f.html) <sup>[archive.org](https://web.archive.org/web/20200221035313/http://www.msi.co.jp/nuopt/glossary/term_c4995faa151e2d66d8ea36c8eaff94885d60c19f.html)</sup>
[^LARSCH]: Larmore, L. L., & Schieber, B. (1991). On-line dynamic programming with applications to the prediction of RNA secondary structure. Journal of Algorithms, 12(3), 490-515.
[^tie-breaking]: 厳密には、$c _ {\lambda} (P)$ を最小化する $P$ が複数存在した場合にどれを選ぶかによって、単調性が成り立たない場合もある。
