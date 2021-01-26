---
layout: entry
author: kimiyuki
reviewers:
date: 2020-07-09T00:00:00+09:00
tags: algorithm fast-kitamasa-method kitamasa-method
algorithm:
  input: $k + 1$ 項間の線型漸化式で定まる数列 $a$ の漸化式および初めの $k$ 項 $(a_0, a_1, \dots, a _ {k-1})$ および自然数 $N$
  output: 数列 $a$ の第 $N$ 項 $a_N$
  time_complexity: $O(k \log k \log N)$
  space_complexity:
  aliases:
  level: red
description: 高速 Kitamasa 法とは、$k + 1$ 項間の線型漸化式で定まる数列の第 $N$ 項を $O(k \log k \log N)$ で求めるアルゴリズムである。Kitamasa 法とは異なる。
---

# 高速Kitamasa法

## 対象となる問題

対象となる問題は次のようなものである:

可換環 $R$ の要素の無限列 $a = (a_0, a_1, a_2, \dots) \in R^{\omega}$ が、その先頭 $k$ 項 $a_0, a_1, \dots, a _ {k-1}$ と漸化式 $a _ {n + k} = \sum _ {i \lt k} c_i a _ {n + i} = c_0 a_n + c_1 a _ {n + 1} + \dots + c _ {k-1} a _ {n + k -1}$ で定義されているとする。
このとき先頭 $k$ 項 $a_0, a_1, \dots, a _ {k-1} \in R$ と漸化式の情報 $c_0, c_1, \dots, c _ {k-1} \in R$ と自然数 $N$ が与えられるので、第 $N$ 項の値 $a_n$ を求めよ。

解き方はいくつかあるので、説明のために、簡単な方から順番に見ていく。

## 愚直: $O(kN)$

それはそう

## 行列累乗: $O(k^3 \log N)$

漸化式を行列で書くと次のようになる。これを行列累乗すればよい。

$$ \begin{pmatrix}
    a _ {n + k} \cr
    a _ {n + k - 1} \cr
    \vdots \cr
    a _ {n + 2} \cr
    a _ {n + 1}
\end{pmatrix} = \begin{pmatrix}
    c _ {k-1} & c _ {k-2} & \dots & c _ 1 & c _ 0 \cr
    1 & 0 & \dots & 0 & 0 \cr
    0 & 1 & \dots & 0 & 0 \cr
    \vdots & \vdots & \ddots & \vdots & \vdots \cr
    0 & 0 & \dots & 1 & 0
\end{pmatrix} \begin{pmatrix}
    a _ {n + k - 1} \cr
    a _ {n + k - 2} \cr
    \vdots \cr
    a _ {n + 1} \cr
    a _ {n}
\end{pmatrix} $$

## Kitamasa 法: $O(k^2 \log N)$

Kitamasa 法とは、$k$ 階の線型漸化式で定まる数列の $N$ 項目を $O(k^2 \log N)$ で求めるアルゴリズムである。
行列累乗の方針と同様に繰り返し二乗法だが、行列を陽には求めない。また、多項式の高速な乗算は必ずしも必要ない。

### 繰り返し二乗法

入力として第 $n, n+1, \dots, n+k-1$ 項から第 $n+k$ 項を求める漸化式 $$a _ {n + k} = \sum _ {i \lt k} c_i a _ {n + i}$$ が与えられている。これを一般化して 第 $n, n+1, \dots, n+k-1$ 項から第 $n + m$ 項を直接に求める漸化式 $$a _ {n + m} = \sum _ {i \lt k} b _ {m,i} a _ {n+i}$$ を求めていく。
特にこれを、以下のふたつを繰り返すことで行う。

-   漸化式 $a _ {n + m} = \sum _ {i \lt k} b _ {m,i} a _ {n+i}$ を使って、漸化式 $a _ {n + m + 1} = \sum _ {i \lt k} b _ {m + 1,i} a _ {n+i}$ を求める
-   漸化式 $a _ {n + m} = \sum _ {i \lt k} b _ {m,i} a _ {n+i}$ を使って、漸化式 $a _ {n + 2m} = \sum _ {i \lt k} b _ {2m,i} a _ {n+i}$ を求める

前者は明らかに $O(k)$ で求まる。

### 次数の半減

後者を求めたい。
簡単のため $n = 0$ のように書く。
漸化式を
$$ \begin{array}{rcl}
    a _ {2m} & = & \sum _ {i \lt k} b _ {2m,i} a _ i \cr
             & = & \sum _ {i \lt k} b _ {m,i} a _ {m+i} \cr
             & = & \sum _ {i \lt k} b _ {m,i} \sum _ {j \lt k} b _ {m+i,j} a _ j
\end{array} $$
と変形すると、$k$ 個の数列 $b _ {m,\ast}, b _ {m+1,\ast}, \dots, b _ {m+k-1, \ast}$ をすでに考えた方法でそれぞれ $O(k)$ かけて求めれば、そらを使って数列 $b _ {2m,\ast}$ をさらに $O(k^2)$ 使って求めることで、全体で $O(k^2)$ で求められることが分かる。

$O(k)$ のステップと $O(k^2)$ のステップを高々 $O(\log N)$ 回行なえば目標の値 $a_N = \sum _ {i \lt k} b _ {N,i} a _ i$ が求まるので、全体では $O(k^2 \log N)$ となる。


## 高速 Kitamasa 法: $O(k \log k \log N)$

高速 Kitamasa 法とは、$k$ 階の線型漸化式で定まる数列の $N$ 項目を $O(k \log k \log N)$ で求めるアルゴリズムである。
Kiatamasa 法では、漸化式 $a _ {2m} = \sum _ {i \lt k} b _ {2m,i} a_i$ を $O(k^2)$ で求めていた。これを多項式乗算と多項式剰余算を用いて高速化し $O(k \log k)$ で行う。

### 多項式乗算

まず $a _ {2m} = \sum _ {i \lt k} b _ {2m,i} a_i$ の漸化式をさらに変形し、多項式の乗算を利用する。
$$ \begin{array}{rcl}
    a _ {2m} & = & \sum _ {i \lt k} b _ {2m,i} a _ i \cr
             & = & \vdots \cr
             & = & \sum _ {i \lt k} b _ {m,i} \sum _ {j \lt k} b _ {m,j} a _ {i+j} \cr
             & = & \sum _ {s \lt 2k-1} a_s \sum _ {i + j = s} b _ {m,i} b _ {m,j}
\end{array} $$ と変形する。
ここで多項式 $g_m = \sum _ {i \lt k} b _ {m,i} x^i$ を考える。
$g_m^2 = \sum _ {s \lt 2k-1} \left( \sum _ {i + j = s} b _ {m,i} b _ {m,j} \right) x^s$ であり、多項式の乗算は高速 Fourier 変換や数論変換によって $O(k \log k)$ で得られるので、この結果を利用することで長さ $2k-1$ の漸化式
$$a _ {2m} = \sum _ {s \lt 2k-1} b' _ {2m,s} a_s$$
が得られる。

### 多項式剰余算

これにより、漸化式 $a _ {2m} = \sum _ {s \lt 2k-1} b' _ {2m,s} a_s$ から $a _ {2m} = \sum _ {i \lt k} b _ {2m,i} a_i$ を得る問題に帰着された。
元々与えられている漸化式を逆向きに適用して次数下げしていくことで $O(k^2)$ で計算が可能だが、より改善したい。
さてこの問題を多項式の言葉で書き直すと、多項式 $f = \sum _ {s \lt 2k-1} b' _ {2m,s} x^s$ を等式 $x^k - \sum _ {i \lt k} a_i x^i = 0$ を使って次数を下げる、ということである。これは多項式 $g = x^k - \sum _ {i \lt k} a_i x^i$ で多項式 $f$ を割った余りを求めることに他ならない。
つまり、高々 $2k-1$ 次の多項式 $f$ を $k+1$ 次の多項式 $g$ で割った余りを $O(k \log k)$ で求めることができればよく、これは可能である。この高速な多項式の剰余については、多項式の乗算と同様に、説明を省略する。
