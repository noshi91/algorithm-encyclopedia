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
  project selection problem は最小カット問題に帰着できる問題のひとつ。
---

# project selection problem

## 概要

project selection problem とは、次の形の問題である:

-   $N$ 個のプロジェクト $x_0, x_1, x_2, \dots, x _ {N-1}$ と $M$ 個の機械 $y_0, y_1, y_2, \dots, y _ {M-1}$ がある。
    プロジェクト $x_i$ を実行すると利益 $a_i$ 円 ($a_i \ge 0$) を産む。
    機械 $y_j$ は購入に費用 $b_j$ 円 ($b_j \ge 0$) かかる。
    さらに、プロジェクト $x _ {c_k}$ を実行するためは機械 $y _ {d_k}$ が購入されていなければならないという形の条件が $K$ 個与えらている。
    ただし機械は複数のプロジェクト間で共有できる。
    実行するプロジェクトと購入する機械を適切に選択したときの利益の最大値を求めよ。


## 最小カット問題への帰着

project selection problem はある $N + M + 2$ 頂点 $N + M + K$ 辺のネットワークを考えることで[最小カット問題](/minimum-cut-problem)に帰着できる。
$N$ 個のプロジェクトと $M$ 個の機械をそれぞれ頂点とし、始点 $s$ および終点 $t$ を追加する。
始点 $s$ からプロジェクト $x_i$ の頂点へ容量 $a_i$ の辺を張り、機械 $y_j$ の頂点から終点 $t$ へ容量 $b_j$ の辺を張り、それぞれの制約 $k$ ごとにプロジェクト $x _ {c_k}$ の頂点から機械 $y _ {d_k}$ の頂点へ容量無限大の辺を張る[^infinity-capacity]。
こうしてできるネットワーク上での最小カットの容量を $F$ とすると project selection problem の答えは $\sum_i a_i - F$ となる。
このネットワークを図示すると以下のようになる。

![project selection problem のネットワーク](assets/img/project-selection-problem.svg)


## 関連項目

-   [最小カット問題](/minimum-cut-problem)
    -   project selection problem は最小カット問題へと帰着できる。
-   [燃やす埋める問題](/moyasu-umeru-mondai)
    -   燃やす埋める問題は project selection problem と同じく最小カット問題に帰着できる問題のひとつである。


## 外部リンク

-   [『燃やす埋める』と『ProjectSelectionProblem』 - とこはるのまとめ](http://tokoharuland.hateblo.jp/entry/2017/11/12/234636)<sup>[archive.org](https://web.archive.org/web/20210401023114/http://tokoharuland.hateblo.jp/entry/2017/11/12/234636)</sup>
    -   <a class="handle">tokoharu</a> によるブログ記事。燃やす埋める問題という問題ではなく project selection problem という別の問題を利用することを提案している。
-   [最小カットを使って「燃やす埋める」問題を解くスライドのフォロー - じじいのプログラミング](https://shindannin.hatenadiary.com/entry/2017/11/15/043009)<sup>[archive.org](https://web.archive.org/web/20210401023113/https://shindannin.hatenadiary.com/entry/2017/11/15/043009)</sup>
    -   <a class="handle">shindannin</a> によるブログ記事。燃やす埋める問題と project selection problem とを比較している。


## 注釈

[^infinity-capacity]: ネットワークや最小カット問題の通常の定義では容量無限大の辺は許容されない。より正確には、入力の他の部分に依存する充分大きな数 $C$ をとって、容量無限大の辺の代わりに容量 $C$ の辺を張る。
