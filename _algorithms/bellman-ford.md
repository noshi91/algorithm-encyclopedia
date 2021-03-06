---
layout: entry
authors: kimiyuki
reviewers: kuretchi
date: 2021-02-12T00:00:00+09:00
updated_at:
algorithm:
  input: >
    辺重み $c : E \to \mathbb{R}$ 付き有向グラフ $G = (V, E)$ および頂点 $s \in V$
  output: >
    各頂点 $t \in V$ に対し $s$-$t$ 最短路長
  time_complexity: $O(\vert V \vert \cdot \vert E \vert)$
  space_complexity:
  aliases: []
  level: cyan
description: >
  Bellman-Ford 法とは、単一始点最短経路問題を解くアルゴリズムのひとつ。負辺があっても動作する。計算量は $O(\vert V \vert \cdot \vert E \vert)$ である。
---

# Bellman-Ford 法

## 概要

Bellman-Ford 法とは、単一始点最短経路問題を解くアルゴリズムのひとつ。負辺があっても動作する。
ある有向辺 $(x, y)$ を使うことで頂点 $y$ への最短経路長が改善するか試し、改善するなら置き換えるという処理 (これを「緩和する」などと言う) を考える。これをすべての辺に対して行うのを 1 セットとし、これを $\vert V \vert - 1$ 回行うのが Bellman-Ford 法である。その後、負閉路が存在していなかったことの確認も行う。
計算量は $O(\vert V \vert \cdot \vert E \vert)$ である。

## 詳細

(省略)

## その他

-   辺の重みの正負をすべて反転させることで、単一始点最長経路問題を解くこともできる。

## 関連項目

-   [Dijkstra 法](/dijkstra)
    -   Dijkstra 法は単一始点最短経路問題を解くアルゴリズムのひとつである。Bellman-Ford 法とは違って負辺があると動作しないが、Bellman-Ford 法より速い。
-   [Warshall-Floyd 法](/warshall-floyd)
    -   Warshall-Floyd 法は全点対間最短経路問題を解くアルゴリズムのひとつである。Bellman-Ford 法と同様に、緩和を収束するまで繰り返すことで動作する。
-   [Shortest Path Faster Algorithm](/spfa)
    -   Bellman-Ford 法はすべての辺について $\vert V \vert - 1$ 回ずつ緩和を行うが、これを (優先度付きではない、普通の) キューを用いて変更のあった頂点の周囲のみを緩和するように修正して高速化したものが Shortest Path Faster Algorithm である。
