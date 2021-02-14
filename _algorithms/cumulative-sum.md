---
layout: entry
authors:
reviewers:
date: 2021-01-26T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: 長さ $N$ の数列 $a$
  output: 長さ $N + 1$ の数列 $b$ (ただし $b_i = \sum _ {j \lt i} a_i$)
  time_complexity: 構築に $O(N)$ で利用に $O(1)$
  space_complexity: $O(N)$
  aliases: []
  level: green
description: 累積和とは、ある数列の接頭辞の総和たちを要素とする数列のこと。長さ $N$ の数列 $a = (a_0, a_1, \dots, a _ N)$ に対する累積和とは $b_i = \sum _ {j \lt i} a_i$ であるような長さ $N + 1$ の数列 $b$ である。数列の要素が群の要素であるときには区間 $\lbrack l, r)$ の総和 $\sum _ {i \in \lbrack l, r)} a_i = b_r - b_l$ を $O(1)$ で計算することなどに用いることができる。
draft: true
draft_urls: []
---

# 累積和

## 話題

-   imos 法との関連
-   可換性についての注意
-   標準ライブラリ内の関数 `std::partial_sum`
-   現実での利用例: 疎行列
