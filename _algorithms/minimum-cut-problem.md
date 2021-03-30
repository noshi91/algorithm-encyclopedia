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
  aliases: ["minimum cut problem"]
  level: blue
description: >
  最小カット問題とは、与えられたネットワークのカットであって容量が最小のものを求めるという問題。
  最大流最小カット定理によって最小カット問題の解の容量は最大流問題の解の流量に等しい。
---

# 最小カット問題

## 概要

最小カット問題とは、与えられたネットワークのカットであって容量が最小のものを求めるという問題である。
最大流最小カット定理によって最小カット問題の解の容量は[最大流問題](/maximum-flow-problem)の解の流量に等しい。


## 燃やす埋める問題

競技プログラミングのコミュニティにおいて「燃やす埋める問題」という名前[^moyasu-umeru-local-name]で呼ばれている問題は、最小カット問題に帰着できる問題のひとつである。
これは次のような形の問題である:

-   $N$ 個のゴミ $0, 1, 2, \dots, N - 1$ があり、それぞれについて「燃やす」か「埋める」かを選んで処理しなければならない。
    ゴミ $i$ は燃やすと $a_i$ 円 ($a_i \ge 0$) かかり埋めると $b_i$ 円 ($b_i \ge 0$) かかる。
    さらに、ゴミ $x_j$ を燃やしたときにゴミ $y_j$ を埋めると罰金として $c_j$ 円 ($c_j \ge 0$) かかるという形の条件が $K$ 個与えられている。
    このときゴミをすべて処理するのに必要な費用の最小値を求めよ。

燃やす埋める問題はある $N + 2$ 頂点 $2N + K$ 辺のネットワークを考えることで最大流問題に帰着できる。
$N$ 個のゴミをそれぞれ頂点とし、始点 $s$ および終点 $t$ を追加する。
始点 $s$ からそれぞれのゴミ $i$ へ容量 $a_i$ の辺を張り、それぞれのゴミ $i$ から終点 $t$ へ容量 $b_i$ の辺を張り、それぞれの制約 $j$ ごとに頂点 $y_j$ から頂点 $x_j$ へ容量 $c_j$ の辺を貼る。
このネットワーク上での最小カットの容量は燃やす埋める問題の答えに等しい。
このネットワークを図示すると以下のようになる。

![燃やす埋める問題のネットワーク](assets/img/minimum-cut-problem-moyasu-umeru.svg)


## project selection problem

problem selection problem[^project-selection-problem-name] は最小カット問題に帰着できる問題のひとつである。
これは次のような形の問題である:

-   $N$ 個のプロジェクト $x_0, x_1, x_2, \dots, x _ {N-1}$ と $M$ 個の機械 $y_0, y_1, y_2, \dots, y _ {M-1}$ がある。
    プロジェクト $x_i$ を実行すると利益 $a_i$ 円を産む。
    機械 $y_i$ は購入に費用 $b_j$ 円かかる。
    さらに、プロジェクト $x _ {c_j}$ を実行するためは機械 $y _ {d_j}$ が購入されていなければならないという形の条件が $K$ 個与えらている。
    ただし機械は複数のプロジェクト間で共有できる。
    実行するプロジェクトと購入する機械を適切に選択したときの利益の最大値を求めよ。

project selection problem はある $N + M + 2$ 頂点 $N + M + K$ 辺のネットワークを考えることで 最大流問題に帰着できる。
$N$ 個のプロジェクトと $M$ 個の機械をそれぞれ頂点とし、始点 $s$ および終点 $t$ を追加する。

このネットワーク上での最小カットの容量を $F$ とすると project selection problem の答えは $F + \sum_i a_i$ となる。
このネットワークを図示すると以下のようになる。

![project selection problem のネットワーク](assets/img/minimum-cut-problem-project-selection-problem.svg)


## その他

-   $s$-$t$ カットは、有向辺の部分集合 $C \subseteq E$ であってどの $s$-$t$ パスも $C$ に含まれるような有向辺を含むものとして定義される場合[^cut-set-of-edges]と、頂点の部分集合 $A \subseteq V$ として定義される場合[^cut-set-of-vertices]とがある。カットの容量は、前者の定義の場合は $C$ に含まれる有向辺の重みの総和として定義され、後者の定義の場合は始点が $A$ に含まれる終点 $V \setminus A$ に含まれるような有向辺の重みの総和として定義される。最小カット問題を考える際にはどちらの定義を用いても解の容量は同じである。


## 関連項目

-   [最大流問題](/maximum-flow-problem)
    -   最大流最小カット定理によって最小カット問題の解の容量は最大流問題の解の流量に等しい。


## 外部リンク

-   <del>[最小カット - CKomakiの日記 - TopCoder部](http://topcoder.g.hatena.ne.jp/CKomaki/20121019/1350663591)</del> (Internet Archive にも保存されておらず現在は閲覧不能)
    -   <a class="handle">Komaki</a> によるブログ記事。燃やす埋める問題という問題はこの記事で提案されたようである。
-   [最小カットを使って「燃やす埋める問題」を解く - SlideShare](https://www.slideshare.net/shindannin/project-selection-problem)<sup>[archive.org](https://web.archive.org/web/20210401023045/https://www.slideshare.net/shindannin/project-selection-problem)</sup>
    -   <a class="handle">shindannin</a> によるスライド。燃やす埋める問題について分かりやすく説明している。
-   [最小カットについて - よすぽの日記](https://yosupo.hatenablog.com/entry/2015/03/31/134336)<sup>[archive.org](https://web.archive.org/web/20210401023012/https://yosupo.hatenablog.com/entry/2015/03/31/134336)</sup>
    -   <a class="handle">yosupo</a> によるブログ記事。最小カット問題はグラフの $2$ 彩色だと思うとよいことが説明されている。
-   [『燃やす埋める』と『ProjectSelectionProblem』 - とこはるのまとめ](http://tokoharuland.hateblo.jp/entry/2017/11/12/234636)<sup>[archive.org](https://web.archive.org/web/20210401023114/http://tokoharuland.hateblo.jp/entry/2017/11/12/234636)</sup>
    -   <a class="handle">tokoharu</a> によるブログ記事。燃やす埋める問題という問題クラスではなく project selection problem という別の問題クラスを利用することを提案している。
-   [最小カットを使って「燃やす埋める」問題を解くスライドのフォロー - じじいのプログラミング](https://shindannin.hatenadiary.com/entry/2017/11/15/043009)<sup>[archive.org](https://web.archive.org/web/20210401023113/https://shindannin.hatenadiary.com/entry/2017/11/15/043009)</sup>
    -   <a class="handle">shindannin</a> によるブログ記事。燃やす埋める問題と project selection problem とを比較している。
-   [最小カット問題と充足最大化問題 - うさぎ小屋](https://kimiyuki.net/blog/2020/03/07/minimum-cut-and-maximum-satisfiability/)<sup>[archive.org](https://web.archive.org/web/20210401023109/https://kimiyuki.net/blog/2020/03/07/minimum-cut-and-maximum-satisfiability/)</sup>
    -   <a class="handle">kimiyuki</a> によるブログ記事。最小カット問題は $\bigvee\mkern-12.5mu\bigvee _ i p_i \to \bigwedge\mkern-12.5mu\bigwedge _ j q_j$ の形の論理式たちの充足最大化問題と見ることができると主張している。
-   [燃やす埋める問題と劣モジュラ関数のグラフ表現可能性 その① - 私と理論](https://theory-and-me.hatenablog.com/entry/2020/03/13/180935)<sup>[archive.org](https://web.archive.org/web/20210401023205/https://theory-and-me.hatenablog.com/entry/2020/03/13/180935)</sup>
    -   <a class="handle">theory_and_me</a> によるブログ記事。TODO: ちゃんと読んでリンクするかどうか判断する + リンクするなら要約を書く
-   [燃やす埋める問題と劣モジュラ関数のグラフ表現可能性 その② グラフ構築編 - 私と理論](https://theory-and-me.hatenablog.com/entry/2020/03/17/180157)<sup>[archive.org](https://web.archive.org/web/20210401023147/https://theory-and-me.hatenablog.com/entry/2020/03/17/180157)</sup>
    -   <a class="handle">theory_and_me</a> によるブログ記事。TODO: ちゃんと読んでリンクするかどうか判断する + リンクするなら要約を書く
-   [燃やす埋める問題を完全に理解した話 - koyumeishiのブログ](https://koyumeishi.hatenablog.com/entry/2021/01/14/052223)<sup>[archive.org](https://web.archive.org/web/20210401023419/https://koyumeishi.hatenablog.com/entry/2021/01/14/052223)</sup>
    -   <a class="handle">koyumeishi</a> によるブログ記事。TODO: ちゃんと読んでリンクするかどうか判断する + リンクするなら要約を書く


## 注釈

[^moyasu-umeru-local-name]: 競技プログラミングのコミュニティ外では通用しない名前であることに注意したい。
[^project-selection-problem-name]: TODO: 出典を探す
[^cut-set-of-edges]: R. J. ウィルソン. グラフ理論入門. 近代科学社, 2001, [ISBN978-4-76-490296-1](https://iss.ndl.go.jp/api/openurl?isbn=9784764902961).
[^cut-set-of-vertices]: R. Diestel, [Graph Theory](https://www.springer.com/jp/book/9783662536216), 5th ed. Berlin Heidelberg: Springer-Verlag, 2017. TODO: そうらしいんだけど私はこの本を持ってないので noshi91 に確認する
