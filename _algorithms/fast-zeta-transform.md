---
layout: entry
authors:
reviewers:
date: 2020-07-09T00:00:00+09:00
updated_at:
tags: algorithm fast-zeta-transform
algorithm:
  input: >
    $n$ 要素の集合 $X$ の部分集合から可換 monoid $M$ への関数 $f : \mathcal{P}(X) \to M$ のグラフ
  output: >
    関数 $g(s) = \sum _ {s \subseteq T} f(T)$ のグラフ
  time_complexity: $O(n 2^n)$
  space_complexity:
  aliases: "高速Mobius変換"
  level: blue
description: >
  高速 zeta 変換とは、$n$ 要素の集合 $X$ の部分集合から可換 monoid $M$ への関数 $f : \mathcal{P}(X) \to M$ が与えられたとき、関数 $g(s) = \sum _ {s \subseteq T} f(T)$ の全体を $O(n 2^n)$ で求めるアルゴリズムである。累積和の $n$ 次元への一般化と理解できる。
draft: true
draft_urls: ["https://naoyat.hatenablog.jp/entry/zeta-moebius", "https://qiita.com/convexineq/items/afc84dfb9ee4ec4a67d5"]
---

# 高速 zeta 変換
