---
layout: entry
authors:
reviewers:
date: 2020-07-09T00:00:00+09:00
updated_at:
tags: algorithm weighted-union-heuristic
algorithm:
  input:
  output:
  time_complexity:
  space_complexity:
  aliases: マージテク デマテク "weighted-union heuristic"
  level: cyan
description: weighted-union heuristic とは、ふたつの集まりの間で要素を移動させてひとつにまとめる操作を繰り返す際に、常に要素が少ない方から多い方へと移すようにすると計算量が落ちるというテクである。具体的には、大きさ $a$ のものを大きさ $b$ のものへと $O(a)$ かけてマージし (中身を移し) て大きさ $a + b$ のものを作るという操作を使って、大きさの合計が $n$ であるようないくつかのものをひとつにマージしてまとめたいというような状況において、合計の計算量 $O(n \log n)$ でこれが可能である。データ構造をマージする一般的なテクとも呼ばれる。
draft: true
draft_urls: "https://web.archive.org/web/20181213115442/https://topcoder.g.hatena.ne.jp/iwiwi/20131226/1388062106"
---

# weighted-union heuristic 
