---
layout: entry
changelog:
  - summary: 記事作成
    authors: kimiyuki
    reviewers:
    date: 2021-03-28T00:00:00+09:00
algorithm:
  input: >
    辺容量が整数であるネットワーク (つまり有向グラフ $G = (V, E)$ および辺容量 $c : E \to \mathbb{N}$ および相異なる頂点 $s, t \in V$)
  output: >
    $s$-$t$ 最大流 (つまり関数 $f : E \to \mathbb{N}$ であって容量制限とフロー保存則を満たすもの)
  time_complexity: >
    出力の $s$-$t$ 最大流量を $F$ として $O(F \cdot \lvert E \rvert)$
  space_complexity:
  aliases: []
  level: blue
description: >
  Ford-Fulkerson 法は最大流問題を解くアルゴリズムのひとつ。
  増加パスを DFS で探してそこにフローを流していくことを繰り返す。
  計算量は出力の $s$-$t$ 最大流量を $F$ として $O(F \cdot \lvert E \rvert)$ である。
---

# Ford-Fulkerson 法

## 概要

Ford-Fulkerson 法は最大流問題を解くアルゴリズムのひとつである。
残余グラフ上で増加パスを DFS で探しそこにフローを流していくことを繰り返す。
計算量は出力の $s$-$t$ 最大流量を $F$ として $O(F \cdot \lvert E \rvert)$ である。


## 詳細

(省略)


## 関連項目

-   [Dinic 法](/dinic)
    -    Dinic 法は Ford-Fulkerson 法と並んで競技プログラミングでよく利用される最大流問題を解くアルゴリズムのひとつである。Ford-Fulkerson 法では増加パスを単純な DFS により探すが、Dinic 法では最短経路 DAG を構成して増加パスをこの DAG の上で探す。


## 外部リンク

-   [競技プログラミングにおける最大流問題まとめ - はまやんはまやんはまやん](https://blog.hamayanhamayan.com/entry/2017/05/09/120217)<sup>[archive.org](https://web.archive.org/web/20210328020304/https://blog.hamayanhamayan.com/entry/2017/05/09/120217)</sup>
    -   <a class="handle">hamayanhamayan</a> によるブログ記事。例題が列挙されている。
