---
layout: entry
changelog:
  - summary: 記事作成
    authors: kimiyuki
    reviewers:
    date: 2021-03-28T00:00:00+09:00
algorithm:
  input: >
    ネットワークフロー (つまり有向グラフ $G = (V, E)$ および辺用量 $c : E \to \mathbb{R}$ および頂点 $s, t \in V$)
  output: >
    $s$-$t$ 最大流 $f : E \to \mathbb{R}$
  time_complexity: >
    最悪計算量は $O(\lvert V \rvert^2 \lvert E \rvert)$ だが実用的にはかなり速い
  space_complexity:
  aliases: []
  level: blue
description: >
  Dinic 法は最大流問題を解くアルゴリズムのひとつ。
  $s$-$t$ 最短経路 DAG を BFS により構成し、増加パスをこの DAG の上の DFS により探して流せるだけ流す、という一連のステップを繰り返す。
  計算量は $O(\lvert V \rvert^2 \lvert E \rvert)$ だが実用的にはかなり速い。
---

# Dinic 法

## 概要

Dinic 法は最大流問題を解くアルゴリズムのひとつである。
$s$-$t$ 最短経路 DAG を BFS により構成し、増加パスをこの DAG の上の DFS により探して流せるだけ流す、という一連のステップを繰り返す。
計算量は $O(\lvert V \rvert^2 \lvert E \rvert)$ だが実用的にはかなり速い。


## 詳細

(省略)


## 関連項目

-   [Ford-Fulkerson 法](/ford-fulkerson)
    -    Ford-Fulkerson 法は Dinic 法と並んで競技プログラミングでよく利用される最大流問題を解くアルゴリズムのひとつである。Dinic 法では最短経路 DAG を構成して増加パスをこの DAG の上で探すが、Ford-Fulkerson 法では増加パスを単純な DFS により探す。


## 外部リンク

-   [Dinic 法とその時間計算量 - みさわめも](https://misawa.github.io/others/flow/dinic_time_complexity.html)<sup>[archive.org](https://web.archive.org/web/20210328020326/https://misawa.github.io/others/flow/dinic_time_complexity.html)</sup>
    -   <a class="handle">MiSawa</a> による解説記事。計算量解析について詳しい。
-   [最大流問題について. - れんしゅうちょう。 - TopCoder部](https://topcoder-g-hatena-ne-jp.jag-icpc.org/Mi_Sawa/20140311.html)<sup>[archive.org](https://web.archive.org/web/20210328021542/https://topcoder-g-hatena-ne-jp.jag-icpc.org/Mi_Sawa/20140311.html)</sup>
    -   <a class="handle">MiSawa</a> によるブログ記事。Dinic 法のよくある実装ミスや最悪ケースが紹介されている。
-   [競技プログラミングにおける最大流問題まとめ - はまやんはまやんはまやん](https://blog.hamayanhamayan.com/entry/2017/05/09/120217)<sup>[archive.org](https://web.archive.org/web/20210328020304/https://blog.hamayanhamayan.com/entry/2017/05/09/120217)</sup>
    -   <a class="handle">hamayanhamayan</a> によるブログ記事。例題が列挙されている。
