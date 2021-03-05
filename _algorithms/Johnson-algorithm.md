---
layout: entry
authors: udon1206
reviewers: noshi91
date: 2021-03-04T00:00:00+09:00
updated_at:
algorithm:
  input: >
    辺重み $c : E \to \mathbb{R}$ 付き有向グラフ $G = (V, E)$
  output: >
    各頂点の組 $(s, t) \in V \times V$ に対し $s$-$t$ 最短路長
  time_complexity: $O(|V| ^ 2 \log |V| + |V||E|)$
  space_complexity: $O(|V| + |E|)$
  aliases: []
  level: yellow
description:  Johnson のアルゴリズムとは、全点対間最短経路問題を解くアルゴリズムのひとつ。負閉路が存在しない場合に動作する。$O(|V| ^ 2 \log |V| + |V||E|)$ で動く。
draft: false
draft_urls: []
---

# Johnson のアルゴリズム

## 概要

Johnson のアルゴリズムとは、全点対間最短経路問題を解くアルゴリズムのひとつ。負閉路が存在しない場合に動作する。グラフ $G = (V, E) $ の辺重み $c$ を以下の2つの性質を保つように、再重み付けをし、辺重み $\hat{c}$ に更新する。

1. すべての頂点対 $u, v \in V$ に対して、ある道が辺重み $c$ について、$u$ から $v$ への最短路であることと、辺重み $\hat{c}$ について、$u$ から $v$ への最短路であることは同値である。

1. $\forall (u, v) \in E, \  \hat{c} (u, v) \geq 0$

再重み付けは、 [Bellman-Ford 法](/bellman-ford)を用いて、$ O(\| V \| \| E \|) $ で可能である。再重み付けされたグラフは、辺重みが非負実数であることから、　[Dijkstra 法](/dijkstra) を用いることができるので、$V$ の各頂点において、フィボナッチヒープを用いた [Dijkstra 法](/dijkstra)をすることで、 $O(\|V\| ^ 2 \log \|V\| + \|V\|\|E\|)$ で全点対間最短経路問題を解くことができる。
