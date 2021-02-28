---
layout: entry
authors:
reviewers:
date: 2021-01-23T00:00:00+09:00
updated_at:
algorithm:
  input: 長さ $N$ のソート済みの列 $a$ と検索対象の要素 $b$
  output: $b$ が含まれる位置 $i$。あるいは、$b$ を挿入してもソート済みのまま保たれるような区間 $\lbrack l, r)$
  time_complexity: $O(\log N)$ など
  space_complexity:
  aliases: bisection
  level: green
description: 二分探索とは、ソート済みの列に対する探索アルゴリズムのひとつ。探索すべき区間の中央の要素を調べることで探索すべき区間の長さを半々にし、区間の長さ $N$ に対し $O(\log N)$ で位置を特定する。
draft: true
draft_urls: ["https://twitter.com/meguru_comp/status/697008509376835584"]
---

# 二分探索

## 話題

-   めぐる式
-   浮動小数点数の場合
-   標準ライブラリ内の関数
-   二分法との違い
-   現実での利用例: git bisect (開発)
-   現実での利用例: LSB Decryption Oracle Attack (CTF)
