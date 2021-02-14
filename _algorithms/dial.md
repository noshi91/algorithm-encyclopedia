---
layout: entry
author: kimiyuki
reviewers:
date: 2021-02-12T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: >
    非負かつ $k$ 以下で整数値の辺重み $c : V \to \lbrace x \in \mathbb{Z} \mid 0 \le x \lt k \rbrace$ 付き有向グラフ $G = (V, E)$ および頂点 $s \in V$
  output: >
    各頂点 $t \in V$ に対し $s \to t$ 最短路長
  time_complexity: $O(k \vert V \vert + \vert E \vert)$
  space_complexity:
  aliases:
  level: red
description: >
  Dial's algorithm とは、単一始点最短経路問題を解くアルゴリズムのひとつ。非負かつ最大値の小さい整数重みのグラフについてしか動作しないが、重みの最大値を $k$ として $O(k \vert V \vert + \vert E \vert)$ で動く。キューの持ち方を工夫して Dijkstra 法をさらに高速化したものになっている。0-1 BFS の一般化でもあり、$k = 1$ のときは 0-1 BFS に一致する。
---

# Dial's algorithm

## 概要

Dial's algorithm とは、単一始点最短経路問題を解くアルゴリズムのひとつ。非負かつ最大値の小さい整数重みのグラフについてしか動作しないが、重みの最大値を $k$ として $O(k \vert V \vert + \vert E \vert)$ で動く。

Dial's algorithm は、キューの持ち方を工夫して Dijkstra 法を高速化したものになっている。
0-1 BFS の一般化でもあり、$k = 1$ のときは 0-1 BFS に一致する。

## 詳細

(省略)

## 参考文献

-   Robert B. Dial. 1969. Algorithm 360: shortest-path forest with topological ordering [H]. Commun. ACM 12, 11 (Nov. 1969), 632–633. DOI:<https://doi.org/10.1145/363269.363610>
    -   Dial による提案論文。始点が複数の形で書かれている。また、Dijkstra 法ではなく SPFA を最適化したものとして説明されている。

## 関連項目

-   [Dijkstra 法](/dijkstra)
    -   Dial's algorithm は Dijkstra 法を修正して高速化したものである。
