---
layout: entry
authors: kimiyuki
reviewers:
date: 2020-07-09T00:00:00+09:00
updated_at: 2021-01-29T00:00:00+09:00
tags: algorithm monotone-minima
algorithm:
  input: monotone な $H \times W$ 行列 $f$
  output: 各行 $y$ に対し最小値の位置 $x \in \mathrm{argmin} _ x f(y, x)$
  time_complexity: $O(H + W \log H)$
  space_complexity:
  aliases:
  level: orange
description: monotone minima とは、monotone な $H \times W$ 行列に対しその各行の最小値を $O(H + W \log H)$ で求めるアルゴリズムである。
---

# Monotone minima

## 説明

### 概要

monotone minima とは、monotone な $H \times W$ の行列 $f$ に対し、それぞれの行 $y$ の最小値の位置 (のうちのひとつ) $x \in \mathrm{argmin} _ x f(y, x)$ をまとめて効率よく求めるアルゴリズムである。
愚直には行列全体を走査して $O(H W)$ であるが、これを $O(H + W \log H)$ で行う。
動作原理は、行列として monotone であるとはそれぞれの列の最小値の位置が左上から右下へと並ぶことであるので、中央付近の行についてその最小値の位置を求めればその右上と左下の区画の探索を省略できるというものである。

### 詳細

行列に対する monotone の定義は、列に対する monotone (つまり単調性) の定義のひとつの一般化である。
列に関する (広義) 単調性の定義を関数の記法で書くと、次のような定義になる: 長さ $H$ の数列 $g : H \to A$ が (weakly) monotone であるとは、$y \lt y'$ ならば $g(y) \le g(y')$ であることを言う。
ただし $H, W$ は自然数とし $A$ は全順序集合とする。
これを行列に一般化して、次のような定義になる: $H \times W$ の行列 $f : H \times W \to A$ が (weakly) monotone であるとは、$y \lt y'$ ならば $\forall x \in \mathrm{argmin} _ x f(y, x).~ \exists x' \in \mathrm{argmin} _ {x'} f(y', x').~ x \le x'$ かつ $\forall x' \in \mathrm{argmin} _ {x'} f(y', x').~ \exists x \in \mathrm{argmin} _ x f(y, x').~ x \le x'$ であることを言う。
$\mathrm{argmin} _ x \dots$ が集合であることに注意したい。

以下では簡単のため、各行 $y$ ごとに要素 $x_0 \in \mathrm{argmin} _ x f(y, x)$ をそれぞれひとつ固定し、この $x_0$ と $\mathrm{argmin} _ x f(y, x)$ を同一視して考える。
この仮定のもとでは monotone の定義は次のように簡単になる: $H \times W$ の行列 $f : H \times W \to A$ が (weakly) monotone であるとは、$y \lt y'$ ならば $\mathrm{argmin} _ x f(y, x) \le \mathrm{argmin} _ {x'} f(y', x')$ であることを言う。
さらに、行列 $f$ が monotone であることは、$g(y) = \mathrm{argmin} _ x f(y, x) \in A$ で定まる数列 $g$ が列として monotone であることと等しい。

具体的なアルゴリズムは次のようなものである。

1.  monotone な $f : H \times W \to A$ を (暗な形で) 入力として受け取る。
1.  中央付近の行 $y_0 = \lfloor H / 2 \rfloor$ に対してその行の最小値を達成する列 $x_0 = \mathrm{argmin} _ x f(y_0, x)$ を求める。
1.  行列 $f$ の左上 $H' \times W' = \lbrace 0, 1, \dots, y_0 - 1 \rbrace \times \lbrace 0, 1, \dots, x_0 - 1 \rbrace$ について再帰する。
1.  行列 $f$ の右下 $H'' \times W'' = \lbrace y_0 + 1, y_0 + 2, \dots, H - 1 \rbrace \times \lbrace x_0 + 1, x_0 + 2, \dots, W - 1 \rbrace$ について再帰する。
1.  ステップ (3.) と (2.) と (4.) の結果をまとめ、$H$ 個の行それぞれの最小値の位置を出力として返す。

左上への再帰 (ステップ (3.)) において、行の長さを $W$ から $x_0$ に制限していることは、$y \lt y_0$ ならば $\mathrm{argmin} _ x f(y, x) \lt x_0$ であるために正当である。
右下への再帰についても同様。

計算量について。$O(W)$ かけてある行の最小値の列を求め、$H' \times W'$ と $H'' \times W''$ であって $H' \approx H'' \approx H/2$ かつ $W' + W'' = W - 1$ なふたつの行列に対し再帰している。
これを $H/2 \times W$ なひとつの行列への再帰だと思えば $O(H + W \log H)$ であることが分かる。

## 関連項目

-   [SMAWK algorithm](/smawk-algorithm)
    -   SMAWK algorithm は monotone minima の動作に必要な仮定を強めたものになっている。monotone ではなく totally monotone までを仮定して、各行の最小値の位置を $O(H + W)$ で求める。

## 外部リンク

-   [Totally Monotone Matrix Searching (SMAWK algorithm) - 週刊 spaghetti_source - TopCoder部](https://topcoder-g-hatena-ne-jp.jag-icpc.org/spaghetti_source/20120923/1348327542.html)
    -   <a class="handle">tmaehara</a> による解説記事
-   <https://ei1333.github.io/library/dp/monotone-minima.cpp><sup>[archive.org](https://web.archive.org/web/20210128162922/https://ei1333.github.io/library/dp/monotone-minima.cpp)</sup>
    -   <a class="handle">ei13333</a> による実装例
-   <https://kmyk.github.io/monotone-matrix-visualizer/>
    -   monotone な行列などを図示してくれるページ
