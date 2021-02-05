---
layout: entry
author:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: 数 $a$ および自然数 $n$
  output: 累乗 $a^n$
  time_complexity: $O(\log n)$
  space_complexity:
  aliases: []
  level: cyan
description: 繰り返し二乗法とは、与えられた数 $a$ と自然数 $n$ に対し累乗 $a^n$ を $O(\log n)$ 回の乗算で求めるアルゴリズムのひとつ。$1 = a^0, a = a^1, a^2 = a \cdot a, a^4 = a^2 \cdot a^2, a^8 = a^4 \cdot a^4, \dots$ を計算し、これらを適切に掛け合わせることで、合計 $O(\log n)$ 回の乗算で $a^n$ が求まる。競技プログラミングにおいては行列などに対してもよく用いられる。
draft: true
draft_urls: []
---

# 繰り返し二乗法
