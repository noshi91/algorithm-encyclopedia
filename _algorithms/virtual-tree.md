---
layout: entry
changelog:
  - summary: "記事作成"
    authors: kimiyuki
    reviewers:
    date: 2021-05-13T00:00:00+09:00
algorithm:
  input: 根付き木 $T = (V, E; r)$ とその頂点の部分集合 $X \subseteq V$
  output: $X$ に含まれる頂点同士の関係を失わないように $T$ を圧縮してできる根付き木 $T'$
  time_complexity: $O(\lvert V \rvert \log \lvert V \rvert + \lvert X \rvert \log \lvert X \rvert)$ で構築できる
  space_complexity:
  aliases: ["virtual tree", "auxiliary tree"]
  level: orange
description: 与えられた根付き木 $T = (V, E; r)$ とその頂点の部分集合 $X \subseteq V$ が与えられたとき、$X$ に含まれる頂点同士の関係を失わないように $T$ を圧縮してできる根付き木 $T'$ を虚樹と呼ぶ。日本の競技プログラミングの界隈では "auxiliary tree" と呼ばれることもあるが、この呼び方は推奨されない。
---

# 虚樹

与えられた根付き木 $T = (V, E; r)$ とその頂点の部分集合 $X \subseteq V$ が与えられたとき、$X$ に含まれる頂点同士の関係を失わないように $T$ を圧縮してできる根付き木 $T'$ を虚樹と呼ぶ。
より正確には、$X$ に含まれる頂点の組 $(x, y) \in X^2$ のそれぞれに対してその最小共通祖先 $z = \mathrm{lca}(x, y)$ を考え、そのような頂点の全体 $V' = \lbrace \mathrm{lca}(x, y) \mid (x, y) \in V^2 \rbrace$ の間に元々の木 $T$ での子孫関係で辺を張ってできる根付き木が虚樹 $T' = (V', E'; r')$ である。
虚樹 $T'$ の頂点数は $2 \lvert X \rvert - 1$ 頂点以下になることが示せる。

虚樹の構築は Euler tour technique や sparse table などを用いることで
$O(\lvert V \rvert \log \lvert V \rvert + \lvert X \rvert \log \lvert X \rvert)$ で可能である。

たとえば、図 1 のような根付き木 $T$ からその頂点の部分集合 $X = \lbrace 7, 9, 11, 13, 14 \rbrace$ による虚樹を作ると図 2 のようになる。

<figure>
  <img src="assets/img/virtual-tree-example-in.svg">
  <figcaption>図 1. 元となる根付き木の例</figcaption>
</figure>
<figure>
  <img src="assets/img/virtual-tree-example-out.svg">
  <figcaption>図 2. 図 1 の根付き木から得られる虚樹</figcaption>
</figure>


## 詳細

具体的な構成方法については [LCAをベースに構築するAuxiliary Treeのメモ - 日々ｄｒｄｒする人のメモ](https://smijake3.hatenablog.com/entry/2019/09/15/200200)<sup>[archive.org](https://web.archive.org/web/20210512172958/https://smijake3.hatenablog.com/entry/2019/09/15/200200)</sup> を参考のこと。


## その他

-   日本の競技プログラミングの界隈では虚樹が (固有名詞的に) "Auxiliary Tree" と呼ばれることがある。しかし "an auxiliary tree" とは日本語であれば「補助的な木」という程度の一般的な表現であり、これを特定の木の名前として利用することは推奨されない[^link-cut-auxiliary][^tmaehara-auxiliary]。
-   中国の競技プログラミングの界隈では「虚树」や "virtual tree" と呼ばれているようである。ただし "virtual tree" という呼称が英語圏の競技プログラミングの界隈で利用されている様子はあまり見られない。


## 外部リンク

-   [LCAをベースに構築するAuxiliary Treeのメモ - 日々ｄｒｄｒする人のメモ](https://smijake3.hatenablog.com/entry/2019/09/15/200200)<sup>[archive.org](https://web.archive.org/web/20210512172958/https://smijake3.hatenablog.com/entry/2019/09/15/200200)</sup>
    -   <a class="handle">yaketake08</a> によるブログ記事。具体的な構成方法が図付きで説明されている。
-   [虚树 - OI Wiki](https://oi-wiki.org/graph/virtual-tree/)<sup>[archive.org](https://web.archive.org/web/20210512172944/https://oi-wiki.org/graph/virtual-tree/)</sup>
    -   中国語の競技プログラミングの wiki。中国の競技プログラミングの界隈では「虚树」や "virtual tree" と呼ばれていることが分かる。


## 注釈

[^tmaehara-auxiliary]: <a class="handle">tmaehara</a> によるツイート: <https://twitter.com/tmaehara/status/1391229611187441666>
[^link-cut-auxiliary]: たとえば link-cut 木の説明では prefereed edges による paths を管理する木たちが "auxiliary trees" と呼ばれることもある (例: [Link/cut tree - Wikipedia](https://en.wikipedia.org/wiki/Link/cut_tree)<sup>[archive.org](https://web.archive.org/web/20210527151259/https://en.wikipedia.org/wiki/Link/cut_tree)</sup>)
