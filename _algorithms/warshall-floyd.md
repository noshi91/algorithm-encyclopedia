---
layout: entry
author: kimiyuki
reviewers:
date: 2021-02-12T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: >
    辺重み $c : V \to \mathbb{R}$ 付き有向グラフ $G = (V, E)$
  output: >
    各頂点の組 $(s, t) \in V \times V$ に対し $s \to t$ 最短路長
  time_complexity: $O(\vert V \vert ^ 3)$
  space_complexity:
  aliases:
  level: green
description: >
  Warshall-Floyd 法とは、全点対間最短経路問題を解くアルゴリズムのひとつ。負閉路が存在するなら検出できる。定数倍の軽い $O(V^3)$ で動く。
---

# Warshall-Floyd  法

## 概要

Warshall-Floyd 法とは、全点対間最短経路問題を解くアルゴリズムのひとつ。
負閉路が存在するなら検出できる。定数倍の軽い $O(V^3)$ で動く。

全点対間最短経路問題を解くとは、辺に重みが付いた有向グラフ $G$ と頂点 $s$ が与えられたとき、頂点の組 $(s, t)$ のすべてに対して $s \to t$ 最短経路を求めるということである。

## 詳細

(省略)

## 関連項目

-   [Dijkstra 法](/dijkstra)
    -   Dijkstra 法は単一始点最短経路問題を解くアルゴリズムのひとつである。競技プログラミングでは Warshall-Floyd 法と並んで頻繁に利用される。
-   [Bellman-Ford 法](/bellman-ford)
    -   Bellman-Ford 法は単一始点最短経路問題を解くアルゴリズムのひとつである。これは Warshall-Floyd 法をすべての頂点を始点として並列で実行するようなアルゴリズムになっている。
