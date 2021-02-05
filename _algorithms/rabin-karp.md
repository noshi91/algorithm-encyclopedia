---
layout: entry
author:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: パターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ とテキスト文字列 $T$
  output: パターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ のどれがテキスト文字列 $T$ に含まれるか。含まれるならその位置も
  time_complexity: 前処理には $O(\sum \vert P_i \vert)$ など、検索には平均 $O(\vert T \vert)$ など
  space_complexity:
  aliases: []
  level: blue
description: Rabin-Karp 法とは、複数のパターン文字列をまとめて扱える文字列検索アルゴリズムのひとつ。固定された $k$ 個のパターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ のそれぞれについて $O(\sum \vert P_i \vert)$ などをかけてハッシュ値を求めておくことで、与えられたテキスト文字列 $T$ に対し平均 $O(\vert T \vert)$ などでこれらの検索ができる。ハッシュ関数は自由だが、ローリングハッシュが使われることが多い。
draft: true
draft_urls: []
---

# Rabin-Karp法

## 参考文献

-   R. M. Karp and M. O. Rabin, "Efficient randomized pattern-matching algorithms," in IBM Journal of Research and Development, vol. 31, no. 2, pp. 249-260, March 1987, doi: [10.1147/rd.312.0249](https://doi.org/10.1147/rd.312.0249).
    -   Rabin-Karp 法が提案された論文

## 関連項目

-   [Aho-Corasick法](/aho-corasick)
    -   Aho-Corasick 法は Rabin-Karp 法と並んで競技プログラミングでよく利用される複数パターン文字列検索アルゴリズムである。

## 外部リンク

-   [競技プログラミングにおける文字列アルゴリズム問題まとめ - はまやんはまやんはまやん](https://www.hamayanhamayan.com/entry/2017/03/25/005452)
    -   hamayanhamayan によるブログ記事。例題が列挙されている。
