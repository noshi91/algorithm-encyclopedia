---
layout: entry
changelog:
  - summary: 見出し作成
    date: 2021-02-05T00:00:00+09:00
    authors: kimiyuki
    reviewers:
  - summary: 記事作成
    authors: kimiyuki
    reviewers: noshi91
    date: 2021-03-09T00:00:00+09:00
algorithm:
  input: パターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ とテキスト文字列 $T$
  output: パターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ のどれがテキスト文字列 $T$ に含まれるか。含まれるならその位置も求める。
  time_complexity: アルファベット $\Sigma$ の大きさは定数であるとして、前処理には $O(\sum \vert P_i \vert)$ で検索には $O(\vert T \vert)$
  space_complexity:
  aliases: []
  level: orange
description: Aho-Corasick 法とは、複数のパターン文字列をまとめて扱える文字列検索アルゴリズムのひとつ。まず前処理として、固定された $k$ 個のパターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ たちから Trie 木を作り、その上に適切に辺を張って $O(\sum \vert P_i \vert)$ でオートマトンを作る。このオートマトンを利用して、与えられたテキスト文字列 $T$ に対して $O(\vert T \vert)$ で検索を行う。
---

# Aho-Corasick 法

## 概要

Aho-Corasick 法とは、複数のパターン文字列をまとめて扱える文字列検索アルゴリズムのひとつ。計算量はアルファベット $\Sigma$ の大きさにも依存するが、ここでは $\Sigma$ を固定し大きさは定数としておく。まず前処理として、固定された $k$ 個のパターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ たちから Trie 木を作り、その上に適切に辺を張って $O(\sum \vert P_i \vert)$ でオートマトンを作る。このオートマトンを利用して、与えられたテキスト文字列 $T$ に対して $O(\vert T \vert)$ で検索を行う。

## 詳細

(省略)

## メモ

-   計算量はアルファベット $\Sigma$ の大きさ $\sigma = \lvert \Sigma \rvert$ にも依存する。競技プログラミングにおいてはたいてい $\sigma = 26$ で定数であり、これに注意する必要はないだろう。一般の $\sigma$ が定数でない場合には、遷移関数をどのように持つかを考える必要が出てくる。これに hash map をもちいると計算量が期待計算量になり、平衡二分探索木を用いると計算量に $\log(\sigma)$ が乗る。

## 参考文献

-   Alfred V. Aho and Margaret J. Corasick. 1975. Efficient string matching: an aid to bibliographic search. Commun. ACM 18, 6 (June 1975), 333–340. DOI:<https://doi.org/10.1145/360825.360855>
    -   Aho-Crasick 法が提案された論文

## 関連項目

-   [Rabin-Karp 法](/algorithm-encyclopedia/rabin-karp)
    -   Rabin-Karp 法は Aho-Corasick 法と並んで競技プログラミングでよく利用される複数パターン文字列検索アルゴリズムである。

## 外部リンク

-   [Aho-Corasick法 - Algoogle](https://algoogle.hadrori.jp/algorithm/aho-corasick.html)<sup>[archive.org](https://web.archive.org/web/20210311070301/https://algoogle.hadrori.jp/algorithm/aho-corasick.html)</sup>
    -   <a class="handle">hadrori</a> による実装例。図付きでの解説もある。
-   [競技プログラミングにおける文字列アルゴリズム問題まとめ - はまやんはまやんはまやん](https://blog.hamayanhamayan.com/entry/2017/03/25/005452)<sup>[archive.org](https://web.archive.org/web/20210402112827/https://blog.hamayanhamayan.com/entry/2017/03/25/005452)</sup>
    -   <a class="handle">hamayanhamayan</a> によるブログ記事。例題が列挙されている。
