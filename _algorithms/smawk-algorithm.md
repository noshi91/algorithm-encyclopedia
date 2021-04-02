---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers: noshi91
    date: 2021-02-04T00:00:00+09:00
algorithm:
  input: totally monotone な $H \times W$ 行列 $f$
  output: それぞれの行 $y$ に対し最小値の位置 $x \in \mathrm{argmin} _ x f(y, x)$
  time_complexity: $O(H + W)$
  space_complexity:
  aliases: ["totally monotone minima", "TM minima"]
  level: orange
description: SMAWK algorithm とは、totally monotone な $H \times W$ 行列に対しその各行の最小値を $O(H + W)$ で求めるアルゴリズムである。
---

# SMAWK algorithm

## 説明

### 概要

SMAWK algorithm とは、totally monotone な $H \times W$ 行列 $f$ に対し、それぞれの行 $y$ の最小値の位置 (のひとつ) $x \in \mathrm{argmin} _ x f(y, x)$ をまとめて効率よく求めるアルゴリズムである。愚直には行列全体を走査して $O(HW)$ であるが、これを $O(H + W)$ で行う。仮定を強めることで monotone minima をより高速にしたようなアルゴリズムである。

入力となる行列のそれぞれの行は distinct (重複を持たない) だと仮定されることがあるが、この制約は取り除ける。ただし、ひとつの行に最小値が複数回出現する場合への注意が必要となる。
SMAWK algorithm はそれぞれの行 $y$ について最小値の位置 $x_y$ を出力するが、これを $(x_0, x_1, \dots, x _ {H-1})$ とならべた列は必ず広義単調増加となる。この性質はアルゴリズム自体の内部でも用いられる。

### totally monotone について

totally monotone の定義について。$H, W$ は自然数とし $A$ は全順序集合とする。$H \times W$ の行列 $f : H \times W \to A$ が totally monotone であるとは、$f$ の任意の $2 \times 2$ 部分行列 $\begin{pmatrix} a & b \cr c & d \end{pmatrix}$ が $c \lt d$ ならば $a \lt b$ を満たしかつ $c = d$ ならば $a \le b$ を満たすこと。

定義の対偶のようなものを考えると次が言える: $f$ の任意の $2 \times 2$ 部分行列 $\begin{pmatrix} a & b \cr c & d \end{pmatrix}$ が $a \gt b$ ならば $c \gt d$ を満たしかつ $a = b$ ならば $c \ge d$ を満たす。
また、totally monotone な行列は任意の行や列を削除しても totally monotone なままに保たれる。

totally monotone であることは $f$ の任意の部分行列が monotone であることと同値である。その自明な場合として、totally monotone な行列は monotone な行列でもあることが言える。

## その他

-   行列 $f$ が陰に保持されるべきことに注意したい。もし陽に保持すると、それだけで空間計算量 $\Theta(HW)$ かかり、自動的に時間計算量も $\Omega(HW)$ になってしまうためである。
-   Monge ならば totally monotone である。
-   totally monotone ならば monotone である。多少は遅くなるが monotone minima で SMAWK algorithm を代用できる。
-   行列の各行の要素が distinct だと仮定すれば細かい定義の問題を気にしなくてすむ。たとえば SMAWK が提案された 1986 年のプロシーディングでも簡単のためとして distinct を仮定した形の説明がなされている。
-   行列の各行の要素が distinct とは限らない場合の議論は面倒であり、totally monotone や monotone の定義にも揺れがでてくる。SMAWK が提案された 1987 年の論文では distinct を仮定しない形で説明がなされている。

## 参考文献

-   A Aggarwal, M Klawe, S Moran, P Shor, and R Wilber. 1986. Geometric applications of a matrix searching algorithm. In Proceedings of the second annual symposium on Computational geometry (SCG '86). Association for Computing Machinery, New York, NY, USA, 285–292. DOI:<https://doi.org/10.1145/10515.10546>
    -   1987 年の論文が発表される前にあった会議のプロシーディング
-   Aggarwal, A., Klawe, M.M., Moran, S. et al. Geometric applications of a matrix-searching algorithm. Algorithmica 2, 195–208 (1987). <https://doi.org/10.1007/BF01840359>
    -   SMAWK algorithm が提案された論文


## 関連項目

-   [Monotone minima](/monotone-minima)
    -   monotone minima は SMAWK algorithm の動作に必要な仮定を弱めたものになっている。totally monotone ではなく monotone のみを仮定して、各行の最小値の位置を $O(H + W \log H)$ で求める。

## 外部リンク

-   [Totally Monotone Matrix Searching (SMAWK algorithm) - 週刊 spaghetti_source - TopCoder部](https://topcoder-g-hatena-ne-jp.jag-icpc.org/spaghetti_source/20120923/1348327542.html)<sup>[archive.org](https://web.archive.org/web/20201231040117/https://topcoder-g-hatena-ne-jp.jag-icpc.org/spaghetti_source/20120923/1348327542.html)</sup>
    -   <a class="handle">tmaehara</a> による解説記事
-   <https://noshi91.github.io/Library/algorithm/smawk.cpp><sup>[archive.org](https://web.archive.org/web/20210128162854/https://noshi91.github.io/Library/algorithm/smawk.cpp)</sup>
    -   <a class="handle">noshi91</a> による実装例
-   <http://web.cs.unlv.edu/larmore/Courses/CSC477/monge.pdf><sup>[archive.org](https://web.archive.org/web/20210103162046/http://web.cs.unlv.edu/larmore/Courses/CSC477/monge.pdf)</sup>
    -   [Lawrence L. Larmore](https://en.wikipedia.org/wiki/Lawrence_L._Larmore) による解説 (英語)。具体例を通して説明されている。
-   <https://kmyk.github.io/monotone-matrix-visualizer/><sup>[archive.org](https://web.archive.org/web/20210402113454/https://kmyk.github.io/monotone-matrix-visualizer/)</sup>
    -   totally monotone な行列などを図示してくれるページ
