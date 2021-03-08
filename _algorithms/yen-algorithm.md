---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers:
    date: 2020-07-09T00:00:00+09:00
algorithm:
  input: 有向あるいは無向グラフ $G$ とその頂点 $s, t$ および自然数 $K$
  output: $G$ の $s-t$ 単純路であって $K$ 番目に短いもの
  time_complexity: $O(K V (E + V) \log V)$
  space_complexity:
  aliases:
  level: black
description: Yen's algorithm とは、与えられたグラフ $G$ の $s-t$ 単純路であって $K$ 番目に短いものを $O(K V (E + V) \log V)$ で求めるアルゴリズムである。
draft: true
draft_urls: "https://qiita.com/nariaki3551/items/821dc6ffdc552d3d5f22"
---

# Yen's algorithm
