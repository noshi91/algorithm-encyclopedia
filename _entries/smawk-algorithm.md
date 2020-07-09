---
layout: entry
author: kimiyuki
reviewers:
date: 2020-07-09T00:00:00+09:00
updated_at:
tags: algorithm smawk-algorithm monotone-minima
algorithm:
  input: totally monotone な $H \times W$ 行列 $f$
  output: 各行 $y$ に対し最小値の位置 $x \in \mathrm{argmin} _ x f(y, x)$
  time_complexity: $O(H + W)$
  space_complexity:
  aliases: "TM minima"
description: SMAWK algorithm とは、totally monotone な $H \times W$ 行列に対しその各行の最小値を $O(H + W)$ で求めるアルゴリズムである。
draft: true
draft_urls: "https://topcoder-g-hatena-ne-jp.jag-icpc.org/spaghetti_source/20120923/1348327542.html"
---

# SMAWK algorithm
