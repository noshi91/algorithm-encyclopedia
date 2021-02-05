---
layout: entry
author:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: []
  level: cyan
description: |
  ダブリングとは、前処理をしておくことによって操作を複数回繰り返した結果を高速に求めるアルゴリズムのひとつ。事前に固定された関数 $f : N \to N$ に対して、関数 $f^0, f^1, f^2, f^4, f^8, \dots, f^{\lfloor \log K \rfloor}$ を繰り返し二乗法のようにして $O(N \log K)$ で事前に求めておく。すると、クエリとして与えられた $x \in N$ と $K$ 以下の自然数 $k$ に対して、$f^k(x)$ を $O(\log k)$ で求めることができる。これがダブリングである。ただし $N$ とは集合 $\lbrace 0, 1, 2, \dots, N - 1 \rbrace$ のことであり $f^k : N \to N$ は関数 $f^k(x) = \underbrace{f(f(\dots f(} _ {k ~\text{times}} x) \dots))$ のことである。
draft: true
draft_urls: []
---

# ダブリング
