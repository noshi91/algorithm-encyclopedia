---
layout: entry
authors: udon1206
reviewers:
date: 2021-03-04T00:00:00+09:00
updated_at:
algorithm:
  input: >
    辺重み $c : E \to \mathbb{R}$ 付き有向グラフ $G = (V, E)$ および頂点 $s \in V$
  output: >
    各頂点 $t \in V$ に対し $s$-$t$ 最短路長
  time_complexity: $O(|V| ^ 2 \log |V| + |V||E|)$
  space_complexity: $O(|V| + |E|)$
  aliases: []
  level: yellow
description:  Johnson のアルゴリズムとは、全点対間最短経路問題を解くアルゴリズムのひとつ。負閉路が存在するなら検出できる。 $O(|V| ^ 2 \log |V| + |V||E|)$ で動く。
draft: true
draft_urls: []
---

# Johnson のアルゴリズム
