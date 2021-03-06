---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers:
    date: 2021-02-05T00:00:00+09:00
algorithm:
  input: 文字列 $S$
  output: すべての $i$ について、$S$ における $i$ 番目の文字を中心とする最長の回文の半径
  time_complexity: $O(\vert S \vert)$
  space_complexity:
  aliases: []
  level: blue
description: |
  Manacher 法とは、与えられた文字列 $S$ に対して、そのすべての位置 $i$ (ただし $0 \le i \lt \vert S \vert$) について「$S$ における $i$ 番目の文字を中心とする最長の回文の半径」をまとめて $O(\vert S \vert)$ で求めるアルゴリズムのひとつ。そのままでは奇数長の回文についてのみしか求まらない。偶数長の回文についても求めたいときは、$S$ の各文字の間にダミーの文字列を計 $\vert S \vert - 1$ 個挿入してできる文字列 $S'$ に対してもう一度 Manacher 法をすることになる。
draft: true
draft_urls: ["https://snuke.hatenablog.com/entry/2014/12/02/235837"]
---

# Manacher 法

## 参考文献

-   Glenn Manacher. 1975. A New Linear-Time ``On-Line'' Algorithm for Finding the Smallest Initial Palindrome of a String. J. ACM 22, 3 (July 1975), 346–351. DOI:<https://doi.org/10.1145/321892.321896>
    -   Manacher による最初の論文
-   Alberto Apostolico, Dany Breslauer, Zvi Galil, "Parallel detection of all palindromes in a string", Theoretical Computer Science, Volume 141, Issues 1–2, 1995, Pages 163-173, ISSN 0304-3975, <https://doi.org/10.1016/0304-3975(94)00083-U>.
    -   Manacher の提案したアルゴリズムが現在の競プロ界隈で知られる形で使えることを示した論文

## 外部リンク

-   [文字列の頭良い感じの線形アルゴリズムたち２ - あなたは嘘つきですかと聞かれたら「YES」と答えるブログ](https://snuke.hatenablog.com/entry/2014/12/02/235837)
    -   snuke による解説。
-   [競技プログラミングにおける文字列アルゴリズム問題まとめ - はまやんはまやんはまやん](https://www.hamayanhamayan.com/entry/2017/03/25/005452)
    -   hamayanhamayan によるブログ記事。例題が列挙されている。
