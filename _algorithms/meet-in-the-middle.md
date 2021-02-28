---
layout: entry
authors:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
algorithm:
  input:
  output:
  time_complexity: たとえば $O(n)$ のものが $O(\sqrt{n} \log n)$ になる
  space_complexity:
  aliases: []
  level: cyan
description: 半分全列挙とは、組合せについて処理するときに使えるテクニックのひとつ。すべての要素を考えたときの組合せの全体は列挙するには多すぎるが、半分程度の数の要素に制限して考えたときの組合せであれば列挙できる、という場合に利用可能である。要素の全体をそれぞれ半分程度の大きさのふたつのグループに分け、それぞれのグループについて組合せを全列挙し、それらふたつの結果を組み合わせて全体に対する結果を得る。そのまま全列挙したときの計算量が $O(f(N))$ であるとき、半分全列挙を行ったときの計算量はたとえば $O(\sqrt{f(N)})$ や $O(\sqrt{f(N)} \log f(N))$ などになる。これを利用するアルゴリズムの代表的なものに baby-step giant-step がある。
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
