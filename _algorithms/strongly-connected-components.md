---
layout: entry
changelog:
  - summary: 記事作成
    authors: udon1206
    reviewers: noshi91
    date: 2021-03-04T00:00:00+09:00
algorithm:
  input: 有向グラフ $G = (V, E)$
  output: $G = (V, E)$ の強連結成分分解
  time_complexity: $O(|V| + |E|)$
  space_complexity: $O(|V| + |E|)$
  aliases: []
  level: blue
description: 有向グラフ $G = (V, E)$ の強連結成分 $C \subset V$ は、全ての $(u, v) \in C^2$ について $u$ から $v$ へ到達可能な極大集合である。$G$ の全ての強連結成分は $V$ の分割になり、これを強連結成分分解と呼ぶ。空間計算量、時間計算量ともに $O(\lvert V \rvert + \lvert E \rvert)$ で構成することができる。
draft: false
draft_urls: []
---

# 強連結成分分解

## 概要
有向グラフ $G = (V, E)$ の強連結成分 $C \subset V$ は、全ての $(u, v) \in C^2$ について $u$ から $v$ へ到達可能な極大集合である。$G$ の全ての強連結成分は $V$ の分割になり、これを強連結成分分解と呼ぶ。空間計算量、時間計算量ともに $O(\lvert V \rvert + \lvert E \rvert)$ で構成することができる。実際に構成するアルゴリズムとして、$G$ と $G$ の転置グラフ $G ^ {\top} = (V, E ^ {\top}),\  E ^ {\top} = \lbrace (u,v) : (v, u) \in E \rbrace$ を深さ優先探索する方法[^mathtrain]と、lowlinkに着目して、構成する方法[^acl]がある。
接続する2頂点が $G$の同じ強連結成分に属する全ての辺を縮約することで得られるグラフが有向非巡回グラフであるという性質がある。


## 注釈
[^mathtrain]: [強連結成分分解の意味とアルゴリズム \| 高校数学の美しい物語](https://mathtrain.jp/kyorenketsu)
[^acl]: [AtCoder Library](https://github.com/atcoder/ac-library) の実装はこちらになっている。
