---
layout: entry
changelog:
  - summary: 記事作成
    authors: kimiyuki
    reviewers:
    date: 2021-04-01T00:00:00+09:00
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases:
  level: blue
description: >
  problem selection problem は最小カット問題に帰着できる問題のひとつである。
---

# project selection problem

## 概要

problem selection problem[^project-selection-problem-name] とは、次の形の問題である:

-   $N$ 個のプロジェクト $x_0, x_1, x_2, \dots, x _ {N-1}$ と $M$ 個の機械 $y_0, y_1, y_2, \dots, y _ {M-1}$ がある。
    プロジェクト $x_i$ を実行すると利益 $a_i$ 円を産む。
    機械 $y_i$ は購入に費用 $b_j$ 円かかる。
    さらに、プロジェクト $x _ {c_j}$ を実行するためは機械 $y _ {d_j}$ が購入されていなければならないという形の条件が $K$ 個与えらている。
    ただし機械は複数のプロジェクト間で共有できる。
    実行するプロジェクトと購入する機械を適切に選択したときの利益の最大値を求めよ。


## 最小カット問題への帰着

project selection problem はある $N + M + 2$ 頂点 $N + M + K$ 辺のネットワークを考えることで[最小カット問題](/minimum-cut-problem)に帰着できる。
$N$ 個のプロジェクトと $M$ 個の機械をそれぞれ頂点とし、始点 $s$ および終点 $t$ を追加する。

このネットワーク上での最小カットの容量を $F$ とすると project selection problem の答えは $F + \sum_i a_i$ となる。
このネットワークを図示すると以下のようになる。

![project selection problem のネットワーク](assets/img/project-selection-problem.svg)


## 関連項目

-   [最小カット問題](/minimum-cut-problem)
    -   project selection problem は最小カット問題へと帰着できる。
-   [燃やす埋める問題](/moyasu-umeru-mondai)
    -   project selection problem は燃やす埋める問題と比較されることが多い。


## 外部リンク

-   [『燃やす埋める』と『ProjectSelectionProblem』 - とこはるのまとめ](http://tokoharuland.hateblo.jp/entry/2017/11/12/234636)<sup>[archive.org](https://web.archive.org/web/20210401023114/http://tokoharuland.hateblo.jp/entry/2017/11/12/234636)</sup>
    -   <a class="handle">tokoharu</a> によるブログ記事。燃やす埋める問題という問題クラスではなく project selection problem という別の問題クラスを利用することを提案している。
-   [最小カットを使って「燃やす埋める」問題を解くスライドのフォロー - じじいのプログラミング](https://shindannin.hatenadiary.com/entry/2017/11/15/043009)<sup>[archive.org](https://web.archive.org/web/20210401023113/https://shindannin.hatenadiary.com/entry/2017/11/15/043009)</sup>
    -   <a class="handle">shindannin</a> によるブログ記事。燃やす埋める問題と project selection problem とを比較している。


## 注釈

[^project-selection-problem-name]: TODO: 出典を探す
