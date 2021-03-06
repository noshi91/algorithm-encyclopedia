---
layout: entry
changelog:
  - summary: 見出し作成
    date: 2021-02-28T00:00:00+09:00
    authors: kimiyuki
    reviewers:
tags: algorithm
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: []
  level: yellow
description: |
  ビームサーチはグラフ探索アルゴリズムのひとつである。与えられたグラフ (たいてい DAG) を初期状態となる頂点群から幅優先探索と同様に探索していくが、定数 $K$ と頂点に対する評価関数 $\varphi : V \to \mathbb{R}$ をあらかじめ固定しておき、各深さごとにその評価関数による評価値が高い順に $K$ 個のみを保持してそれ以外の頂点は無視する。$K = 1$ のときは貪欲法と一致する。焼きなまし法と並んで、ヒューリスティックコンテストで頻繁に利用されるアルゴリズムである。
draft: true
draft_urls: ["http://hakomof.hatenablog.com/entry/2018/12/06/000000"]
---

# ビームサーチ

## 話題

-   重複除去の話
