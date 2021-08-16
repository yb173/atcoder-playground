import sys
from itertools import chain
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)

def fast_prime_set(n: int):
    if n < 4:
        return ({}, {}, {2}, {2, 3})[n]
    n_sqrt = int(n ** 0.5) + 1
    primes = {2, 3} | set(chain(range(5, n + 1, 6), range(7, n + 1, 6)))
    for i in range(5, n_sqrt, 2):
        if i in primes:
            primes.difference_update(range(i * i, n, i * 2))
    return primes

def prime_factorization(x: int):
    primes = fast_prime_set(1000)

    fact = defaultdict(int)
    for prime in primes:
        while x % prime == 0:
            fact[prime] += 1
            x //= prime
        if x == 1:
            break
        if x in primes:
            fact[x] += 1
            break
    return fact

MOD = 10 ** 9 + 7

N = int(input())
d = defaultdict(lambda: 0)

for i in range(1, N + 1):
    for p, cnt in prime_factorization(i).items():
        d[p] += cnt

ans = 1
for cnt in d.values():
    ans *= (cnt + 1)
    ans %= MOD 

print(ans)
