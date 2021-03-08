---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers:
    date: 2021-02-05T00:00:00+09:00
  - summary: 記事作成
    authors: kimiyuki
    reviewers: noshi91
    date: 2021-03-09T00:00:00+09:00
algorithm:
  input: パターン文字列 $P$ とテキスト文字列 $T$
  output: パターン文字列 $P$ がテキスト文字列 $T$ に含まれるかどうか。含まれるならその位置も求める。
  time_complexity: 前処理は $O(\vert P \vert)$ である。検索は、ランダムな文字列に対しては $O(\vert T \vert / \vert P \vert)$ だが最悪ケースは $O(\vert P \vert \cdot \vert T \vert)$ である。
  space_complexity:
  aliases: ["BM法"]
  level: orange
description: Boyer-Moore 法とは、文字列検索アルゴリズムのひとつ。どこで不一致が起きたらパターン文字列をいくつずらせばよいかの情報を $O(\vert P \vert)$ かけて構築しておき、パターン文字列をその末尾から順にテキスト文字列と照合していく。ランダムな文字列に対しては $O(\vert T \vert / \vert P \vert)$ だが、最悪ケースでは $O(\vert P \vert \cdot \vert T \vert)$ かかる。
---

# Boyer-Moore 法

## 概要

Boyer-Moore 法とは、文字列検索アルゴリズムのひとつ。どこで不一致が起きたらパターン文字列をいくつずらせばよいかの情報を $O(\vert P \vert)$ かけて構築しておき、パターン文字列をその末尾から順にテキスト文字列と照合していく。ランダムな文字列に対しては $O(\vert T \vert / \vert P \vert)$ だが、最悪ケースでは $O(\vert P \vert \cdot \vert T \vert)$ かかる。

## 詳細

(省略)

## 参考文献

-   Robert S. Boyer and J. Strother Moore. 1977. A fast string searching algorithm. Commun. ACM 20, 10 (Oct. 1977), 762–772. DOI:<https://doi.org/10.1145/359842.359859>
    -   Boyer-Moore 法が提案された論文

## 関連項目

-   [Boyer-Moore-Horspool 法](/boyer-moore-horspool)
    -   Boyer-Moore-Horspool 法は Boyer-Moore 法を簡略化したアルゴリズムである。
-   [Knuth-Morris-Pratt 法](/knuth-morris-pratt)
    -   Knuth-Morris-Pratt 法は Boyer-Moore 法と並んで競技プログラミングでよく用いられる単一パターン文字列検索アルゴリズムである。

## 外部リンク

-   [boyer_moore_searcher - cpprefjp C++日本語リファレンス](https://cpprefjp.github.io/reference/functional/boyer_moore_searcher.html)
    -   C++ の標準ライブラリには Boyer-Moore 法を用いた関数オブジェクトが `std::boyer_moore_searcher` として含まれている。
