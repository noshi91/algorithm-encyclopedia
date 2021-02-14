---
layout: entry
authors: kimiyuki
reviewers:
date: 2020-01-16T00:00:00+09:00
updated_at:
algorithm:
  aliases: ["箱根DP", "箱根駅伝", "箱根"]
tags: tenkei dp
description: 区間の集合を構成するような DP であって「左端は決まったが右端はまだ決まってない区間の数」と「右端は決まったが左端はまだ決まってない区間の数」を状態とする DP のこと。
---

# 箱根駅伝 DP

箱根駅伝 DP とは、区間の集合を構成するような DP であって「左端は決まったが右端はまだ決まってない区間の数」と「右端は決まったが左端はまだ決まってない区間の数」を状態とする DP のこと。状態が何であるかに基づく DP の分類のひとつ。

## 例題

-   [AOJ 2439: 箱根駅伝](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2439)
    -   この問題が呼称の由来である。
-   [AtCoder Beginner Contest 134: F - Permutation Oddness](https://atcoder.jp/contests/abc134/tasks/abc134_f)
