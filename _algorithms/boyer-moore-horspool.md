---
layout: entry
authors:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: パターン文字列 $P$ とテキスト文字列 $T$
  output: パターン文字列 $P$ がテキスト文字列 $T$ に含まれるかどうか。含まれるならその位置も
  time_complexity: 前処理は $O(\vert P \vert)$ である。検索は、ランダムな文字列に対しては $O(\vert T \vert)$ だが最悪ケースは $O(\vert P \vert \cdot \vert T \vert)$ である。
  space_complexity:
  aliases: []
  level: black
description: Boyer-Moore-Horspool 法は、文字列検索アルゴリズムのひとつ。Boyer-Moore 法を簡略化したものである。
draft: true
draft_urls: []
---

# Boyer-Moore-Horspool法

## 関連項目

-   [Boyer-Moore法](/boyer-moore)
    -   Boyer-Moore-Horspool 法は Boyer-Moore 法を簡略化したアルゴリズムである。

## 外部リンク

-   [boyer_moore_horspool_searcher - cpprefjp C++日本語リファレンス](https://cpprefjp.github.io/reference/functional/boyer_moore_horspool_searcher.html)
    -   C++ の標準ライブラリには Boyer-Moore-Horspool 法を用いた関数オブジェクトが `std::boyer_moore_horspool_searcher` として含まれている。
