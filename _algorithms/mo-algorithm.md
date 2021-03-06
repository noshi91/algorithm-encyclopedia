---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers:
    date: 2020-07-09T00:00:00+09:00
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: "クエリ平方分割"
  level: orange
description: >
  Mo's algorithm とは、群 $G$ の要素の列 $(a_0, a_1, \dots, a _ {N-1})$ と区間の列 $\lbrack l_0, r_0), \lbrack l_1, r_1), \dots, \lbrack l _ {Q-1}, r _ {Q-1})$ が与えられたとき、それぞれの区間中の要素の総和 $\sum _ {i \in \lbrack l_j, r_j)} a_i$ を全体で $O(N \sqrt{Q})$ あるいは $O((N + Q) \sqrt{N})$ で求めるアルゴリズムである。ただし、その計算の過程において、群の演算 $\cdot$ が要素 $A \in G$ と添字 $i$ に対し $A \cdot a_i, A \cdot a_i^{-1}, a_i \cdot A, a_i^{-1} \cdot A$ のいずれかの形でしか出現しないという特徴がある。
draft: true
draft_urls: ["https://snuke.hatenablog.com/entry/2016/07/01/000000", "https://ei1333.hateblo.jp/entry/2017/09/11/211011"]
---

# Mo's algorithm
