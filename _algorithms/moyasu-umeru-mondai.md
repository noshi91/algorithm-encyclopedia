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
  燃やす埋める問題は最小カット問題に帰着できる問題のひとつである。
  ただし、これは競技プログラミングのコミュニティの中でだけ通用する用語であることに注意したい。
---

# 燃やす埋める問題

## 概要

競技プログラミングのコミュニティにおいて「燃やす埋める問題」という名前[^moyasu-umeru-local-name]で呼ばれている問題は、次のような形の問題である:

-   $N$ 個のゴミ $0, 1, 2, \dots, N - 1$ があり、それぞれについて「燃やす」か「埋める」かを選んで処理しなければならない。
    ゴミ $i$ は燃やすと $a_i$ 円 ($a_i \ge 0$) かかり埋めると $b_i$ 円 ($b_i \ge 0$) かかる。
    さらに、ゴミ $x_j$ を燃やしたときにゴミ $y_j$ を埋めると罰金として $c_j$ 円 ($c_j \ge 0$) かかるという形の条件が $K$ 個与えられている。
    このときゴミをすべて処理するのに必要な費用の最小値を求めよ。


## 最小カット問題への帰着

燃やす埋める問題はある $N + 2$ 頂点 $2N + K$ 辺のネットワークを考えることで[最小カット問題](/minimum-cut-problem)に帰着できる。
$N$ 個のゴミをそれぞれ頂点とし、始点 $s$ および終点 $t$ を追加する。
始点 $s$ からそれぞれのゴミ $i$ へ容量 $a_i$ の辺を張り、それぞれのゴミ $i$ から終点 $t$ へ容量 $b_i$ の辺を張り、それぞれの制約 $j$ ごとに頂点 $y_j$ から頂点 $x_j$ へ容量 $c_j$ の辺を貼る。
このネットワーク上での最小カットの容量は燃やす埋める問題の答えに等しい。
このネットワークを図示すると以下のようになる。

![燃やす埋める問題のネットワーク](assets/img/moyasu-umeru-mondai.svg)


## その他

-   広義には燃やす埋める問題は「選択肢とそれに関わる制約が与えられて最大化や最小化をする問題であって、最小カット問題へと帰着できるもの」を指すことがある。$s$-$t$ カットを頂点の部分集合 $A \subseteq V$ であって $s \in A$ かつ $t \in V \setminus A$ なものとして定義して最小カット問題を考えるとき、このような広義の燃やす埋める問題と最小カット問題とはほとんど区別が付かなくなる。


## 関連項目

-   [最小カット問題](/minimum-cut-problem)
    -   燃やす埋める問題は最小カット問題へと帰着できる。
-   [project selection problem](/project-selection-problem)
    -   project selection problem は燃やす埋める問題と比較されることが多い。


## 外部リンク

-   <del><a href="http://topcoder.g.hatena.ne.jp/CKomaki/20121019/1350663591">最小カット - CKomakiの日記 - TopCoder部</a></del> (Internet Archive にも保存されておらず現在は閲覧不能)
    -   <a class="handle">Komaki</a> によるブログ記事。燃やす埋める問題という問題はこの記事で提案されたようである。
-   [最小カットを使って「燃やす埋める問題」を解く - SlideShare](https://www.slideshare.net/shindannin/project-selection-problem)<sup>[archive.org](https://web.archive.org/web/20210401023045/https://www.slideshare.net/shindannin/project-selection-problem)</sup>
    -   <a class="handle">shindannin</a> によるスライド。燃やす埋める問題について分かりやすく説明している。


## 注釈

[^moyasu-umeru-local-name]: 競技プログラミングのコミュニティ外では通用しない名前であることに注意したい。
