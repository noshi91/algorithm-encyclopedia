---
layout: entry
changelog:
  - summary: 記事作成
    authors: noshi91
    reviewers:
    date: 2021-04-07T19:24:14+09:00
algorithm:
  input: totally monotone な $H \times W$ generalized lower trianglar matrix $f$
  output: >
    $y$ の昇順に $x ^ {\ast} \in \argmin _ x f(y, x)$。
    ただし第 $x$ 列の成分は、その列の成分のいずれかが $\argmin$ の定義に必要になったときに計算されていればよい。
  time_complexity: $\Theta(N)$
  space_complexity: $\Theta(N)$
  aliases: []
  level: red
description: >
    LARSCH algorithm は totally monotone な $H \times W$ generalized lower trianglar matrix に対してその各行の最小値を $\Theta(N)$ で計算するアルゴリズムである。
    SMAWK algorithm の状況と異なり、最小値の計算が終わるまで値が分からない成分が存在しても良いという特徴がある。
---

# LARSCH algorithm

## 概要

## generalized lower trianglar matrix

部分的に定義された $H \times W$ 行列 $f$ が generalized lower trianglar matrix であるとは、整数列 $0 \leq C _ 0 \leq \dots \leq C _ {H - 1} = W - 1$ が存在して $0 \leq x \leq C _ y$ のときかつその時に限り $f(y, x)$ が定義されることをいう。

## 詳細

より小さいインスタンスへの帰着を利用した、相互再帰的な $2$ 種類の機械 $\texttt{ReduceRow}$ と $\texttt{ReduceColumn}$ を考える。
これらは以下の機能を持つ。

-   $\texttt{add\_column} (c)$

    列 $c$ を追加する。

-   $\texttt{get\_argmin} (y)$

    呼び出された時点で追加済の列について、$\argmin _ x f(y, x)$ を計算する。
    これは $y = 0, 1, \dots, H - 1$ の順に呼ばれることが保証される。

### $\texttt{ReduceRow}$

$\texttt{ReduceRow}$ は $f$ の $\lfloor H / 2 \rfloor \times M$ 部分行列をとり、そのインスタンスを解く $\texttt{ReduceColumn}\ A$ を作成する。
各関数の内容は以下のようになる。

-   $\texttt{add\_column} (c)$
-   $\texttt{add \_ column} (c)$
-   $\texttt{add_column} (c)$
-   $\texttt{add _ column} (c)$

    $c$ を考慮の対象に追加したのち、$A$ に $\texttt{add\_column} (c)$ を適用する。

-   $\texttt{get\_argmin} (y)$

    -   $y$ が偶数のとき

        行 $y$ は $\mathscr{A}$ に含まれないことに注意せよ。
        行 $y - 1$ 及び $y + 1$ の $\argmin$ の位置の間だけを考えればよい。
        $\argmin _ x f(y - 1, x)$ は既に求まっている。
        $A$ に対して $\texttt{get\_argmin} (y / 2)$ を適用し、$k$ とする。
        $k$ は $\argmin _ x f(y + 1, x)$ とは必ずしも一致しないが、それでもなお $\argmin _ x f(y ,x) \leq k$ は成立するため、利用することができる。

    -   $y$ が奇数のとき

        行 $y$ は $A$ に含まれていることに注意せよ。
        $\texttt{get\_argmin} (y - 1)$ の呼び出しで $A$ に対する $\texttt{get\_argmin} ((y - 1) / 2) \eqqcolon k$ が既に計算されている。
        $\texttt{get\_argmin} (y - 1)$ の呼び出しから $\texttt{get\_argmin} (y)$ の呼び出しの間に追加された行全体を $c$ とすれば、$\argmin _ x f(y, x) \in \lbrace k \rbrace \cup c$ である。
        これらを全て調べて、$\argmin _ x f(y, x)$ を得る。


### $\texttt{ReduceColumn}$

$\texttt{ReduceColumn}$ は $f$ の $H \times M ^ {\prime}$ 部分行列をとり、そのインスタンスを解く $\texttt{ReduceRow}\ A$ を作成する。
$M ^ {\prime} \leq H$ を満たす。

$A$ に追加する列の候補 $C$ を管理する。
最初、$C = \emptyset$ である。
各関数の内容は以下のようになる。

-   $\texttt{add\_column} (c)$

    $s \coloneqq \lvert C \rvert$ とする。
    $C$ の最右列を $t$ とする。
    $f(s, t) \gt f(s, c)$ ならば $C$ から $t$ を削除する。
    これを $f(s, t) \leq f(s, c)$ となるまで繰り返す。
    $C$ に $c$ を追加する。

-   $\texttt{get\_argmin} (y)$

    $C$ の最左 $y$ 個の列は、もう $\texttt{add\_column}$ の操作で削除されることが決してない。
    したがって、これらの列のうちまだ $A$ に追加されていないもの全てを $\texttt{add\_column}$ を呼び出して追加する。
    今 $\argmin _ x f(y, x)$ になり得る列は全て $A$ に追加されているため、$A$ に対して $\texttt{get\_argmin} (y)$ を呼び出せば、それが求める $\argmin _ x f(y, x)$ である。

## 参考文献

-   Larmore, L. L., & Schieber, B. (1991). On-line dynamic programming with applications to the prediction of RNA secondary structure. Journal of Algorithms, 12(3), 490-515.
    -   LARSCH algorithm が提案された論文。


## 関連項目

-   [SMAWK algorithm](/smawk-algorithm)
    -   LARSCH algorithm で用いられる考え方は SMAWK algorithm のものと類似している。
