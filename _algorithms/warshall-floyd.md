---
layout: entry
author: kimiyuki
reviewers:
date: 2021-01-26T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: >
    重み $c : V \to \mathbb{R}$ 付き有向グラフ $G = (V, E)$
  output: >
    各頂点 $s, t \in V$ に対し $s \to t$ 最短路長
  time_complexity: $O(V^3)$
  space_complexity:
  aliases:
  level: green
description: >
  Warshall-Floyd 法とは、全点対間最短経路問題を解くアルゴリズムのひとつ。負閉路が存在するなら検出できる。定数倍の軽い $O(V^3)$ で動く。
draft: true
draft_urls: []
---

# Warshall-Floyd  法

## 話題

-   隣接行列の積との関連
