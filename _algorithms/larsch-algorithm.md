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

部分的に定義された $H \times W$ 行列 $f$ が generalized lower trianglar matrix であるとは、整数列 $0 \lt L _ 0 \leq L _ 1 \leq \dots \leq L _ {H - 1} = W$ が存在して、$0 \leq x \lt L _ y$ のときかつその時に限り $f(y, x)$ が定義されることをいう。

## 詳細

相互再帰的な $2$ 種類の機械 $\texttt{ReduceRow}$ と $\texttt{ReduceColumn}$ を考える。
これらの機械は行集合 $R \subseteq H$ 及び列集合 $C \subseteq W$ を管理し、$f$ を $R \times C$ 部分に制限した行列に対する行最小値問題を解く。
$R$ は機械が構成されたときに与えられ不変であるが、$C$ は昇順に追加されていく。

$\mathcal{A}$ をこれらいずれかの機械としたとき、以下の操作を考える。

-   $\texttt{add\textunderscore column} (\mathcal{A}, c)$

    機械 $\mathcal{A}$ に列 $c$ を追加する。

-   $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$

    機械 $\mathcal{A}$ の管理するその時点の $C$ 内で、行 $y$ についての $\argmin$ を計算する。
    これは $y \in R$ かつ $y$ 昇順に呼ばれることが保証される。

### $\texttt{ReduceRow}$

$\mathcal{A}$ を $\texttt{ReduceRow}$ とする。
$R = \lbrace r _ 0, r _ 1, \dots, r _ {h - 1} \rbrace$ としたとき、行集合を $\lbrace r _ i \mid i \equiv 1 \pmod 2 \rbrace$ として $\texttt{ReduceColumn}$ $\mathcal{B}$ を作成する。
各関数の内容は以下のようになる。

-   $\texttt{add\textunderscore column} (\mathcal{A} , c)$

    $C \leftarrow C \cup \lbrace c \rbrace$ と更新する。
    $\texttt{add\textunderscore column} (\mathcal{B}, c)$ を呼び出す。

-   $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$

    $r _ i = y$ を満たす $i$ をとる。

    -   $i$ が偶数のとき

        行 $y$ は $\mathcal{B}$ に含まれないことに注意せよ。
        $k _ p$ を $\texttt{get\textunderscore argmin} (\mathcal{A}, r _ {i - 1})$ が呼び出されたときの結果、すなわち $C ^ {\prime}$ を当時の $C$ として $\argmin _ {x \in C ^ {\prime}} f(r _ {i - 1}, x)$ とする。
        また、$\texttt{get\textunderscore argmin} (\mathcal{B}, r _ {i + 1})$ を呼び出し、得た値を $k _ s$ とする。
        totally monotone 性から、$k _ p \leq \argmin _ {x \in C} f(r _ i, x) \leq k _ s$ である。
        したがって、この範囲の列を全て調べて求める値を計算する。
        

    -   $i$ が奇数のとき

        行 $y$ は $\mathcal{B}$ に含まれることに注意せよ。
        $\texttt{get\textunderscore argmin} (\mathcal{A}, r _ {i - 1})$ の呼び出しの際に $\texttt{get\textunderscore argmin} (\mathcal{B}, y) \eqqcolon k$ が既に計算されている。
        $\texttt{get\textunderscore argmin} (\mathcal{A}, r _ {i - 1})$ の呼び出しから $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$ の呼び出しの間に追加された行全体を $\Delta C$ とすれば、$\argmin _ {x \in C} f(y, x) \in \lbrace k \rbrace \cup \Delta C$ である。
        これらを全て調べて、$\argmin _ {x \in C} f(y, x)$ を得る。


### $\texttt{ReduceColumn}$

$\mathcal{A}$ を $\texttt{ReduceColumn}$ とする。
行集合を $R$ とする $\texttt{ReduceRow}$ を構成し、$\mathcal{B}$ とする。

$\mathcal{B}$ に追加する列の候補 $T$ を管理する。
最初、$T = \emptyset$ である。
各関数の内容は以下のようになる。

-   $\texttt{add\textunderscore column} (\mathcal{A}, c)$

    $C \leftarrow C \cup \lbrace c \rbrace$
    $s \coloneqq \lvert T \rvert$ とする。
    $T$ の最右列を $t$ とする。
    $f(s, t) \gt f(s, c)$ ならば $T$ から $t$ を削除する。
    これを $f(s, t) \leq f(s, c)$ となるまで繰り返す。
    $T$ に $c$ を追加する。

-   $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$

    $r _ i = y$ を満たす $i$ をとる。

    $T$ の最左 $i$ 個の列は、もう $\texttt{add\textunderscore column}$ の操作で削除されることが決してない。
    したがって、これらの列のうちまだ $\mathcal{B}$ に追加されていないもの全てを $\texttt{add\textunderscore column}$ を呼び出して追加する。
    今 $\argmin _ {x \in C} f(y, x)$ になり得る列は全て $\mathcal{B}$ に追加されているため、$\texttt{get\textunderscore argmin} (\mathcal{B}, y)$ が求める値である。

行集合 $R$ が空であるような機械の $\texttt{get\textunderscore argmin}$ の処理は明らかであるから、その場合は再帰的に機械を構成せず打ち切る。

### 時間計算量

$\texttt{ReduceRow}$ は $\lvert R \rvert$ が概ね半分になるような機械を再帰的に管理する。
一方で $\texttt{ReduceColumn}$ が管理する機械へは、$\texttt{add\textunderscore column}$ が高々 $\lvert R \rvert$ 回しか呼び出されない。
結果として $\lvert R \rvert$ と $\lvert C \rvert$ は再帰の度に指数的に小さくなり、全体の時間計算量は $\Theta (H + W)$ となる。

## 参考文献

-   Larmore, L. L., & Schieber, B. (1991). On-line dynamic programming with applications to the prediction of RNA secondary structure. Journal of Algorithms, 12(3), 490-515.
    -   LARSCH algorithm が提案された論文。


## 関連項目

-   [SMAWK algorithm](/smawk-algorithm)
    -   LARSCH algorithm で用いられる考え方は SMAWK algorithm のものと類似している。
