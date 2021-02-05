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
  time_complexity: たとえば $O(n)$ のものが $O(\sqrt{n} \log n)$ になる
  space_complexity:
  aliases: []
  level: cyan
description: 半分全列挙とは、$N$ 個ある要素の組合せ ($2^N$ 個ある) について処理するときに使えるテクニックのひとつ。要素を $N/2$ 個と $N/2$ 個の半分ずつに分け、それぞれのグループついて $O(\sqrt{N})$ (これは $O(2^{(N/2)})$ と等しい) で全列挙し、それらの結果を組み合わせて全体の結果を得る。計算量はたいてい $O(\sqrt{N} \log N)$ のようになる。これを利用するアルゴリズムの代表的なものに baby-step giant-step がある。
draft: true
draft_urls: ["https://www.hamayanhamayan.com/entry/2018/01/06/112704"]
---

# 半分全列挙

## 関連項目

-   baby-step giant-step
    -   baby-step giant-step は半分全列挙を用いて離散対数問題を解くアルゴリズムである。

## 外部リンク

-   [競技プログラミングにおける半分全列挙問題まとめ - はまやんはまやんはまやん](https://www.hamayanhamayan.com/entry/2018/01/06/112704)
    -   例題が多数紹介されている。
