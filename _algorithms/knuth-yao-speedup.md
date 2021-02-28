---
layout: entry
authors:
reviewers:
date: 2020-07-09T00:00:00+09:00
updated_at:
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases:
  level: red
description: Knuth-Yao speedup とは、Monge な $N \times N$ 行列 $f$ に対して $\mathrm{dp}(l, r) = \min \lbrace \mathrm{dp}(l, m) + \mathrm{dp}(m + 1, r) \mid l \le m \lt r \rbrace + f(l, r)$ (ただし $l \le r$) で定まる関数 $\mathrm{dp}$ のグラフを $O(N^2)$ で求めるアルゴリズムである。
draft: true
draft_urls: "https://topcoder-g-hatena-ne-jp.jag-icpc.org/spaghetti_source/20120915/1347668163.html"
---

# Knuth-Yao speedup
