---
layout: entry
changelog:
  - summary: 記事作成
    authors: kimiyuki
    reviewers: kuretchi
    date: 2021-02-12T00:00:00+09:00
algorithm:
  input: >
    辺重み $c : E \to \mathbb{R}$ 付き有向グラフ $G = (V, E)$ および頂点 $s \in V$
  output: >
    各頂点 $t \in V$ に対し $s$-$t$ 最短路長
  time_complexity: $O(\vert V \vert \cdot \vert E \vert)$
  space_complexity:
  aliases: ["SPFA"]
  level: yellow
description: >
  Shortest Path Faster Algorithm (SPFA) とは、単一始点最短経路問題を解くアルゴリズムのひとつ。Bellman-Ford 法をキューを使って定数倍高速化したものであり、優先度付きキューでなく普通のキューを使う Dijkstra 法のようなものでもある。計算量は $O(\vert V \vert \cdot \vert E \vert)$ である。
---

# Shortest Path Faster Algorithm

## 概要

Shortest Path Faster Algorithm (SPFA) とは、単一始点最短経路問題を解くアルゴリズムのひとつ。Bellman-Ford 法をキューを使って定数倍高速化したものであり、優先度付きキューでなく普通のキューを使う Dijkstra 法のようなものでもある。計算量は $O(\vert V \vert \cdot \vert E \vert)$ である。

## 詳細

(省略)

## その他

-   基本的に常に Bellman-Ford 法より速いようである[^hogloid-speed]。

## 関連項目

-   [Bellman-Ford 法](/bellman-ford)
    -   Bellman-Ford 法をキューを用いて高速化したものが SPFA である。
-   [Dijkstra 法](/dijkstra)
    -   Dijkstra 法を優先度付きキューでなく普通のキューを使うように修正するとほとんど SPFA になる。

## 外部リンク

-   [SPFAの紹介 - hogloidのブログ](https://hogloid.hatenablog.com/entry/20120409/1333973448)<sup>[archive.org](https://web.archive.org/web/20130519162505/http://hogloid.hatenablog.com/entry/20120409/1333973448)</sup>
    -   <a class="handle">hogloid</a> によるブログ記事。簡単な解説と実装例がある。

## 注釈

[^hogloid-speed]: 「少なくともベルマンフォードより遅くなったことはありません」 [SPFAの紹介 - hogloidのブログ](https://hogloid.hatenablog.com/entry/20120409/1333973448)<sup>[archive.org](https://web.archive.org/web/20130519162505/http://hogloid.hatenablog.com/entry/20120409/1333973448)</sup>
