---
layout: entry
changelog:
  - summary: 記事作成
    authors: kimiyuki
    reviewers:
    date: 2021-04-01T00:00:00+09:00
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: ["最大フロー問題", "maximum flow problem"]
  level: blue
description: >
  最大流問題とは、与えられたネットワークのフローであって流量が最大のものを求めるという問題。
  最大流最小カット定理によって最大流問題の解の流量は最小カット問題の解の容量に等しい。
---

# 最大流問題

## 概要

最大流問題とは、与えられたネットワークのフローであって流量が最大のものを求めるという問題である。
最大流最小カット定理によって最大流問題の解の流量は[最小カット問題](/minimum-cut-problem)の解の容量に等しい。


## 詳細

(省略)


## その他

-   フローの定義では「始点から終点へと向かうフローと無関係な位置に閉路状のフローがないこと」は要求されていない。最大流を求めるアルゴリズムはこのような閉路状のフローを含む出力をすることがあるので、出力されたフローの構成を利用する際には注意が必要である。なお、最大流問題の解から流量を変えずにこのような閉路状のフローを取り除くことは常に可能である。


## 関連項目

-   [最小カット問題](/minimum-cut-problem)
    -   最大流最小カット定理によって最大流問題の解の流量は最小カット問題の解の容量に等しい。
-   [Dinic 法](/dinic)
    -   Dinic 法は最大流問題を解くアルゴリズムである。最悪計算量は $O(\lvert V \rvert^2 \cdot \lvert E \rvert)$ だが実用的にはかなり速い。
-   [Ford-Fulkerson 法](/ford-fulkerson)
    -   Ford-Fulkerson 法は最大流問題を $O(F \cdot \lvert E \rvert)$ で解く代表的なアルゴリズムである。
