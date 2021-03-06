---
layout: entry
authors:
reviewers:
date: 2021-02-05T00:00:00+09:00
updated_at:
algorithm:
  input: パターン文字列 $P$ とテキスト文字列 $T$
  output: パターン文字列 $P$ がテキスト文字列 $T$ に含まれるかどうか。含まれるならその位置も
  time_complexity: 前処理に $O(\vert P \vert)$ かつ検索に $O(\vert T \vert)$
  space_complexity:
  aliases: ["KMP法"]
  level: yellow
description: Knuth-Morris-Pratt法とは文字列検索アルゴリズムのひとつ。パターン文字列 $P$ の各 prefix について最長の border (prefix かつ suffix であるような文字列) を $O(\vert P \vert)$ で求めておくことで、与えられたテキスト文字列 $T$ に対する検索を $O(\vert T \vert)$ で行う。
draft: true
draft_urls: ["https://snuke.hatenablog.com/entry/2017/07/18/101026", "https://potetisensei.hatenablog.com/entry/2017/07/10/174908"]
---

# Knuth-Morris-Pratt法

## 関連項目

-   [Boyer-Moore法](/boyer-moore)
    -   Boyer-Moore 法は Knuth-Morris-Pratt 法と並んで競技プログラミングでよく用いられる単一パターン文字列検索アルゴリズムである。

## 外部リンク

-   [KMPのK - あなたは嘘つきですかと聞かれたら「YES」と答えるブログ](https://snuke.hatenablog.com/entry/2017/07/18/101026)<sup>[archive.org](https://web.archive.org/save/https://snuke.hatenablog.com/entry/2017/07/18/101026)</sup>
    -   snuke による解説。
-   [MP法とKMP法の違い - 生きたい](https://potetisensei.hatenablog.com/entry/2017/07/10/174908)<sup>[archive.org](https://web.archive.org/web/20200325162220/http://potetisensei.hatenablog.com/entry/2017/07/10/174908)</sup>
    -   potetisensei による解説。Morris-Pratt 法と Knuth-Morris-Pratt 法の違いについて説明されている。
-   [競技プログラミングにおける文字列アルゴリズム問題まとめ - はまやんはまやんはまやん](https://www.hamayanhamayan.com/entry/2017/03/25/005452)
    -   hamayanhamayan によるブログ記事。例題が列挙されている。
