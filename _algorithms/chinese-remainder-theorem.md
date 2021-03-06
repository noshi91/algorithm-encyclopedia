---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers: ["MiSawa", "hos_lyric"]
    date: 2021-02-28T00:00:00+09:00
tags: algorithm
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: ["Chinese remainder theorem", "CRT", "中国人剰余定理"]
  level: blue
description: |
  中国剰余定理とは、任意の互いに素な正整数 $m, n$ に対して、剰余環 $\mathbb{Z}/m n \mathbb{Z}$ と剰余環の直積環 $(\mathbb{Z}/m \mathbb{Z}) \times (\mathbb{Z}/n \mathbb{Z})$ とが $\phi(x) = (x \bmod m, x \bmod n)$ で定まる写像 $\phi : \mathbb{Z}/m n \mathbb{Z} \to (\mathbb{Z}/m \mathbb{Z}) \times (\mathbb{Z}/n \mathbb{Z})$ によって環同型である、という定理のこと。あるいは同じことだが、任意の互いに素な正整数 $m, n$ および任意の整数 $a, b$ に対して、ある整数 $x$ が $m n$ を法として一意に存在して、$x \equiv a \pmod{m}$ かつ $x \equiv b \pmod{n}$ を満たす、という定理のこと。
draft: true
draft_urls: ["http://elliptic-shiho.hatenablog.com/entry/2016/04/03/020117", "https://qiita.com/drken/items/ae02240cd1f8edfc86fd"]
---

# 中国剰余定理
