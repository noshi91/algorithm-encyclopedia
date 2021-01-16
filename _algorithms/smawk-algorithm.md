---
layout: entry
author: kimiyuki
reviewers:
date: 2020-07-11T00:00:00+09:00
updated_at:
tags: algorithm smawk-algorithm monotone-minima
algorithm:
  input: totally monotone な $H \times W$ 行列 $f$
  output: 各行 $y$ に対し最小値の位置 $x \in \mathrm{argmin} _ x f(y, x)$
  time_complexity: $O(H + W)$
  space_complexity:
  aliases: ["TM minima", "totally monotone minima"]
description: SMAWK algorithm とは、totally monotone な $H \times W$ 行列に対しその各行の最小値を $O(H + W)$ で求めるアルゴリズムである。
draft: true
draft_urls: "https://topcoder-g-hatena-ne-jp.jag-icpc.org/spaghetti_source/20120923/1348327542.html"
---

# SMAWK algorithm

## 説明

### 概要

SMAWK algorithm とは、totally monotone な $H \times W$ 行列 $f$ に対し、それぞれの行 $y$ の最小値の位置 (のひとつ) $x \in \mathrm{argmin} _ x f(y, x)$ をまとめて効率よく求めるテクである。愚直には行列全体をなめて $O(HW)$ であるが、これを $O(H + W)$ で行う。 仮定を強めることで monotone minima をより高速にしたようなアルゴリズムである。

### 準備

totally monotone の定義について。$H, W$ は自然数とし $A$ は全順序集合とする。$H \times W$ の行列 $f : H \times W \to A$ が totally monotone であるとは、$f$ の任意の $2 \times 2$ 部分行列 $\begin{pmatrix} a & b \cr c & d \end{pmatrix}$ が $c \lt d$ ならば $a \lt b$ を満たしかつ $c = d$ ならば $a \le b$ を満たすこと。
この定義は次と等しい: $f$ の任意の部分行列が monotone であること。
また、monotone の定義については [[/monotone minima]] を参照してほしい。

totally monotone の性質について確認しておく。
totally でない monotone であれば言えることとして「$x \in \mathrm{argmin} _ x f(y, x)$ ならば、座標 $(y, x)$ の右上 ($y \le y'$ かつ $x' \le x$ かつ $(y', x') \ne (y, x)$ な位置 $(y', x')$) と左下 (同様) には最小値はないと仮定してよい」がある。
totally monotone であればこれをさらに強めて「$x \lt x'$ な $x'$ が存在し $f(y, x) \le f(y, x')$ ならば、座標 $(y, x)$ の右上 ($y \le y'$ かつ $x' \le x$ かつ $(y', x') \ne (y, x)$ な位置 $(y', x')$) には最小値はないと仮定してよい」および「$x' \lt x$ な $x'$ が存在し $f(y, x - 1) \ge f(y, x)$ ならば、座標 $(y, x)$ の左下には最小値はないと仮定してよい」が言える。
この性質は後述の Reduce ステップと Interpolate ステップで用いられる。
また、monotone では任意の行を削除しても monotone が保たれるが、列を削除すると monotone でなくなる可能性があった。一方で、totally monotone は任意の行や列を削除しても totally monotone が保たれる。
この性質は後述の Recursion ステップで用いられる。

### 詳細

SMAWK algorithm の具体的な手順は以下のようになる。

1.  入力
    1.  totally monotone な $H \times W$ 行列 $f$ を (暗な形で) 入力として受けとる。
1.  Initialize
    1.  行の集合 $\mathrm{row} = \lbrace 0, 1, \dots, H - 1 \rbrace$ を用意する。
    1.  列の集合 $\mathrm{col} = \lbrace 0, 1, \dots, W - 1 \rbrace$ を用意する。
1.  Reduce
    1.  行の集合 $\mathrm{row}$ のうちから偶数行目だけを選んで、$\mathrm{row}' \subseteq \mathrm{row}$ を得る。このとき $vert \mathrm{row}' \vert \le H/2$ である。
    1.  列の集合 $\mathrm{col}$ のうちから最小値を含まないと仮定してよい列を削除して、残された列の集合 $\mathrm{col}' \subseteq \mathrm{col}$ を得る。このとき $\vert \mathrm{col}' \vert \le H$ である。(詳細は後述)
1.  Recursion
    1.  行列 $f$ を $\mathrm{row}'$ に含まれる行と $\mathrm{col}'$ に含まれる列に制限してできる行列を $f'$ とする。totally monotone の性質から、この $f'$ も totally monotone である。これに対し再帰的に最小値の位置をすべて求める。
1.  Interpolate
    1.  集合 $\mathrm{row} \setminus \mathrm{row}'$ に含まれるそれぞれの行 $y$ について、その上下の行 $y \pm 1$ の最小値の位置を参照しながら、行 $y$ の最小値の位置 $x \in \mathrm{argmin} _ x f(y, x)$ を求める。(詳細は後述)
1.  出力
    1.  $H$ 個の行それぞれの最小値の位置を出力として返す。

Reduce ステップについて。
このステップでは、最小値を含む可能性のある列を高々 $H$ 個選んで $\mathrm{col}'$ とする。
具体的には次のような手順になる:

1.  $y \gets 0$ および $S_0 \gets 0$ と初期化する。
1.  $x \in \lbrace 1, \dots, W - 1 \rbrace$ について昇順に以下を行う。
    1.  $f(y, S_y)$ と $f(y, x)$ 比較して、その結果が
        -   $f(y, S_y) \ge f(y, x)$ ならば、$S_y \gets x$ と更新する。
        -   $f(y, S_y) \lt f(y, x)$ ならば、$y \gets y + 1$ と更新し、$y = H$ になれば $S_y \gets x$ と初期化する。
1.  $\mathrm{col}' = \lbrace S_y \mid y \rbrace$ とする。

こうして得られる $\mathrm{col}'$ には「$\mathrm{col}'$ に含まれない列には最小値はない (と見なせる)」という性質が成り立つ。
なぜなら、ループの過程においてある列が削除されるのはその列が列 $S_y$ であり、$f(y, S_y) \ge f(y, x)$ が見つかったときのみであり、これについて以下が言えるためである。

-   $(y, S_y) \ge f(y, x)$ であるために、列 $S_y$ は $y$ 行目の最小値を含まない (見なしてよい)。
-   $(y, S_y) \ge f(y, x)$ と totally monotone 性から、列 $S_y$ は $y \lt y'$ な $y'$ 行目の最小値を含まない。
-   $y$ の更新のされ方と totally monotone 性から「$S _ {y+1} = x$ ならば、$x \lt x'$ な $x'$ 列目は $y$ 行目の最小値を含まない」が常に言えるため、列 $S_y$ は $y \lt y'$ な $y'$ 行目の最小値を含まない。


Interpolate ステップについて。
行 $y - 1$ の最小値の位置 (のひとつ) $x _ {y-1} \in \mathrm{argmin} _ x f(y, x)$ と行 $y + 1$ の最小値の位置 (のひとつ) $x _ {y-1} \in \mathrm{argmin} _ x f(y, x)$ が分かっているとき、行 $y$ の最小値の位置 (のひとつ) $x _ y \in \mathrm{argmin} _ x f(y, x)$ を求めることを考える。
(totally) monotone という仮定から、$x _ {y-1} \le x _ y \le x _ {y+1}$ であると仮定してよい。これにより $f(y, x _ {y-1}), f(y, x _ {y - 1} + 1), \dots, f(y, x _ {y + 1})$ のみを調べれば最小値の位置 $x_y$ が見付かる。
最小値の位置が分かっていないすべての $y$ についてこれを行なうことを考えると、調べる必要があるのはたとえば $H$ が偶数なら $f(1, x_0), f(1, x_0 + 1), \dots, f(1, x_2); f(3, x_2), f(3, x_2 + 1), \dots, f(3, x_4); \dots; f(H-1, x _ {H-2}), f(H-1, x _ {H-2} + 1), \dots, f(H-1, W-1)$ であり、調べる必要がある位置は $H + W$ 個で抑えられる。
よって、偶数行目の最小値の位置から奇数行目の最小値の位置を $O(H + W)$ で復元できる。

計算量について。
Reduce と Interpolate にそれぞれ $O(W)$ と $O(H + W)$ かかり、$H/2 \times H$ の大きさの行列に再帰をする。
$(H + 2W) + (H/2 + 2H) + (H/4 + H) + (H/8 + H/2) + \dots = 2W + (H + H/2 + H/4 + H/8 + \dots) + (2H + H + H/2 + \dots) = 2W + 6H$ のように考えれば、計算量は全体で $O(H + W)$ である。

## その他

-   行列 $f$ が陰に保持されるべきことに注意したい。もし陽に保持すると、それだけで空間計算量 $O(HW)$ かかり、自動的に時間計算量も $O(HW)$ になってしまうためである。
-   Monge ならば totally monotone である。
-   totally monotone ならば monotone である。多少は遅くなるが monotone minima で SMAWK algorithm を代用できる。

## 参考文献

-   [Totally Monotone Matrix Searching (SMAWK algorithm) - 週刊 spaghetti_source - TopCoder部](https://topcoder-g-hatena-ne-jp.jag-icpc.org/spaghetti_source/20120923/1348327542.html)
    -   信頼できる解説記事 (日本語)
-   <http://web.cs.unlv.edu/larmore/Courses/CSC477/monge.pdf>
    -   具体例を通して説明されており分かりやすい
-   A. Aggarwal, M. M. Klawe, S. Moran, P. W. Shor, and R. E. Wilber, “Geometric Applications of a Matrix-Searching Algorithm,” Algorithmica, vol. 2, pp. 195–208, Jan. 1987, doi: 10.1007/BF01840359.
    -   SMAWK algorithm が提案された論文
