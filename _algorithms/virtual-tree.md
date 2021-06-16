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
  time_complexity: $O(\lvert V \rvert)$ で構築できる。複数の頂点の部分集合 $X_0, X_1, \dots, X _ {Q - 1}$ のそれぞれについて構築する場合でも全体で $O(\lvert V \rvert + \sum _ i \lvert X_i \rvert)$ で構築可能である。
  space_complexity:
  aliases: ["virtual tree", "auxiliary tree"]
  level: orange
description: 与えられた根付き木 $T = (V, E; r)$ とその頂点の部分集合 $X \subseteq V$ に対し、$X$ に含まれる頂点同士の最小共通祖先関係を失わないように $T$ を圧縮して根付き木を作ることができる。なお、この木は日本の競技プログラミングの界隈では "auxiliary tree" と呼ばれることもあるが、この呼び方は推奨されない。
---

# 指定された頂点たちの最小共通祖先関係を保って木を圧縮してできる補助的な木

## 概要

与えられた根付き木 $T = (V, E; r)$ とその頂点の部分集合 $X \subseteq V$ が与えられたとき、$X$ に含まれる頂点同士の子孫/祖先関係や最小共通祖先関係を失わないように $T$ を圧縮してできる補助的な根付き木 $T'$ を考えると便利であることがある。
より正確には、$X$ に含まれる頂点の組 $(x, y) \in X^2$ のそれぞれに対してその最小共通祖先 $z = \mathrm{lca}(x, y)$ を考え、そのような頂点の全体 $V' = \lbrace \mathrm{lca}(x, y) \mid (x, y) \in X^2 \rbrace$ の間に元々の木 $T$ での子孫関係で辺を張ってできるものがその根付き木 $T' = (V', E'; r')$ である。

この木 $T'$ は $X$ の頂点をすべて含む (つまり $X \subseteq V'$)。
また $T'$ の任意の頂点 $x, y \in V'$ に対し、それらの $T$ における最小共通祖先とそれらの $T'$ における最小共通祖先とは一致する。
そしてこの木 $T'$ の頂点数は $2 \lvert X \rvert - 1$ 頂点以下になることが示せる。
この木の構築は単純な DFS を用いることで $O(\lvert V \rvert)$ 時間で可能である。

与えられた複数の頂点の部分集合 $X_0, X_1, \dots, X _ {Q - 1}$ のそれぞれに対しての $Q$ 個のこのような補助的な木をまとめて構成することも $K = \sum _ {i \lt Q} \lvert X_i \rvert$ に対し $O(\lvert V \rvert \log \lvert V \rvert + K \log K)$ 時間で可能である。
これには sparse table などによるクエリが定数時間の LCA および Euler tour technique を用いる。
頂点の部分集合 $X_i$ はオンラインに与えられても構わない。
また、LCA に構築が線型時間かつクエリが定数時間のものを用いれば $O(\lvert V \rvert + K \log K)$ 時間で、クエリがオフラインに与えられると仮定してバケットソートを利用すれば $O(\lvert V \rvert \log V + K)$ 時間で、これらの両方を用いれば $O(\lvert V \rvert + K)$ 時間での構築も可能である。

たとえば、図 1 のような根付き木 $T$ からその頂点の部分集合 $X = \lbrace 7, 9, 11, 13, 14 \rbrace$ による木を作ると図 2 のようになる。

<figure>
  <img src="assets/img/virtual-tree-example-in.svg">
  <figcaption>図 1. 元となる根付き木の例</figcaption>
</figure>
<figure>
  <img src="assets/img/virtual-tree-example-out.svg">
  <figcaption>図 2. 図 1 の根付き木から $X$ に属する頂点たちの最小共通祖先関係を保って木を圧縮してできる補助的な木</figcaption>
</figure>


## 詳細

複数のこの補助的な木をまとめて構成する場合の具体的な構成方法については [LCAをベースに構築するAuxiliary Treeのメモ - 日々ｄｒｄｒする人のメモ](https://smijake3.hatenablog.com/entry/2019/09/15/200200)<sup>[archive.org](https://web.archive.org/web/20210512172958/https://smijake3.hatenablog.com/entry/2019/09/15/200200)</sup> を参考のこと。


## その他

-   日本の競技プログラミングの界隈ではこの木が (固有名詞的に) "Auxiliary Tree" と呼ばれることがある。しかし "an auxiliary tree" とは日本語であれば「補助的な木」という程度の一般的な表現であり、これを特定の木の名前として利用することは推奨されない[^link-cut-auxiliary][^tmaehara-auxiliary]。
-   中国の競技プログラミングの界隈ではこの木は「虚树」や "Virtual Tree" と呼ばれているようである[^virtual-tree]。
-   英語圏の競技プログラミングの界隈においては統一された呼称はないようである[^uwi-survey]。


## 外部リンク

-   [LCAをベースに構築するAuxiliary Treeのメモ - 日々ｄｒｄｒする人のメモ](https://smijake3.hatenablog.com/entry/2019/09/15/200200)<sup>[archive.org](https://web.archive.org/web/20210512172958/https://smijake3.hatenablog.com/entry/2019/09/15/200200)</sup>
    -   <a class="handle">yaketake08</a> によるブログ記事。ある木 $T = (V, E)$ と複数の頂点の部分集合 $X_0, X_1, \dots, X _ {Q - 1}$ とが与えられたときに、それぞれの部分集合 $X_i$ に対する $Q$ 個の木をまとめて $K = \sum _ {i \lt Q} \lvert X_i \rvert$ に対し $O(\lvert V \rvert \log \lvert V \rvert + K \log K)$ で構築する方法を紹介している。
-   [虚树 - OI Wiki](https://oi-wiki.org/graph/virtual-tree/)<sup>[archive.org](https://web.archive.org/web/20210512172944/https://oi-wiki.org/graph/virtual-tree/)</sup>
    -   中国語の競技プログラミングの wiki。中国の競技プログラミングの界隈ではこの木が「虚树」や "virtual tree" と呼ばれていることが分かる。


## 注釈

[^tmaehara-auxiliary]: <a class="handle">tmaehara</a> によるツイート: <https://twitter.com/tmaehara/status/1391229611187441666>
[^link-cut-auxiliary]: たとえば link-cut 木の説明では preferred edges による paths を管理する木たちが "auxiliary trees" と呼ばれることもある (例: [Link/cut tree - Wikipedia](https://en.wikipedia.org/wiki/Link/cut_tree)<sup>[archive.org](https://web.archive.org/web/20210527151259/https://en.wikipedia.org/wiki/Link/cut_tree)</sup>)
[^virtual-tree]: ただし "virtual tree" という呼称が英語圏の競技プログラミングの界隈で利用されている様子はあまり見られない。"auxiliary tree" と同様に、この "virtual tree" という表現も「実質的な木」という程度の一般的な表現でしかなく、特定の木の名前として利用することは推奨されないものであるという可能性は高い。
[^uwi-survey]: <a class="handle">uwi</a> による調査: <https://github.com/kmyk/algorithm-encyclopedia/issues/165#issuecomment-850781687><sup>[archive.org](https://web.archive.org/web/20210616100742/https://github.com/kmyk/algorithm-encyclopedia/issues/165#issuecomment-850781687)</sup>
