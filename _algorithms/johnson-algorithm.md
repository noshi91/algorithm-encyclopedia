---
layout: entry
changelog:
- summary: 記事作成
  authors: udon1206
  reviewers: noshi91
  date: 2021-03-04T00:00:00+09:00
algorithm:
  input: >
    辺重み $c : E \to \mathbb{R}$ 付き有向グラフ $G = (V, E)$
  output: >
    各頂点の組 $(s, t) \in V \times V$ に対し $s$-$t$ 最短路長
  time_complexity: $O(\lvert V \rvert ^ 2 \log \lvert V \rvert + \lvert V \rvert\lvert E \rvert)$
  space_complexity: $O(\lvert V \rvert + \lvert E \rvert)$
  aliases: []
  level: yellow
description:  Johnson のアルゴリズムとは、全点対間最短経路問題を解くアルゴリズムのひとつ。負閉路が存在しない場合に動作する。$O(\lvert V \rvert ^ 2 \log \lvert V \rvert + \lvert V \rvert\lvert E \rvert)$ で動く。
draft: false
draft_urls: []
---

# Johnson のアルゴリズム

## 概要

Johnson のアルゴリズムとは、全点対間最短経路問題を解くアルゴリズムのひとつ。負閉路が存在しない場合に動作する。グラフ $G = (V, E) $ の辺重み $c$ を以下の2つの性質を保つように、再重み付けをし、辺重み $\hat{c}$ に更新する。

1. 各頂点の組 $(u, v) \in V times V$ に対して、ある道が辺重み $c$ について、$u$ から $v$ への最短路であることと、辺重み $\hat{c}$ について、$u$ から $v$ への最短路であることは同値である。

1. $\forall (u, v) \in E, \  \hat{c} (u, v) \geq 0$

再重み付けは、 [Bellman-Ford 法](/bellman-ford)を用いて、$ O(\lvert V \rvert \lvert E \rvert) $ で可能である。再重み付けされたグラフは、辺重みが非負実数であることから、　[Dijkstra 法](/dijkstra) を用いることができるので、$V$ の各頂点において、フィボナッチヒープを用いた [Dijkstra 法](/dijkstra)をすることで、 $O(\lvert V \rvert ^ 2 \log \lvert V \rvert + \lvert V \rvert\lvert E \rvert)$ で全点対間最短経路問題を解くことができる。

## グラフの再重み付け

$G = (V, E)$ に対して、超頂点 $s$ を導入した、 $G' = (V', E')$, $V' = V \cup \lbrace s \rbrace$, $E' = E \cup \lbrace(s, v) : v \in V \rbrace$ を考える。全ての $v \in V$ に対して、 $c(s, v) = 0$ と定義し、辺重みを拡張する。このとき、$G'$ の各頂点の組 $(u, v) \in V \times V$ の辺重み $c$ における最短経路長は $G$ の 辺重み $c$ における最短経路長と一致する。このことから、 $G'$ における全点対間最短経路問題を解くことで、 $G$ の全点対間最短経路問題を解くことができる。再重み付けをした辺重み $\hat{c}$ を以下のように定義することで、概要で述べた再重み付けの性質を持つことを述べる。
$$
\hat{c}(u,v) = c(u, v) + \delta (s, u) - \delta (s, v)
$$
ただし、 $\delta (u, v), \  (u, v) \in V' \times V'$ は辺重み $c$ における $u$ から $v$ への最短経路長である。

### 性質1. について

$p = \langle v _ 0, v _ 1, \dots, v _ {k - 1}\rangle$ を $v _ 0$ から $v _ {k - 1}$ への道とする。このとき、辺重み $\hat{c}$ 上での $p$ の経路長は、
$$
\hat{c} (p) = \displaystyle \sum _ {n = 1} ^ {k - 1} \hat{c} (v _ {n - 1}, v _ {n}) = c(p) + \delta (s, v _ 0) - \delta (s, v _ {k - 1})
$$
となる。 $\delta (s, v _ 0), \delta (s, v _ {k - 1})$ は $p$ に依存しないので、 $p$ が辺重み $c$ における $v _ 0$ から $v _ {k - 1}$ の最短経路であることと、 辺重み $\hat{c}$ における $v _ 0$ から $v _ {k - 1}$ の最短経路であることは同値である。

### 性質2. について

辺重み $c$ において、$G$ が負閉路を持たないとき、 $G'$ も負閉路を持たない。このことから、
$$
\forall u, v \in V' ,\ \delta (s, v) \leq \delta (s, u) + c(u, v)
$$
が成り立つ。よって、
$$
\hat{c}(u,v) = c(u, v) + \delta (s, u) - \delta (s, v) \geq 0
$$
となる。

以上から、 すべての $v \in V'$ における $\delta (s, v)$ が求まれば、グラフの再重み付けすることができ、これは [Bellman-Ford 法](/bellman-ford) を用いて、 $ O(\lvert V \rvert \lvert E \rvert) $ で可能である。

## 関連項目

- [Warshall-Floyd 法](/warshall-floyd)
  - Warshall-Floyd 法は全点対間最短経路問題を解くアルゴリズムのひとつ。定数倍の軽い $O(\lvert V \rvert ^ 3)$ で動く。Johnson のアルゴリズムとは異なる点として、 各頂点の組 $(s, t) \in V \times V$ において、 $s$ から $t$ への経路に負閉路が存在するかを検出できる。
