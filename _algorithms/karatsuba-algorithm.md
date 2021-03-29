---
layout: entry
changelog:
  - summary: 見出し作成
    authors: kimiyuki
    reviewers:
    date: 2020-07-09T00:00:00+09:00
  - summary: 本文作成
    authors: ngtkana
    reviewers:
    date: 2021-03-30T00:00:00+09:00
algorithm:
  input:
     次数 $N - 1$ の多項式 $f, g$ の係数列
  output:
    積 $f g$ の係数列
  time_complexity: $O ( N ^ { 1.59 } )$ 回の環演算
  space_complexity:
  aliases:
  level: yellow
description: Karatsuba 法とは、多項式乗算などを $O ( N ^ { 1.59 } )$ 回の環演算で行なうアルゴリズムである。
draft: false
---


# Karatsuba法

## 概要

環 $R$ 上の次数 $N - 1$ の多項式 $f, g$ の積 $f g$ を計算する。これを小学校の方法（筆算と同じ方法、Long multiplication, grade-school multiplication などと呼ばれる。）で計算すると、$\Theta ( N ^ 2 )$ 回の環演算を要する。また、計算量は同じであるが、次のように分割統治法で計算することができる。

```
Multiplication( f, g )
 1. // 入力: f, g は多項式
 2. // 出力: 積 fg
 3. n = max(deg(f), deg(g)) + 1
 4. if n == 1
 5.     return f[0] * g[0]
 6. m = floor(n)
 7. f(x) = f₁(x) x^m + f(0),  g(x) = g₁(x) x^m + g₀(x) と分解する。
 8. h₀  = Multiplication( f₀ , g₀  )
 9. h₂ = Multiplication( f₁, g₁ )
10. h₁ = Multiplication( f₀ +  g₁ ) + Multiplication( f₁, g₀ )
11. return h₂ x^{2*m} + h₁ x^m + h₀
```

Karatsuba 法では、恒等式
$$
f _ 0 g _ 1 + f _ 1 g _ 0 = ( f _ 0 + f _ 1 ) ( g _ 0 + g _ 1 ) - f _ 0 f _ 1 - g _ 0 g _ 1
$$
を利用する。すると次のような疑似コードを得る。再帰呼出しの回数が $4$ 回から $3$ 回に減り、計算量が $\Theta ( N ^ { \lg 3 } ) = O ( N ^ { 1.59 } )$ に改善する。


```
Karatsuba( f, g )
 1. // 入力: f, g は多項式
 2. // 出力: 積 fg
 3. n = max(deg(f), deg(g)) + 1
 4. if n == 1
 5.     return f[0] * g[0]
 6. m = floor(n)
 7. f(x) = f₁(x) x^m + f(0),  g(x) = g₁(x) x^m + g₀(x) と分解する。
 8. h₀  = Karatsuba( f₀ , g₀ )
 9. h₂ = Karatsuba( f₁, g₁)
10. h₁ = Karatsuba( f₀ + f₁, g₀ + g₁ ) - h₀ - h₂
11. return h₂ x^{2*m} + h₁ x^m + h₀
```


## 定数倍について

小学校の方法は $2 N ^ 2$ 回以下、Karatsuba 法は $9 N ^ { \lg 3 }$ 回以下の環演算を行う。


## 環の条件の緩和

実は $R$ は環である必要はない。とくに加法逆元が存在する必要がなく、例えば $(+, \times)$ の代わりに $(\min, +), (\max, +), (\mathrm { gcd }, \times ), (\mathrm { lcm }, \times )$ などに適用することができる。


## 多倍長整数の乗算への応用

多倍長整数の乗算も、桁数半分で分けて同様の方法で計算することで、高速に計算することができる。


## 参考文献

* 山本慎 ・三好重明 ・原正雄 ・谷聖一 ・衛藤和文 訳*コンピュータ代数ハンドブック*. 朝倉書店, 2006.
