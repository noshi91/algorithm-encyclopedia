---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers:
    date: 2020-07-09T00:00:00+09:00
algorithm:
  input: 整数と正整数の対の長さ $k$ の列 $((a_0, m_0), (a_1, m_1), \dots, (a _ {k-1}, m _ {k-1}))$ および正整数 $M$
  output: $\forall i. x \equiv a_i \pmod{m_i}$ を満たす $x$ を $M$ で割った余り $x \bmod M$
  time_complexity: $\bmod m_i$ および $\bmod M$ での演算を $O(1)$ と仮定して $O(k^2)$
  space_complexity:
  aliases:
  level: yellow
description: Garner 法とは、中国剰余定理で存在が示されるところの $\forall i. x \equiv a_i \pmod{m_i}$ を満たす整数 $x$ について、それを別の $M$ で割った余り $x \bmod M$ を求めるアルゴリズムである。計算の過程で現われる整数の大きさが $m_i$ や $M$ の $2$ 乗程度で抑えられることを特徴とする。
draft: true
draft_urls:
---

# Garner法
