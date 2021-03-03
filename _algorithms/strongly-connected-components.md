---
layout: entry
authors: udon1206
reviewers:
date: 2021-03-04T00:00:00+09:00
updated_at:
algorithm:
  input: 有向グラフ $G = (V, E)$
  output: $G = (V, E)$ の強連結成分
  time_complexity: $O(|V| + |E|)$
  space_complexity: $O(|V| + |E|)$
  aliases: []
  level: blue
description: 有効グラフ $G = (V, E)$ の強連結成分 $C \subset V$ は、$C$ の全ての頂点対 $u, v$ に対して互いに到達可能な極大集合である。空間計算量、時間計算量ともに $O(|V| + |E|)$ で構成することができる。
draft: false
draft_urls: []
---

# 強連結成分分解

## 概要
有効グラフ $G = (V, E)$ の強連結成分 $C \subset V$ は、$C$ の全ての頂点対 $u, v$ に対して互いに到達可能な極大集合である。接続する2頂点が $G$ の同じ強連結成分に属する全ての辺を縮約することで得られるグラフが有向非巡回グラフであるという性質がある。空間計算量、時間計算量ともに $O(|V| + |E|)$ で構成することができる。実際に構成するアルゴリズムとして、$G$ と $G$ の転置グラフ $G ^ {T} = (V, E ^ {T}),\  E ^ {T} = \lbrace (u,v) : (v, u) \in E \rbrace$ を深さ優先探索する方法[^mathtrain]と、lowlinkに着目して、構成する方法[^acl]がある。


## 注釈
[^mathtrain]: <https://mathtrain.jp/kyorenketsu>
[^acl]: [AtCoder Library](https://github.com/atcoder/ac-library) の実装はこちらになっている。