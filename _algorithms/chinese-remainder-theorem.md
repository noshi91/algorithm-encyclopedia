---
layout: entry
authors:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
tags: algorithm
algorithm:
  input: パターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ とテキスト文字列 $T$
  output: パターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ のどれがテキスト文字列 $T$ に含まれるか。含まれるならその位置も
  time_complexity: 前処理には $O(\sum \vert P_i \vert)$ で検索には $O(\vert T \vert)$
  space_complexity:
  aliases: ["中国人剰余定理", "CRT"]
  level: blue
description: 中国剰余定理とは、任意の互いに素な正整数 $m, n$ に対して、剰余群の直積群 $\mathbb{Z}/m \mathbb{Z} \times \mathbb{Z}/n \mathbb{Z}$ と剰余群 $\mathbb{Z}/ m n \mathbb{Z}$ とが同型である、という定理のこと。あるいは同じことだが、任意の互いに素な正整数 $m, n$ および任意の整数 $a, b$ に対して、ある整数 $x$ が $m n$ を法として一意に存在して、$x \equiv a \pmod{m}$ かつ $x \equiv b \pmod{n}$ を満たす、という定理のこと。
draft: true
draft_urls: ["http://elliptic-shiho.hatenablog.com/entry/2016/04/03/020117", "https://qiita.com/drken/items/ae02240cd1f8edfc86fd"]
---

# 中国剰余定理
