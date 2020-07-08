---
layout: entry
author: kimiyuki
reviewers:
date: 2020-07-09T00:00:00+09:00
updated_at:
tags: algorithm montgomery-reduction montgomery-multiplication
algorithm:
  input: 剰余環の要素 $a, b \in \mathbb{Z}/N\mathbb{Z}$
  output: 積 $ab$
  time_complexity: 設定に依存する
  space_complexity:
  aliases:
description: Montgomery 乗算は、剰余環 $\mathbb{Z}/N\mathbb{Z}$ での乗算を高速に行うためのテクニックである。
---

# Montgomery乗算

## Montgomery reduction

Montgomery reduction は、剰余環上での定数による除算を高速に行なうためのテクニックである。
具体的には、互いに素な正整数 $R, N$ が固定されているとき、与えられた整数 $a$ に対して $b \equiv a \cdot R^{-1} \pmod{N}$ な整数 $b$ (ただし $0 \le b \lt N$) を求める。高速化のために $N \lt R$ でかつ $R$ での除算と剰余が速いこと ($R$ が $2$ 冪など) と $0 \le a \lt RN$ であることを仮定する。

流れとしては、まず整数環上での定数による除算に帰着させ、その後 $N$ での剰余を $R$ での剰余に置き換える。
具体的な式としては $b' = (a + (a N' \bmod R) N) / R$ とおいて $b = b'$ または $b = b' - N$ が答えである。

計算量については、ワードサイズに収まる範囲で考えているなら、$O(\log N)$ だったものが $O(1)$ になる。
$2^k$ bit の整数の加算に $O(k)$ かつ乗算に $O(k \log k)$ かかる設定で考えているなら、$O(k \log k \log N)$ あるいはこれより遅かったものが $O(k \log k)$ に落ちる。

### 剰余環上の定数除算から整数環上の定数除算への帰着

互いに素な正整数 $R, N$ が固定されており、整数 $a$ が与えられたとする。
$N' \equiv (-N)^{-1} \pmod{R}$ となるような整数 $N'$ (ただし $0 \le N' \lt R$) を事前に計算しておく。
整数 $t = (a + a N' N)$ を考える。この $t$ は $t \equiv a \pmod{N}$ と $t \equiv 0 \pmod{R}$ を共に満たす。
$t$ は $R$ の倍数なので整数の除算を用いて書かれる整数 $b = t/R$ が存在し、これは式 $b \equiv a \cdot R^{-1} \pmod{N}$ を満たす。よって $b \bmod N$ が目的の整数である。

さてこの整数 $b \bmod N$ を実際に計算することを考えよう。
整数 $N'$ を事前に計算しておき、$t = a + a N' N$ を計算し、$b = t/R$ を計算し、そして $b \bmod N$ を計算する。
剰余環上の除算は繰り返し二乗法や拡張 Euclid の互除法を必要とし $O(\log N)$ かかるが、整数上の除算 $b = t/R$ はこれに比べて速い。
他には整数上の乗算と剰余のみであり、剰余環上の除算や剰余を回避できた。

### $R$ の仮定を用いての高速化

ここまでで分かったことは、以下の演算により剰余環上の除算ができるということである。

-   整数上の加算を数回
-   整数上の乗算を数回
-   整数上の $R$ での除算を $1$ 回
-   整数上の $N$ での剰余を $1$ 回

さらに演算の強度を減らしていく。ただしここで、$N \lt R$ であることと $0 \le a \lt RN$ であることを仮定する。

まず $t$ について準備する。
$t = a + a N' N$ でなく $t = a + (a N' \bmod R) N$ で置き換えることとする。
これは $t \equiv a \pmod{N}$ であることを壊さずに、$t$ の最大値を $t = a + (aN' \bmod R)N \le RN + RN = 2RN$ と抑えられる。

次に $b \bmod N$ を変形する。
$t$ の工夫の結果である $t \lt 2RN$ の制約および $R$ の仮定 $N \le R$ によって $b = t/R \lt 2RN/R = 2N$ が成り立つ。
すると、$b \bmod N$ をそのまま $N$ を剰余で取るのでなく、条件分岐と減算によって $b \bmod N = \begin{cases} b & (b \lt N) \\ b - N & (\text{otherwise}) \end{cases}$ と書くことができる。

よって $N \lt R$ の仮定によって、演算を以下の形にまで減らせた。

-   整数上の加算を数回
-   整数上の乗算を数回
-   整数上の $R$ での除算を $1$ 回
-   整数上の $R$ での剰余を $1$ 回

ここでさらに $R$ での除算と剰余が速いことを仮定すれば、十分に速い演算だけで剰余環上の除算ができたことになる。
この仮定は、具体的には、$R$ が $2$ 冪や $10$ 冪であり除算や剰余を bit 演算など桁ごとで表現できることだと考えてよく、妥当な仮定である。

手順まとめ:

1.  事前計算: $N' \equiv (-N)^{-1} \pmod{R}$
1.  $a N' \bmod R$ を求める
1.  $t = a + (a N' \bmod R) N$ を求める
1.  $b = t/R$ を求める
1.  $b \bmod N = \begin{cases} b & (b \lt N) \\ b - N & (\text{otherwise}) \end{cases}$ を求める

## Montgomery 乗算

Montgomery 乗算は、剰余環 $\mathbb{Z}/N\mathbb{Z}$ での乗算を高速に行うためのテクニックである。
同型な環 $M$ であってその乗算に Montgomery reduction を用いられるようなものを用いる。

### $\mathbb{Z}/N\mathbb{Z}$ と同型な環 $M$

剰余環 $\mathbb{Z}/N\mathbb{Z} = (\lbrace 0, 1, 2, \dots, N - 1 \rbrace, +, \cdot, 0, 1)$ を考える。
ただし、以下でも演算はすべて $\bmod N$ を陽に書くため、$\mathbb{Z}/N\mathbb{Z}$ の演算は正確には $\lambda xy. (x + y) \bmod N$ と $\lambda xy. (x \cdot y) \bmod N$ であることに注意したい。
$R$ を $N$ と互いに素な正整数とする。$R \lt N$ である必要はない。
$R' \equiv R^{-1} \pmod{N}$ な整数 $R'$ (ただし $0 \le R' \lt N$) を用意しておく。
ただし、$R'$ は「$b \equiv a \cdot R^{-1} \pmod{N}$ と $0 \le c \lt N$ を満たすような整数 $c$」という言い方を避けるための記号であり、これを事前に計算しておくことは重要でない。

剰余環 $\mathbb{Z}/N\mathbb{Z}$ の乗法を $$a \otimes b = a b R' \bmod N$$ で置き換えて得られる環 $M = (\lbrace 0, 1, 2, \dots, N - 1 \rbrace, +, \otimes, 0, R \bmod N)$ を考える。
この $M$ は $\mathbb{Z}/N\mathbb{Z}$ と同型であることが示せる。
これは関数 $\overline{-} : \mathbb{Z}/N\mathbb{Z} \to M$ を $$\overline{a} = Ra \bmod N$$ で定義すると、以下のすべてが成り立つことによる。

-   $\overline{0} = 0$
-   $\overline{1} = R \bmod N$
-   $\overline{(a + b) \bmod N} = R \cdot (a + b) \bmod N = (Ra + Rb) \bmod N = (\overline{a} + \overline{b}) \bmod N$
-   $\overline{(a \cdot b) \bmod N} = R a b \bmod N = Ra \cdot Rb \cdot R' \bmod N = \overline{a} \otimes \overline{b}$
-   逆関数が構成できるため $\overline{-}$ は全単射

### $M$ の演算や $M$ との相互変換に Montgomery reduction が使えることについて

$N \lt R$ だと仮定すれば、このような可換環 $M$ での演算は速い。
加法 $\overline{a} + \overline{b}$ は剰余環の演算と同じなためもとから速い。
乗法 $\overline{a} \otimes \overline{b}$ については Montgomery reduction をする。
$\overline{a} \otimes \overline{b} = \overline{a} \cdot \overline{b} \cdot R' \bmod N$ であった。
整数として $\overline{a} \cdot \overline{b} \lt N^2 \lt NR$ が成り立つので Montgomery reduction が可能である。
これにより $(\overline{a} \cdot \overline{b}) \cdot R' \bmod N$ の値が得られる。

この他に $x$ と $\overline{x}$ との間の相互変換が速い必要がある。
$\overline{x}$ から $x = \overline{x} \cdot R' \bmod N$ を得るには、単に Montgomery reduction をすればよい。
$x$ から $\overline{x} = x \cdot R \bmod N$ を得るには、事前に $R_2 = R^2 \bmod N$ な整数 $R_2$ (ただし $0 \le R_2 \lt N$) を求めておき、これを使った $\overline{x} = (R_2 x) \cdot R' \bmod N$ に対しての Montgomery reduction をすればよい。整数として $R_2 x \lt N^2$ であるのでこれは可能である。
