---
layout: entry
author: kimiyuki
reviewers:
date: 2021-01-23T00:00:00+09:00
updated_at:
tags: algorithm dijkstra
algorithm:
  input: >
    非負の辺重み $c : V \to \lbrace x \in \mathbb{R} \mid x \ge 0 \rbrace$ 付き有向グラフ $G = (V, E)$ および頂点 $s \in V$
  output: >
    各頂点 $t \in V$ に対し $s \to t$ 最短路長、あるいは $s \to t$ 最短路
  time_complexity: $O(E \log V)$ など
  space_complexity:
  aliases:
description: >
  Dijkstra's algorithm とは、単一始点最短経路問題を解くアルゴリズムのひとつ。辺に非負の重みが付いた有向グラフ $G$ と頂点 $s$ が与えられたとき、$s$ を始点とする $s \to t$ 最短経路をすべての頂点 $t$ に対して $O(E \log V)$ などで求める。コストが非負という仮定をもとに動的計画法を利用する。
draft: true
draft_urls: ["http://kuuso1.hatenablog.com/entry/2015/12/20/212620"]
---

# Dijkstra 法

## 話題

-   拡張グラフ上の Dijkstra 法
-   高速化テク
-   $O(V^2)$ Dijkstra 法について
-   計算量について
-   両側からの Dijkstra 法
