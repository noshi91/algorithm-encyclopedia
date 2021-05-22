---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers: MiSawa
    date: 2021-02-28T00:00:00+09:00
  - summary: 記事作成
    authors: kimiyuki
    reviewers:
    date: 2021-05-22T00:00:00+09:00
tags: algorithm
algorithm:
  input: |
    有向グラフ $G = (V, E)$ と頂点に対する評価関数 $\varphi : V \to \mathbb{R}$ と初期解 $x_0 \in V$ と終了時刻 $t_e$
  output: 解 $x \in V$
  time_complexity:
  space_complexity:
  aliases: []
  level: yellow
description: |
  山登り法はグラフ探索アルゴリズムのひとつである。与えられた評価関数 $\varphi : V \to \mathbb{R}$ の値が大きいような解 $x \in V$ を、暫定解を貪欲に更新することでヒューリスティックに求める。
---

# 山登り法

## 概要

山登り法はグラフ探索アルゴリズムのひとつである。
与えられた評価関数 $\varphi : V \to \mathbb{R}$ の値が大きいような解 $x \in V$ を、暫定解を貪欲に更新することでヒューリスティックに求める。

探索はあらかじめ決められた時間だけ行われ、その時点の暫定解が出力となる。
必ずしも $\varphi(x)$ の値が最大 (あるいは極大) となる解 $x \in V$ を出力するとは限らない。

## 詳細

山登り法は次のような疑似コードで定義される。

```plaintext-katex
$\mathtt{HillClimbing}(G, \varphi, x_0, t_e)$
 1. // 入力: 有向グラフ $G = (V, E)$、評価関数$\varphi : V \to \mathbb{R}$、初期解 $x_0 \in V$、終了時刻 $t_e$
 2. // 出力: 解 $x \in V$
 3. $x \gets x_0$
 4. $\mathtt{while}$ 現在時刻 $t$ が $t \lt t_e$:
 5.     $(x, y) \in E$ であるような頂点 $y \in V$ をランダムにひとつ選ぶ。
 6.     $\mathtt{if}$ $\varphi(x) \le \varphi(y)$:
 7.         $x \gets y$
 8. $\mathtt{return}$ $x$
```

## 関連項目

-   [焼きなまし法](/#simulated-annealing)
    -   山登り法を修正して評価が悪化するような遷移も確率的に行うようにしたものが焼きなまし法である。
