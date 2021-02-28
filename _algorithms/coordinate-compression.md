---
layout: entry
authors:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
algorithm:
  input: 長さ $N$ の整数列 $a$
  output: |
    長さ $N$ の自然数列 $b$ であって、要素の順序関係が $a$ と同じでかつ最大値 $\max_i b_i$ が最小であるもの
  time_complexity: $O(N \log N)$
  space_complexity:
  aliases: ["座圧"]
  level: cyan
description: |
  座標圧縮とは、与えられた長さ $N$ の整数列 $a$ から、長さ $N$ の自然数列 $b$ であって要素の順序関係が $a$ と同じでかつ最大値 $\max_i b_i$ が最小であるような $b$ を作ること。ただし「要素の順序関係が同じ」とは、任意の $i, j$ に対し $a_i \le a_j \leftrightarrow b_i \le b_j$ を満たすことを言う。このような $b$ は常に一意に存在し、単純な方法により $O(N \log N)$ で構成できる。
draft: true
draft_urls: []
---

# 座標圧縮
