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
  最大フロー最小カット定理によって最小カット問題の解の容量は最大フロー問題の解の流量に等しい。
---

# 最小カット問題

## 概要

最小カット問題とは、与えられたネットワークのカットであって容量が最小のものを求めるという問題である。
最大フロー最小カット定理によって最小カット問題の解の容量は[最大フロー問題](/maximum-flow-problem)の解の流量に等しい。


## カットの定義

与えられたネットワークの $s$-$t$ カットの定義としては、大きく分けて以下のみっつがある。

1.  有向辺の部分集合 $C \subseteq E$ であってどの $s$-$t$ パスも $C$ に含まれるような有向辺を含むもの[^cut-set-of-edges]
2.  頂点の部分集合 $S \subseteq V$ であって $s \in S$ かつ $t \in V \setminus S$ なもの[^cut-set-of-vertices]
3.  有向辺の部分集合 $C \subseteq E$ であって、次を満たすもの: ある頂点の部分集合 $S \subseteq V$ であって $s \in S$ かつ $t \in V \setminus S$ なものが存在し、$S$ に含まれる頂点から $V \setminus S$ に含まれる頂点への有向辺の全体が $C$ に等しい[^cut-set-of-vertices-as-edges]

カットの容量は、(1.) と (3.) の定義の場合は $C$ に含まれる有向辺の重みの総和として定義される。
(2.) の定義の場合は始点が $S$ に含まれかつ終点が $V \setminus S$ に含まれるような有向辺の重みの総和として定義される。

最小カット問題を考える際にはどの定義を用いても解の容量は同じであるが、カットの定義としてはすべて異なるものである。
(1.) の定義と (2.) の定義との違いはカットの容量の最大値について考えれば明らかである。
(2.) の定義と (3.) の定義とはほとんど同じものであるが、ネットワークが非連結な場合に異なってくる。
(1.) で定義されるものを (2.) や (3.) で定義されるものから区別したいときには、(1.) で定義されるものを $s$-$t$ 非連結化集合 ($s$-$t$ disconnecting) と呼ぶことがある[^s-t-disconnecting]。


## 関連項目

-   [最大フロー問題](/maximum-flow-problem)
    -   最大フロー最小カット定理によって最小カット問題の解の容量は最大フロー問題の解の流量に等しい。
-   [燃やす埋める問題](/moyasu-umeru-mondai)
    -   燃やす埋める問題は最小カット問題へと帰着できる。
-   [project selection problem](/project-selection-problem)
    -   project selection problem は最小カット問題へと帰着できる。


## 外部リンク

-   [最小カットについて - よすぽの日記](https://yosupo.hatenablog.com/entry/2015/03/31/134336)<sup>[archive.org](https://web.archive.org/web/20210401023012/https://yosupo.hatenablog.com/entry/2015/03/31/134336)</sup>
    -   <a class="handle">yosupo</a> によるブログ記事。最小カット問題はグラフの $2$ 彩色だと思うとよいことが説明されている。
-   [最小カット問題と充足最大化問題 - うさぎ小屋](https://kimiyuki.net/blog/2020/03/07/minimum-cut-and-maximum-satisfiability/)<sup>[archive.org](https://web.archive.org/web/20210401023109/https://kimiyuki.net/blog/2020/03/07/minimum-cut-and-maximum-satisfiability/)</sup>
    -   <a class="handle">kimiyuki</a> によるブログ記事。最小カット問題は $\bigvee\mkern-12.5mu\bigvee _ i p_i \to \bigwedge\mkern-12.5mu\bigwedge _ j q_j$ の形の論理式たちの充足最大化問題と見ることができると主張している。
-   [燃やす埋める問題と劣モジュラ関数のグラフ表現可能性 その① - 私と理論](https://theory-and-me.hatenablog.com/entry/2020/03/13/180935)<sup>[archive.org](https://web.archive.org/web/20210401023205/https://theory-and-me.hatenablog.com/entry/2020/03/13/180935)</sup>, [燃やす埋める問題と劣モジュラ関数のグラフ表現可能性 その② グラフ構築編 - 私と理論](https://theory-and-me.hatenablog.com/entry/2020/03/17/180157)<sup>[archive.org](https://web.archive.org/web/20210401023147/https://theory-and-me.hatenablog.com/entry/2020/03/17/180157)</sup>
    -   <a class="handle">theory_and_me</a> によるブログ記事。$3$ 変数までの劣モジュラ関数の和 $\sum_i \theta_i(x_i) + \sum _ {i \lt j} \phi _ {i, j} (x_i, x_j) + \sum _ {i \lt j \lt k} \psi _ {i, j, k} (x_i, x_j, x_k)$ で表される関数の最小化問題は最小カット問題に帰着できることを説明している。
-   [燃やす埋める問題を完全に理解した話 - koyumeishiのブログ](https://koyumeishi.hatenablog.com/entry/2021/01/14/052223)<sup>[archive.org](https://web.archive.org/web/20210401023419/https://koyumeishi.hatenablog.com/entry/2021/01/14/052223)</sup>
    -   <a class="handle">koyumeishi</a> によるブログ記事。$2$ 変数間の制約からグラフ表現可能な劣モジュラ関数を自動導出するライブラリを提案している。


## 注釈

[^moyasu-umeru-local-name]: 競技プログラミングのコミュニティ外では通用しない名前であることに注意したい。
[^cut-set-of-edges]: たとえば R. J. ウィルソン. グラフ理論入門. 近代科学社, 2001, [ISBN978-4-76-490296-1](https://iss.ndl.go.jp/api/openurl?isbn=9784764902961).
[^cut-set-of-vertices]: たとえば R. Diestel, [Graph Theory](https://www.springer.com/jp/book/9783662536216), 5th ed. Berlin Heidelberg: Springer-Verlag, 2017.
[^cut-set-of-vertices-as-edges]: たとえば Schrijver, A. [Combinatorial Optimization: Polyhedra and Efficiency](https://www.springer.com/jp/book/9783540443896), Springer Science &amp; Business Media, 2003.
[^s-t-disconnecting]: たとえば Schrijver, A. [Combinatorial Optimization: Polyhedra and Efficiency](https://www.springer.com/jp/book/9783540443896), Springer Science &amp; Business Media, 2003.
