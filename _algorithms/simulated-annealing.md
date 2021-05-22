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
    有向グラフ $G = (V, E)$ と頂点に対する評価関数 $\varphi : V \to \mathbb{R}$ と初期解 $x_0 \in V$ と終了時刻 $t_e$ と採択確率関数 $p : \mathbb{R} _ {\gt 0} \times \lbrack 0, 1 \rbrack \to \lbrack 0, 1 \rbrack$
  output: 解 $x \in V$
  time_complexity:
  space_complexity:
  aliases: []
  level: yellow
description: 焼きなまし法はグラフ探索アルゴリズムのひとつである。山登り法を改良したものであり、評価値が悪化する場合であっても、評価値の変化量と実行開始からの経過時刻などの関数として定まる確率に従ってランダムにそのような遷移を行う。これには局所最適解から抜け出す効果がある。
---

# 焼きなまし法

## 概要

焼きなまし法はグラフ探索アルゴリズムのひとつである。
山登り法を改良したものであり、評価値が悪化する場合であっても、評価値の変化量と実行開始からの経過時刻などの関数として定まる確率に従ってランダムにそのような遷移を行う。
これには局所最適解から抜け出す効果がある。


## 詳細

焼きなまし法は次のような疑似コードで定義される。
ただし採択確率関数 $p$ には定数 $k \in \mathbb{R} _ {\gt 0}$ を使って $p(\Delta, T) = \exp(k \Delta / T)$ と定義されるものを使うことが多い。

```plaintext-katex
$\mathtt{SimulatedAnnealing}(G, \varphi, x_0, t_e, p)$
 1. // 入力: 有向グラフ $G = (V, E)$、評価関数$\varphi : V \to \mathbb{R}$、初期解 $x_0 \in V$、終了時刻 $t_e$、採択確率関数 $p : \mathbb{R} _ {\gt 0} \times \lbrack 0, 1 \rbrack \to \lbrack 0, 1 \rbrack$
 2. // 出力: 解 $z \in V$
 3. $t_s \gets t$ (ただし $t$ は現在時刻)
 4. $x \gets x_0$
 5. $z \gets x$
 6. $\mathtt{while}$ 現在時刻 $t$ が $t \lt t_e$:
 7.     $T \gets 1 - \frac{t - t_s}{t_e - t_s}$
 8.     $(x, y) \in E$ であるような頂点 $y \in V$ をランダムにひとつ選ぶ。
 9.     $\varphi(x) \gt \varphi(y)$ のとき、真偽値 $q$ を確率 $p(\varphi(y) - \varphi(x), T)$ で真になるようにランダムに選ぶ。
10.     $\mathtt{if}$ $\varphi(x) \le \varphi(y)$ または $q$ が真:
11.         $x \gets y$
12.         $\mathtt{if}$ $\varphi(z) \lt \varphi(x)$:
13.             $z \gets x$
14. $\mathtt{return}$ $z$
```


## その他

-   焼きなまし法とビームサーチが両方使える問題においては、一般に焼きなまし法の方が良い解を出力することが多い。ただし解空間が広すぎる場合などにはビームサーチの方が良い解を出力することもある。
-   焼きなまし法の初期解には、貪欲法などの他のアルゴリズムから得られた解を利用してもよい。


## 関連項目

-   [山登り法](/#hill-climbing)
    -   山登り法を修正して評価が悪化するような遷移も確率的に行うようにしたものが焼きなまし法である。
-   [ビームサーチ](/#beam-search)
    -   焼きなまし法はビームサーチと並んでヒューリスティックコンテストで頻繁に利用されるアルゴリズムである。


## 外部リンク

-   [焼きなまし法のコツ Ver. 1.3 - じじいのプログラミング](https://shindannin.hatenadiary.com/entry/2021/03/06/115415)<sup>[archive.org](https://web.archive.org/web/20210313210319/https://shindannin.hatenadiary.com/entry/2021/03/06/115415)</sup>
    -   <a class="handle">shindannin</a> によるブログ記事。
-   [競技プログラミングにおいて焼きなまし法に堕ちずに落とすコツ - Qiita](https://qiita.com/tsukammo/items/b410f3202372fe87c919)<sup>[archive.org](https://web.archive.org/web/20210305024810/https://qiita.com/tsukammo/items/b410f3202372fe87c919)</sup>
    -   <a class="handle">tsukammo</a> による Qiita 記事。
