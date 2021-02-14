---
layout: entry
authors:
reviewers:
date: 2020-07-09T00:00:00+09:00
updated_at:
tags: algorithm dsu-on-tree sack disjoint-set-union
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: Sack
  level: orange
description: DSU on tree とは、それぞれの頂点 $x$ に可換 monoid $(M, +, 0)$ の要素の重み $a_x$ のついた木 $T$ のそれぞれの部分木について、その部分木内の重みの総和を全体で $O(n \log n)$ で求めるアルゴリズムである。ただし、その計算の過程において、monoid 演算 $+$ がある要素 $A \in M$ と頂点 $x$ に対し $A + a_x$ という形でしか出現しないという特徴がある。
draft: true
draft_urls: "https://codeforces.com/blog/entry/44351"
---

# DSU on tree
