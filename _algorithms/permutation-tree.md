---
layout: entry
changelog:
  - summary: 記事作成
    authors: noshi91
    reviewers:
    date: 2021-06-06T00:43:16+09:00
algorithm:
  input: 順列 $P$
  output: $P$ の permutation tree
  time_complexity: $\Theta ( \lvert P \rvert )$
  space_complexity: $\Theta ( \lvert P \rvert )$
  aliases: ["common interval decomposition tree"]
  level: red
description: >
    permutation tree は順列に対して定まる、ある木構造である。
    順列 $P$ の連続部分列 $P \lbrack l , r \rbrack$ であって $\max - \min = r - l$ となるようなもの全体の構造を表現している。
---

# Permutation Tree

## 概要

permutation tree は順列に対して定まる、ある木構造である。
順列 $P$ の連続部分列 $P \lbrack l , r \rbrack$ であって $\max - \min = r - l$となるようなもの全体の構造を表現している。

## 詳細

$P$ を順列とする。
区間 $\lbrack l , r \rbrack$ であってを満たすものを common interval と呼ぶことにする。
今

## メモ

-   計算量はアルファベット $\Sigma$ の大きさ $\sigma = \lvert \Sigma \rvert$ にも依存する。競技プログラミングにおいてはたいてい $\sigma = 26$ で定数であり、これに注意する必要はないだろう。一般の $\sigma$ が定数でない場合には、遷移関数をどのように持つかを考える必要が出てくる。これに hash map をもちいると計算量が期待計算量になり、平衡二分探索木を用いると計算量に $\log(\sigma)$ が乗る。

## 参考文献

-   Alfred V. Aho and Margaret J. Corasick. 1975. Efficient string matching: an aid to bibliographic search. Commun. ACM 18, 6 (June 1975), 333–340. DOI:<https://doi.org/10.1145/360825.360855>
    -   Aho-Crasick 法が提案された論文

## 関連項目

-   [Rabin-Karp 法](/rabin-karp)
    -   Rabin-Karp 法は Aho-Corasick 法と並んで競技プログラミングでよく利用される複数パターン文字列検索アルゴリズムである。

## 外部リンク

-   [Aho-Corasick法 - Algoogle](https://algoogle.hadrori.jp/algorithm/aho-corasick.html)<sup>[archive.org](https://web.archive.org/web/20210311070301/https://algoogle.hadrori.jp/algorithm/aho-corasick.html)</sup>
    -   <a class="handle">hadrori</a> による実装例。図付きでの解説もある。
-   [競技プログラミングにおける文字列アルゴリズム問題まとめ - はまやんはまやんはまやん](https://blog.hamayanhamayan.com/entry/2017/03/25/005452)<sup>[archive.org](https://web.archive.org/web/20210402112827/https://blog.hamayanhamayan.com/entry/2017/03/25/005452)</sup>
    -   <a class="handle">hamayanhamayan</a> によるブログ記事。例題が列挙されている。
