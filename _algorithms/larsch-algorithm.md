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

LARSCH algorithm は totally monotone な $H \times W$ generalized lower trianglar matrix に対してその各行の最小値を $\Theta(N)$ で計算するアルゴリズムである。
SMAWK algorithm の状況と異なり、最小値の計算が終わるまで値が分からない成分が存在しても良いという特徴がある。

## generalized lower trianglar matrix

部分的に定義された $H \times W$ 行列 $f$ が generalized lower trianglar matrix であるとは、整数列 $0 \lt L _ 0 \leq L _ 1 \leq \dots \leq L _ {H - 1} = W$ が存在して、$0 \leq x \lt L _ y$ のときかつその時に限り $f(y, x)$ が定義されることをいう。
例えば、対角部分を含む下三角部分のみが定義された正方行列は generalized lower trianglar matrix である。

## 詳細

相互再帰的な $2$ 種類の機械 $\texttt{ReduceRow}$ と $\texttt{ReduceColumn}$ を考える。
これらの機械 $\mathcal{A}$ は行集合 $R _ {\mathcal{A}} \subseteq H$ 及び列集合 $C _ {\mathcal{A}} \subseteq W$ を管理し、$f$ を $R _ {\mathcal{A}} \times C _ {\mathcal{A}}$ 部分に制限した行列に対する行最小値問題を解く。
$R _ {\mathcal{A}}$ は機械 $\mathcal{A}$ が構成されたときに与えられ不変であるが、$C _ {\mathcal{A}}$ は昇順に追加されていく。

$\mathcal{A}$ をこれらいずれかの機械としたとき、以下の操作を考える。

-   $\texttt{add\textunderscore column} (\mathcal{A}, c)$

    $C _ {\mathcal{A}}$ に列 $c$ を追加する。

-   $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$

    $\displaystyle \argmin _ {x \in C _ {\mathcal{A}}} f(y, x)$ を計算する。
    $C _ {\mathcal{A}}$ は呼び出し時点での値である。
    $y \in R _ {\mathcal{A}}$ かつ $y$ 昇順に呼ばれることが保証される。

### $\texttt{ReduceRow}$

$\mathcal{A}$ を $\texttt{ReduceRow}$ とし、$R _ {\mathcal{A}}$ の元を昇順に並べた列を  $( r _ 0, r _ 1, \dots )$ とする。
$\texttt{ReduceColumn}\ \mathcal{B}$ を構成し、$R _ {\mathcal{B}} \coloneqq \lbrace r _ i \mid i \equiv 1 \pmod 2 \rbrace$ とする。
各関数の内容は以下のようになる。

-   $\texttt{add\textunderscore column} (\mathcal{A} , c)$

    $C _ {\mathcal{A}} \leftarrow C _ {\mathcal{A}} \cup \lbrace c \rbrace$ と更新する。
    $\texttt{add\textunderscore column} (\mathcal{B}, c)$ を呼び出す。

-   $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$

    $r _ i = y$ を満たす $i$ をとる。

    -   $i$ が偶数のとき

        行 $r _ i$ は $R _ {\mathcal{B}}$ に含まれないことに注意せよ。
        $k _ p$ を $\texttt{get\textunderscore argmin} (\mathcal{A}, r _ {i - 1})$ が呼び出されたときの結果、すなわち $C ^ {\prime}$ を当時の $C _ {\mathcal{A}}$ として $\displaystyle \argmin _ {x \in C ^ {\prime}} f(r _ {i - 1}, x)$ とする。
        また、$\texttt{get\textunderscore argmin} (\mathcal{B}, r _ {i + 1})$ を呼び出し、得た値を $k _ s$ とする。
        totally monotone 性から、$\displaystyle k _ p \leq \argmin _ {x \in C _ {\mathcal{A}}} f(r _ i, x) \leq k _ s$ である。
        この範囲の列を全て調べて求める値を計算する。


    -   $i$ が奇数のとき

        行 $r _ i$ は $R _ {\mathcal{B}}$ に含まれることに注意せよ。
        $\texttt{get\textunderscore argmin} (\mathcal{A}, r _ {i - 1})$ の呼び出しの際に $\texttt{get\textunderscore argmin} (\mathcal{B}, r _ i) \eqqcolon k$ が既に計算されている。
        $\texttt{get\textunderscore argmin} (\mathcal{A}, r _ {i - 1})$ の呼び出しから $\texttt{get\textunderscore argmin} (\mathcal{A}, r _ i)$ の呼び出しの間に $C _ {\mathcal{A}}$ に追加された行全体を $\Delta C$ とすれば、$\displaystyle \argmin _ {x \in C _ {\mathcal{A}}} f(r _ i, x) \in \lbrace k \rbrace \cup \Delta C$ である。
        これらの列を全て調べて求める値を計算する


### $\texttt{ReduceColumn}$

$\mathcal{A}$ を $\texttt{ReduceColumn}$ とし、$R _ {\mathcal{A}}$ の元を昇順に並べた列を  $( r _ 0, r _ 1, \dots )$ とする。
$\texttt{ReduceRow}\ \mathcal{B}$ を構成し、$R _ {\mathcal{B}} \coloneqq R _ {\mathcal{A}}$ とする。

$C _ {\mathcal{B}}$ に追加する列の候補 $T _ {\mathcal{A}}$ を管理する。
最初、$T _ {\mathcal{A}} = \emptyset$ である。
各関数の内容は以下のようになる。

-   $\texttt{add\textunderscore column} (\mathcal{A}, c)$

    $C _ {\mathcal{A}} \leftarrow C _ {\mathcal{A}} \cup \lbrace c \rbrace$ と更新する。
    $s \coloneqq \lvert T _ {\mathcal{A}} \rvert$、$T _ {\mathcal{A}}$ に含まれる最右の列を $t$ とする。
    $f(r _ s, t) \gt f(r _ s, c)$ ならば $T _ {\mathcal{A}}$ から $t$ を削除する。
    これを $f(r _ s, c)$ が未定義になるか $f(r _ s, t) \leq f(r _ s, c)$ となるまで繰り返す。
    $\lvert T _ {\mathcal{A}} \rvert \lt \lvert R _ {\mathcal{A}} \rvert$ ならば $T _ {\mathcal{A}}$ に $c$ を追加する。

    この過程で $T _ {\mathcal{A}}$ から削除された列が $\argmin$ になり得ないことは、SMAWK algorithm と全く同様に示される。

-   $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$

    $r _ i = y$ を満たす $i$ をとる。

    $T _ {\mathcal{A}}$ の左から $i$ 個の列は、もう $\texttt{add\textunderscore column}$ の操作で削除されることが決してない。
    したがって、これらの列のうちまだ $C _ {\mathcal{B}}$ に追加されていないもの全てを $\texttt{add\textunderscore column} (\mathcal{B}, \ast ) $ を呼び出して追加する。
    今 $\displaystyle \argmin _ {x \in C _ {\mathcal{A}}} f(y, x)$ になり得る列は全て $C _ {\mathcal{B}}$ に含まれるため、$\texttt{get\textunderscore argmin} (\mathcal{B}, y)$ を呼び出し、求める値を得る。

$R _ {\mathcal{A}} = \emptyset$ であるような機械の $\texttt{get\textunderscore argmin}$ の処理は明らかであるから、その場合は再帰的に機械を構成せず打ち切る。

これらの機械を用いて、元の問題は以下のように解くことができる。

-   $\texttt{ReduceRow}\ \mathcal{A}$ を構成し、$R _ \mathcal{A} \coloneqq H$ とする。
-   $y = 0, 1, \dots, H - 1$ の順に以下の操作を行う。
    -   $x = L _ {y - 1}, L _ {y - 1} + 1, \dots, L _ y - 1$ の順に $\texttt{add\textunderscore column} (\mathcal{A}, x)$ を呼び出す。
    -   $\texttt{get\textunderscore argmin} (\mathcal{A}, y)$ を $\displaystyle \argmin _ {x} f(y, x)$ として報告する。

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
