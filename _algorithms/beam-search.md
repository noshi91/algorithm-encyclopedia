---
layout: entry
changelog:
  - summary: 見出し作成
    date: 2021-02-28T00:00:00+09:00
    authors: kimiyuki
    reviewers: MiSawa
  - summary: 記事作成
    date: 2021-05-22T00:00:00+09:00
    authors: kimiyuki
    reviewers:
tags: algorithm
algorithm:
  input: |
    有向グラフ $G = (V, E)$ と評価関数 $\varphi : V \to \mathbb{R}$ と初期状態 $x_0 \in V$ と深さ $h \in \mathbb{N}$ と幅 $w \in \mathbb{N}$
  output: 解 $x \in V$
  time_complexity:
  space_complexity:
  aliases: []
  level: yellow
description: |
  ビームサーチはグラフ探索アルゴリズムのひとつである。与えられたグラフ (たいてい DAG) を初期状態となる頂点群から幅優先探索と同様に探索していくが、定数 $K$ と頂点に対する評価関数 $\varphi : V \to \mathbb{R}$ をあらかじめ固定しておき、各深さごとにその評価関数による評価値が高い順に $K$ 個のみを保持してそれ以外の頂点は無視する。
---

# ビームサーチ

## 概要

ビームサーチはグラフ探索アルゴリズムのひとつである。
与えられたグラフ (たいてい DAG) を初期状態となる頂点群から幅優先探索と同様に探索していくが、定数 $K$ と頂点に対する評価関数 $\varphi : V \to \mathbb{R}$ をあらかじめ固定しておき、各深さごとにその評価関数による評価値が高い順に $K$ 個のみを保持してそれ以外の頂点は無視する。
$K = 1$ のときは貪欲法と一致する。

## 詳細

ビームサーチは次のような疑似コードで定義される。

```plaintext-katex
$\mathtt{SimulatedAnnealing}(G, \varphi, x_0, h, w)$
 1. // 入力: 有向グラフ $G = (V, E)$、評価関数 $\varphi : V \to \mathbb{R}$、初期解 $x_0 \in V$、深さ $h \in \mathbb{N}$、幅 $h \in \mathbb{N}$
 2. // 出力: 解 $z \in V$
 3. $X \gets \lbrace x_0 \rbrace$
 4. $\mathtt{for}$ $i \in \lbrace 0, 1, 2, \dots, h - 1 \rbrace$:
 5.     $Y \gets \varnothing$
 6.     $\mathtt{for}$ $x \in X$:
 7.         $\mathtt{for}$ $y \in \lbrace y \mid (x, y) \in E \rbrace$:
 8.             $y \gets Y \cup \lbrace y \rbrace$
 9.     $Y$ の要素を $\varphi$ の順に並べ、上位 $w$ 個を残して他は削除する。
10.     $X \gets Y$
11. $X$ の要素を $\varphi$ の順に並べ、最大のものを $z$ とする。
12. $\mathtt{return}$ $z$
```

## その他

-   暫定解の集合 $X$ の中にほとんど同じような解ばかり含まれていると性能が悪化する。そのような解を削除して解の多様性を上げると性能が向上する。そのような削除の処理は重複除去と呼ばれる。

## 関連項目

-   [焼きなまし法](/#simulated-annealing)
    -   焼きなまし法はビームサーチと並んでヒューリスティックコンテストで頻繁に利用されるアルゴリズムである。

## 外部リンク

-   [ビームサーチは DP - びったんびったん](http://hakomof.hatenablog.com/entry/2018/12/06/000000)<sup>[archive.org](https://web.archive.org/web/20191206130137/http://hakomof.hatenablog.com/entry/2018/12/06/000000)</sup>
    -   <a class="handle">hakomo</a> によるブログ記事。
