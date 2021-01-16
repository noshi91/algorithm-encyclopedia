---
layout: entry
author: kimiyuki
reviewers:
date: 2020-01-16T00:00:00+09:00
updated_at:
tags: tenkei dp
description: 桁 DP とは、自然数の \(10\) 進数展開などを桁ごとに決定していくような DP のこと。状態の持ちかたによる DP の分類のひとつ。
draft: true
draft_urls: []
---

# 桁 DP

桁 DP とは、自然数の \(10\) 進数展開などを桁ごとに決定していくような DP のこと。おそらくは状態の持ちかたによる DP の分類のひとつ。

特に「自然数 $n \lt L$ であって条件 $\varphi(n)$ を満たすものの個数を求めよ」のような形式の問題の際によく現れる。
このときは「現時点までずっと $L$ と一致している」場合の (あるひとつの) 値と「もう $L$ より真に小さいことが確定した」場合の値たちとを管理すればよい。

## 例題

-   [AtCoder Beginner Contest 129: E - Sum Equals Xor](https://atcoder.jp/contests/abc129/tasks/abc129_e)


## 厳密な定義について

厳密な定義はかなり揺れる。構成途中の文字列を状態とする DP や、数字列 (あるいは記号の種類数が少ない文字列) 上のオートマトン DP と理解されることもある。 「境界となる自然数 $N より小さくなることが確定したか」のフラグを状態とする DP だと言う人もいる。


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">桁dpって「この値を超えることが確定していますか?」を状態に持つのが最大の特徴だと思っていて、これがあるかどうかが僕の中では桁dpと認識するかどうかの判定基準になっています</p>&mdash; こるとん (@kyort0n) <a href="https://twitter.com/kyort0n/status/1229096380431396864?ref_src=twsrc%5Etfw">February 16, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">桁でDPすれば何でも桁DPでは(前処理用に上限設けずにやる系も含めて)</p>&mdash; 有為 (@uwitenpen) <a href="https://twitter.com/uwitenpen/status/1229100036450996224?ref_src=twsrc%5Etfw">February 16, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">桁DPは単に数字列のオートマトン上でのDP全般だろ...</p>&mdash; 精進 (@shojin_comp) <a href="https://twitter.com/shojin_comp/status/1229099045475344384?ref_src=twsrc%5Etfw">February 16, 2020</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
