---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers:
    date: 2021-02-05T00:00:00+09:00
  - summary: 記事作成
    authors: kimiyuki
    reviewers: noshi91
    date: 2021-03-09T00:00:00+09:00
algorithm:
  input: $k$ 個のすべて長さが等しいパターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ およびテキスト文字列 $T$
  output: パターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ のどれがテキスト文字列 $T$ に含まれるか。含まれるならその位置も求める。
  time_complexity: 前処理には $O(\sum \vert P_i \vert)$ など、検索には平均 $O(\vert T \vert)$ など
  space_complexity:
  aliases: []
  level: blue
description: Rabin-Karp 法とは、複数のパターン文字列をまとめて扱える乱択の文字列検索アルゴリズムのひとつ。$k$ 個のパターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ のそれぞれについて $O(\sum \vert P_i \vert)$ などをかけてハッシュ値を求めておくことで、与えられたテキスト文字列 $T$ に対し平均 $O(\vert T \vert)$ などでこれらの検索ができる。ハッシュ関数は固定ではないが、ローリングハッシュが使われることが多い。
---

# Rabin-Karp 法

## 概要

Rabin-Karp 法とは、複数のパターン文字列をまとめて扱える乱択の文字列検索アルゴリズムのひとつ。$k$ 個のすべて長さが等しいパターン文字列 $P_0, P_1, P_2, \dots, P _ {k-1}$ が与えられたとき、性質の良いハッシュ関数 $H$ を用意しておき、パターン文字列のそれぞれについてハッシュ値 $H(P_0), H(P_1), H(P_2), \dots, H(P _ {k-1})$ を $O(\sum \vert P_i \vert)$ などをかけて求めておく。ただし、ハッシュ関数 $H$ の性質が良いとは、与えられた文字列 $T$ に対し、その長さ $\lvert P_i \rvert$ の部分文字列たちについて、それらのハッシュ値のすべてを高速に計算できるということである。このとき、与えられたテキスト文字列 $T$ に対し期待計算量 $O(\lvert T \rvert)$ などで検索ができる。誤検出の可能性を許容できるならば、ハッシュ値が一致したときの検証を省略して Monte Carlo アルゴリズムとすることで期待計算量 $O(\lvert T \rvert)$ にできる。ハッシュ関数は固定ではないが、ローリングハッシュが使われることが多い。

## 詳細

(省略)

## メモ

-   ローリングハッシュが文字列を多項式と見るものであることを思い出せば、Rabin-Karp 法は多項式 $f, g$ の等価性 $f = g$ を検査するために乱数 $r$ を用いて $f(r) = g(r)$ を計算しているものだと思うことができる。これには行列 $A, B$ の等価性 $A = B$ 検査の Monte Carlo アルゴリズム[^pfn-matrix-monte-carlo]との類似がある。
-   ハッシュ値が一致したときの検証を省略したとしても最悪計算量 $O(\lvert T \rvert)$ とまでは言えない。$T$ の部分文字列 $T'$ に対するハッシュ値 $H(T')$ をパターン文字列についてのハッシュ値 $H(P_0), H(P_1), H(P_2), \dots, H(P _ {k-1})$ と比較する必要があるが、ここにハッシュマップを使う必要があるため、最悪計算量は $O(\lvert T \rvert)$ より悪くなる。

## 参考文献

-   R. M. Karp and M. O. Rabin, "Efficient randomized pattern-matching algorithms," in IBM Journal of Research and Development, vol. 31, no. 2, pp. 249-260, March 1987, doi: [10.1147/rd.312.0249](https://doi.org/10.1147/rd.312.0249).
    -   Rabin-Karp 法が提案された論文。空間計算量が定数であることを強調しており、パターン文字列が複数の場合についての言及はない。ハッシュ値の衝突とそれによる厳密比較が発生するたびにハッシュ関数を選び直すことが提案されている。

## 関連項目

-   [Aho-Corasick 法](/aho-corasick)
    -   Aho-Corasick 法は Rabin-Karp 法と並んで競技プログラミングでよく利用される複数パターン文字列検索アルゴリズムである。

## 外部リンク

-   [競技プログラミングにおける文字列アルゴリズム問題まとめ - はまやんはまやんはまやん](https://www.hamayanhamayan.com/entry/2017/03/25/005452)
    -   <a class="handle">hamayanhamayan</a> によるブログ記事。例題が列挙されている。

## 注釈

[^pfn-matrix-monte-carlo]: [乱択アルゴリズム紹介(行列乗算の検査&amp;多項式等価性の検査) &#124; Preferred Networks Research &amp; Development](https://tech.preferred.jp/ja/blog/matrix-multiplication-and-polynomial-identity/)<sup>[archive.org](https://web.archive.org/web/20210110054323/https://tech.preferred.jp/ja/blog/matrix-multiplication-and-polynomial-identity/)</sup>
