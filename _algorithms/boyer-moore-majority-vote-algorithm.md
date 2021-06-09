---
layout: entry
changelog:
  - summary: 記事作成
    authors: noshi91
    reviewers:
    date: 2021-06-09T14:03:49+09:00
algorithm:
  input: 長さ $N$ の列 $a$
  output: $a$ に $\frac{N}{2}$ 回を超えて出現する要素が存在するかどうか、存在する場合その要素
  time_complexity: $\Theta(N)$
  space_complexity: $\Theta(1)$
  aliases: []
  level: yellow
description: >
    Boyer-Moore majority vote algorithm は、全体の過半数を占める要素を効率的に発見するあるアルゴリズムである。
    相異なる要素を繰り返し対にして、対にならずに残った要素が過半数となる候補であるという事実を用いる。
    要素に対しては一致判定のみを用いるため、全順序などが定義されている必要が無い。
    過半数を占める要素が存在しない場合何を出力しても良いことにすると、空間計算量をそのままに、列を一度走査するだけで計算することが可能になる。
---

# Boyer-Moore majority vote algorithm

## 概要

Boyer-Moore majority vote algorithm は、全体の過半数を占める要素を効率的に発見するあるアルゴリズムである。
相異なる要素を繰り返し対にして、対にならずに残った要素が過半数となる候補であるという事実を用いる。
要素に対しては一致判定のみを用いるため、全順序などが定義されている必要が無い。
過半数を占める要素が存在しない場合何を出力しても良いことにすると、空間計算量をそのままに、列を一度走査するだけで計算することが可能になる。

## 詳細



## 一般化

長さ $N$ の列 $a$ と $1 \leq k \leq N$ を満たす整数 $k$ が与えられて、$a$ に $\frac{N}{k + 1}$ 回を超えて出現する要素を列挙することが $\Theta(Nk)$ の時間計算量、$\Theta(k)$ の空間計算量で可能である。
元のアルゴリズムとほとんど同様に、$k + 1$ 個の互いに相異なる要素を組にして、組になっていない高々 $k$ 種類の要素とそれぞれの個数を管理すればよい。

## その他

-   同様の考え方で、Segment Tree を用いて、区間の過半数を占める要素を発見することが出来る。
    それぞれのノードは対応する区間で対にならずに残る要素とその個数を管理し、区間をマージする際は必要なだけ対を作れば、常に 1 種類以下の要素が残る状態が保たれる。

## 参考文献

-   Boyer, R. S., & Moore, J. S. (1991). MJRTY—a fast majority vote algorithm. In Automated Reasoning (pp. 105-117). Springer, Dordrecht.
    -   Boyer-Moore majority vote algorithm が提案された論文
