---
layout: entry
authors: kimiyuki
reviewers: noshi91
date: 2021-02-23T00:00:00+09:00
updated_at:
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: ["dynamic programming", "DP"]
  level: green
description: 動的計画法とは、アルゴリズムの分類のひとつ。対象となる問題を複数の部分問題に分割して、部分問題の答えを記録しながらそのすべてを解くという形のアルゴリズムの総称である。動的計画法に分類されるようなアルゴリズムの実装方法の典型例として、配列をループで埋めていく実装や、メモ化を伴なう再帰による実装がある。
---

# 動的計画法

## 概要

動的計画法 (dynamic programming; DP) はアルゴリズムの分類のひとつである。対象となる問題を複数の部分問題に分割し、部分問題の答えを記録しながらそのすべてを解くという形のアルゴリズムたちを総称して動的計画法と呼ぶ。


## 分類

動的計画法に分類されるアルゴリズムたちは、さらに細かく分類することができる。また、そのような分類方法もまたいくつかに分類できる。

### 状態にもとづく分類

-   bit DP
    -   状態として bitset として表現された集合を持つ DP のこと。bitmask DP などとも呼ばれる。
-   区間 DP
    -   状態として区間を持つ DP のこと。
-   木 DP
    -   なにか根付き木を考え、状態としてその木の部分木を用いる DP のことを木 DP と呼ぶ。[木の畳み込み](https://en.wikipedia.org/wiki/Catamorphism#Tree_fold)などとも呼ばれる。
-   桁 DP
    -   状態に数字列の桁が関連するある種の DP のことを桁 DP と呼ぶ。明確な定義はなく、桁が関係していればすべて桁 DP だと考える人もいれば[^uwi-digits][^shojin-comp-digits]、構築途中の数字列がある値を越えるかどうかの判断を状態に含めることが重要だと考える人もいる[^kyort0n-digits]。
-   オートマトン DP
    -   なにかオートマトンを考え、状態としてそのオートマトンの状態を用いる DP のことをオートマトン DP と呼ぶ。
-   連結性 DP
    -   グラフの接続関係を状態とする DP のこと。 連結 DP や frontier DP や frontier 法風 DP などとも呼ばれる。
-   箱根駅伝 DP
    -   マッチング (あるいは順列) の個数を数える DP であって「ペアにするのを保留にしている要素の数」を状態の一部に用いる DP のこと。箱根 DP とも呼ばれる。

### 値にもとづく分類

-   確率 DP
    -   値が確率であるような DP のこと。
-   期待値 DP
    -   値が期待値であるような DP のこと。

### 漸化式や実装方法にもとづく分類

-   配る DP
    -   更新する側に注目して書いた漸化式にもとづいて実装される DP のこと。
-   貰う DP
    -   更新される側に注目して書いた漸化式にもとづいて実装される DP のこと。
-   in-place DP
    -   DP テーブルを in-place に更新していく DP のこと。セグメント木や convex hull trick を使って高速化できることがある。そこで使われる DP の高速化手法のみを指して in-place DP と呼ばれることもあり、その場合は実家 DP やインライン DP とも呼ばれる。
-   戻す DP
    -   漸化式を逆向きに使って更新し、なにかを使わなかった場合の値を求めるような DP のこと。DP の高速化手法のひとつ。
-   挿入 DP
    -   列を状態とし、その列に要素を挿入することを遷移とするような DP のこと。逆に抜いていく場合もある。
-   二乗の木 DP
    -   ある種の木 DP を指す。時間計算量が一見 $O(N^3)$ に見えるが実は $O(N^2)$ になっていることから名前が付いた。
-   rerooting
    -   木 DP をした結果をもとに、すべての頂点についてその頂点を根だとした場合の値を求める DP のこと。全方位木 DP とも呼ばれる。
-   Monge DP
    -   Monge 性を利用する DP の高速化手法のひとつ。あるいはそれを利用した結果のこと。Knuth optimization とか Knuth-Yao speedup とも呼ばれる。
-   Alien DP
    -   辺の重みが特定の条件[^snuke-alien]を満たす DAG 上の $2$ 点対間 $k$ 辺最短経路問題のアルゴリズムのこと。二分探索を利用する[^yosupo-alien]。またはこれに帰着して解ける DP のこと。中国では WQS Binary Search と呼ばれているとのことである。


## 関数の再帰的定義による理解

再帰的に定義された関数 $f : X \to Y$ をその定義に従って計算するとき、それぞれの $x \in X$ について $y = f(x)$ を記憶しておきちょうど一度のみ計算するようにすれば指数的な爆発を防げ、$O(\vert X \vert)$ 回の漸化式の計算で値が求まる。動的計画法とはこのような事実を利用したアルゴリズムのことである、という見方ができる[^kimiyuki-dp-recursion]。
このとき $X$ は状態の集合であり $Y$ は値の集合である。


## ループとメモ化再帰

動的計画法に分類されるようなアルゴリズムの実装方法の典型例として、配列をループで埋めていく実装や、メモ化を伴なう再帰による実装がある。
ただし、競技プログラミングの界隈においては、特に配列をループで埋めていく実装のみを指して動的計画法と呼ばれることもある[^chokudai-memoization]。


## 配る DP と貰う DP

ほとんどの場合、DP はその漸化式をどのように実装するかによって、貰う DP か配る DP のどちらかに分類できる。

$y = f(x_0, x_1, x_2, \dots)$ という形で書かれた漸化式をそのまま用いるのが貰う DP である。
貰う DP の特徴としては、in-place DP などの形の高速化がしやすいことが挙げられる。

$y = f(x_0, x_1, x_2, \dots)$ という形で書かれた元々の漸化式を逆転させて、$x_0, x_1, x_2, \dots$ のそれぞれを主体として $y \gets g(y, x_0); y \gets g(y, x_1); y \gets g(y, x_2); \dots$ のような更新を行うことで $y$ を計算するのが配る DP である。
配る DP の特徴としては、遷移関係と処理の向きが一致しており考えやすいことや、添字に負数がでてきにくく実装しやすいことが挙げられる。


## その他

-   動的計画法は関数の再帰的定義と関係があり、再帰は帰納法と関係がある。帰納法においてはその仮定を強めることでむしろ証明がうまくいくことがあるが、動的計画法においても持つ状態や計算する範囲を増やすことで計算がうまくいくことがある。
-   確率は期待値の特殊な場合と見ることができるため、確率 DP も期待値 DP の特殊な場合だと考えることができる。確率 DP や期待値 DP に特有の技法として、「自己ループを確率分布の期待値で潰す[^furuya1223-loop]」や「十分小さい確率の遷移を無視する[^kuuso1-converge]」などがある。
-   戻す DP の亜種として、関係する要素の影響量や寄与度を計算して修正をする DP がある。
-   有限種類の (計算対象の) 状態を (DP の) 状態とする DP は [Ears](https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_d) という問題に由来して「耳 DP」と呼ばれることがある[^tempura-ears][^md19970824-ears]。
-   漸化式が規則的かつ線形になっている DP では、漸化式を行列と見て行列累乗で計算することができる。
-   すでに使った区間の集合を管理するような DP では、使った区間同士の間隔をできる限り未決定のままにしておくこと[^example-dwacon6th_prelims_e]や、区間の長さを降順で使うこと[^example-dwacon6th_prelims_e]などがよくある。


## 関連項目

-   [Dijkstra 法](/dijkstra)
    -   Dijkstra 法は動的計画法に分類される代表的なアルゴリズムのひとつである。


## 外部リンク

-   [プログラミングコンテストでの動的計画法 - SlideShare](https://www.slideshare.net/iwiwi/ss-3578511)<sup>[archive.org](https://web.archive.org/web/20200814003001/https://www.slideshare.net/iwiwi/ss-3578511)</sup>
    -   <a class="handle">iwiwi</a> による解説スライド
-   [DPの話 - aizuzia](https://tayama-2.hatenadiary.org/entry/20111210/1323502092)<sup>[archive.org](https://web.archive.org/web/20210107111902/https://tayama-2.hatenadiary.org/entry/20111210/1323502092)</sup>
    -   DP を DAG 上の最短経路を求めることに関連づけて説明した記事
-   [競技プログラミングにおける動的計画法更新最適化まとめ（CHT, MongeDP, AlianDP, インラインDP, きたまさ法, 行列累乗） - はまやんはまやんはまやん](https://blog.hamayanhamayan.com/entry/2017/03/20/234711)
    -   <a class="handle">hamayanhamayan</a> による DP の問題集
-   [「インラインDP」というテクニックに関して - skyaozoraの日記 - TopCoder部](http://topcoder.g.hatena.ne.jp/skyaozora/20171212/1513084670)
<sup>[archive.org](https://web.archive.org/web/20200113085207/http://topcoder.g.hatena.ne.jp/skyaozora/20171212/1513084670)</sup>
    -   <a class="handle">sky58</a> による in-place DP の高速化の解説記事。この記事が書かれる前は「実家 DP」と呼ばれていたが、この記事によって「インライン DP」で置き換えられたという経緯がある。なお、今ではこの呼び名も不適切だという指摘があり、主に「in-place DP」が代替として用いられている[^sky58-inplace]。
-   [戻すDP - sigma425のブログ](http://sigma425.hatenablog.com/entry/2015/07/31/121439)<sup>[archive.org](https://web.archive.org/web/20210209142104/http://sigma425.hatenablog.com/entry/2015/07/31/121439)</sup>
    -   <a class="handle">sigma425</a> による戻す DP の解説記事
-   [競技プログラミングにおける戻すDP問題 - はまやんはまやんはまやん](https://blog.hamayanhamayan.com/entry/2017/03/19/154334)<sup>[archive.org](https://web.archive.org/web/20210217130302/https://blog.hamayanhamayan.com/entry/2017/03/19/154334)</sup>
    -   <a class="handle">hamayanhamayan</a> による戻す DP の問題集
-   [International Olympiad in Informatics 2016: day2_3. Aliens](https://ioinformatics.org/files/ioi2016problem6.pdf)<sup>[archive.org](https://web.archive.org/web/20191021104945/https://ioinformatics.org/files/ioi2016problem6.pdf)</sup>
    -   Alien DP の語源となった IOI の問題
-   [AOJ 2439. 箱根駅伝](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2439)
    -   箱根駅伝 DP の語源となった AOJ の問題
-   [二乗の木 DP - (iwi) ｛ 反省します - TopCoder部](https://topcoder.g.hatena.ne.jp/iwiwi/20120428/1335635594)<sup>[archive.org](https://web.archive.org/web/20150920041654/https://topcoder.g.hatena.ne.jp/iwiwi/20120428/1335635594)</sup>
    -   <a class="handle">iwiwi</a> による二乗の木 DP の解説
-   [木と計算量 前編 〜O(N^2)とO(NK)の木DP〜 - あなたは嘘つきですかと聞かれたら「YES」と答えるブログ](https://snuke.hatenablog.com/entry/2019/01/15/211812)<sup>[archive.org](https://web.archive.org/web/20201211213146/https://snuke.hatenablog.com/entry/2019/01/15/211812)</sup>
    -   <a class="handle">snuke</a> による二乗の木 DP の解説
-   [AOJ 2439  箱根駅伝 (JAG 夏合宿 2012 day3a-F) (600 点) - けんちょんの競プロ精進記録](https://drken1215.hatenablog.com/entry/2019/10/05/173700)<sup>[archive.org](https://web.archive.org/web/20210102014812/https://drken1215.hatenablog.com/entry/2019/10/05/173700)</sup>
    -   <a class="handle">drken</a> による箱根駅伝 DP の解説


## 注釈

[^kimiyuki-dp-recursion]: <a class="handle">kimiyuki</a> による記事 [DPそのものとは何であるかを理解する - うさぎ小屋](https://kimiyuki.net/blog/2019/02/11/dp-itself/)<sup>[archive.org](https://web.archive.org/web/20210107131727/https://kimiyuki.net/blog/2019/02/11/dp-itself/)</sup>
[^furuya1223-loop]: <a class="handle">furuya1223</a> によるツイート <https://twitter.com/furuya1223/status/1189903074107654145><sup>[archive.org](https://web.archive.org/web/20191031141515/https://twitter.com/furuya1223/status/1189903074107654145)</sup>
[^kuuso1-converge]: <a class="handle">kuuso</a> によるツイート <https://twitter.com/kuuso1/status/1189904707067600901><sup>[archive.org](https://web.archive.org/web/20191031142007/https://twitter.com/kuuso1/status/1189904707067600901)</sup>
[^uwi-digits]: <a class="handle">uwi</a> によるツイート <https://twitter.com/uwitenpen/status/1229100036450996224><sup>[archive.org](https://web.archive.org/web/20200216180244if_/https://twitter.com/uwitenpen/status/1229100036450996224)</sup>
[^shojin-comp-digits]: <https://twitter.com/shojin_comp/status/1229099045475344384><sup>[archive.org](https://web.archive.org/web/20210217113914/https://twitter.com/shojin_comp/status/1229099045475344384<Paste>)</sup>
[^kyort0n-digits]: <a class="handle">kort0n</a> によるツイート <https://twitter.com/kyort0n/status/1229096380431396864><sup>[archive.org](https://web.archive.org/web/20200216174335/https://twitter.com/kyort0n/status/1229096380431396864)</sup>
[^sky58-inplace]: <a class="handle">sky58</a> によるツイート <https://twitter.com/skyaozora/status/1177173768738705408><sup>[archive.org](https://web.archive.org/web/20190926110305/https://twitter.com/skyaozora/status/1177173768738705408)</sup>
[^tempura-ears]: <a class="handle">tempura0224</a> によるツイート <https://twitter.com/tempura_cpp/status/1177147483010387968><sup>[archive.org](https://web.archive.org/web/20210217132148/https://twitter.com/tempura_cpp/status/1177147483010387968)</sup>
[^md19970824-ears]: <a class="handle">kanra824</a> によるツイート <https://twitter.com/Md19970824/status/1254015456362459137><sup>[archive.org](https://web.archive.org/web/20200504062557/https://twitter.com/Md19970824/status/1254015456362459137)</sup>
[^example-dwacon6th_prelims_e]: 例題: <https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_e>
[^chokudai-memoization]: <a class="handle">chokudai</a> によるツイート <https://twitter.com/chokudai/status/1010049288460570624><sup>[archive.org](https://web.archive.org/web/20210217134038/https://twitter.com/chokudai/status/1010049288460570624)</sup>
[^snuke-alien]: <a class="handle">snuke</a> によるツイート <https://twitter.com/snuke_/status/928314561890959360><sup>[archive.org](https://web.archive.org/web/20210221081356/https://twitter.com/snuke_/status/928314561890959360)</sup>
[^yosupo-alien]: <a class="handle">yosupo</a> によるツイート <https://twitter.com/yosupot/status/928313911891214336><sup>[archive.org](https://web.archive.org/web/20210221064608/https://twitter.com/yosupot/status/928313911891214336)</sup>
