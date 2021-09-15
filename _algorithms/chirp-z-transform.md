---
layout: entry
changelog:
  - summary: 記事作成
    authors: noshi91
    reviewers: []
    date: 2021-09-15T21:46:53+09:00
algorithm:
  input: 体 $\mathbb{K}$ 上の長さ $n$ の列 $x$、$a \in \mathbb{K}, w \in \mathbb{K}$、整数 $m$
  output: 各 $0 \leq k \lt m$ に対し、$X _ {k} = \sum _ {i = 0} ^ {n - 1} x _ {i} (a ^ {- 1} w ^ {k}) ^ {i}$
  time_complexity: $\mathrm{M}(n, n + m - 1) + \Theta(n + m)$
  space_complexity: $\mathrm{M}(n, n + m - 1) + \Theta(n + m)$
  aliases: ["Bluestein's algorithm", "chirp transform", "CZT"]
  level: red
description: >
    chirp z-transform は、数列の z-transform を等比数列を成す点で評価した値を計算するアルゴリズムの一つ。
    長さが $2$ の冪でない離散フーリエ変換の計算などに使用できる。
    時間計算量/空間計算量は、$\mathrm{M}(M, N)$ を長さ $M, N$ の列の畳み込みに必要な計算量として、$\mathrm{M}(n, n + m - 1) + \Theta(n + m)$ である。
---

# chirp z-transform

## 概要

chirp z-transform は、数列の Z 変換を等比数列を成す点で評価した値を計算するアルゴリズムの一つ。
長さが $2$ の冪でない離散フーリエ変換の計算などに使用できる。
時間計算量/空間計算量は、$\mathrm{M}(M, N)$ を長さ $M, N$ の列の畳み込みに必要な計算量として、$\mathrm{M}(n, n + m - 1) + \Theta(n + m)$ である。

$a$ が $- 1$ 乗がされているのは Z 変換に由来するもので、取り除けば多項式の多点評価と解釈できる ($a ^ {- 1}$ を $a$ と定義し直せば相互に変換可能である)。

## 詳細

$w = 0$ の場合は自明であるから、以降 $w \neq 0$ とする。

$t _ {i} \coloneqq \frac{i(i - 1)}{2}$ で三角数を定義すると、以下の等式が成り立つ。
$$
  ki = t _ {k + i} - t _ {k} - t _ {i}
$$

これを用いて $X _ {k}$ を変形すると以下のようになる。
$$ \begin{align*}
  X _ {k}
  &= \sum _ {i = 0} ^ {n - 1} x _ {i} (a ^ {- 1} w ^ {k}) ^ {i} \cr
  &= \sum _ {i = 0} ^ {n - 1} x _ {i} a ^ {- i} w ^ {ki} \cr
  &= \sum _ {i = 0} ^ {n - 1} x _ {i} a ^ {- i} w ^ {t _ {k + i}} w ^ {- t _ {k}} w ^ {- t _ {i}} \cr
  &= w ^ {- t _ {k}} \sum _ {i = 0} ^ {n - 1} (x _ {i} a ^ {- i} w ^ {- t _ {i}}) w ^ {t _ {k + i}}
\end{align*} $$
最後の式は畳み込みの形になっている。
実際、
$$ \begin{aligned}
  y _ {i} &\coloneqq x _ {i} a ^ {- i} w ^ {- t _ {i}} \cr
  v _ {i} &\coloneqq w ^ {t _ {i}}
\end{aligned} $$
と定義すれば
$$ \begin{align*}
  X _ {k}
  &= w ^ {- t _ {k}} \sum _ {i = 0} ^ {n - 1} y _ {i} v _ {k + i} \cr
  &= w ^ {- t _ {k}} \sum _ {i + j = n - 1 + k} y _ {n - 1 - i} v _ {j}
\end{align*} $$
となる。

関係式 $w ^ {t _ {i + 1}} = w ^ {t _ {i}} w ^ {i}$ を用いることで $y, v$ は $\Theta(n + m)$ で計算できる。
よって全体の計算量は、これに畳み込みに掛かる時間計算量を加えた $\mathrm{M}(n, n + m - 1) + \Theta(n + m)$ となる。

畳み込みの結果のうち第 $n - 1$ 項から第 $n + m - 2$ 項までを使用するため、畳み込みは長さ $n + m - 1$ 以上の巡回畳み込みでも問題ない。
$\mathbb{K} = \mathbb{C}$ や $\mathbb{K} = \mathbb{F} _ {p}$ の場合は離散フーリエ変換を用いた巡回畳み込みが効率的に行えるため、定数倍高速化が見込める。

## その他

-   $y \in \mathbb{K} ^ {n}$ を固定して写像 $\mathrm{mul} ^ {t} \colon \mathbb{K} ^ {n + m - 1} \to \mathbb{K} ^ {m}$ を $\mathrm{mul} ^ {t}(v) _ {k} = \sum _ {i = 0} ^ {n - 1} y _ {i} v _ {k + i}$ によって定めると $X _ {k} = w ^ {- t _ {k}} \mathrm{mul} ^ {t} (v) _ {k}$ であるから、$\mathrm{mul} ^ {t}$ の高速な計算が問題となる。
    $\mathrm{mul} ^ {t}$ は線形写像となるが、これを行列で表現し転置して得られる写像 $\mathrm{mul} \colon \mathbb{K} ^ {m} \to \mathbb{K} ^ {n + m - 1}$ は引数と $y$ の畳み込みに一致する。
    Tellegen's principle により、線形写像を計算するアルゴリズムが特定の条件を満たす時、その転置写像もまた同じ計算量で計算できることが知られている。
    従って畳み込みのアルゴリズムが特定の条件を満たすならば、$\mathrm{mul} ^ {t}$ はその転置 $\mathrm{mul}$ と同じ計算量 $\mathrm{M}(n, m)$ で計算できる。
    実際、本ページ中で示した離散フーリエ変換を用いる場合の定数倍高速化も Tellegen's principle から導出できる。

## 参考文献

1.  Rabiner, L., Schafer, R. W., & Rader, C. (1969). The chirp z-transform algorithm. IEEE transactions on audio and electroacoustics, 17(2), 86-92.
    -   chirp z-transform が提案された論文
1.  Crandall, R., & Pomerance, C. B. (2006). Prime numbers: a computational perspective (Vol. 182). Springer Science & Business Media.
    -   参考文献 1 のアルゴリズムにおいて三角数を用いて $w ^ {1 / 2}$ の計算を不要にする方法が説明されている
1.  Bostan, A., & Schost, É. (2005). Polynomial evaluation and interpolation on special sets of points. Journal of Complexity, 21(4), 420-446.
    -   参考文献 2 のアルゴリズムにおいて三角数の使い方を少しだけ変えている。
        本ページはこのアルゴリズムを説明している。
1.  Bostan, A., Lecerf, G., & Schost, É. (2003, August). Tellegen's principle into practice. In Proceedings of the 2003 international symposium on Symbolic and algebraic computation (pp. 37-44).
    -   離散フーリエ変換を用いた畳み込みを転置するアルゴリズムの導出についての記述がある
