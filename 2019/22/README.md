# How to derive the formula

We have:

  $n_{k+1} \equiv A\,n_k + B \pmod M,\qquad n_0\ \text{given}.$

Unrolling the recurrence:

$\begin{aligned}
n_1 &\equiv A n_0 + B \\
n_2 &\equiv A(A n_0 + B) + B = A^2 n_0 + B(A+1) \\
n_3 &\equiv A^3 n_0 + B(A^2 + A + 1) \\
&\vdots \\
n_k &\equiv A^k n_0 + B\sum_{i=0}^{k-1} A^i \pmod M
\end{aligned}$

So in general:

$\boxed{\,n_k \equiv A^k n_0 + B\,(1 + A + \dots + A^{k-1}) \pmod M\,}$

The geometric sum is

$1 + A + \dots + A^{k-1} = \frac{A^k - 1}{A-1}$

…but **“division” modulo $M$** means multiplying by the modular inverse of $A-1$.

So if $\gcd(A-1, M)=1$ then $(A-1)^{-1} \bmod M$ exists and:

$\boxed{\,n_k \equiv A^k n_0 + B\,(A^k-1)\,(A-1)^{-1} \pmod M\,}$

```python
def k_times(k, n0, A, B, M):
    ak = pow(A, k, M)
    bk = (B * (ak - 1) * pow(A - 1, -1, M)) % M
    return (ak * n0 + bk) % M
```
