from math import factorial

MOD = 10 ** 9 + 7

w, h = map(int, input().split())
w -= 1
h -= 1

ans = factorial(w + h) // (factorial(w) * factorial(h))
ans %= MOD

print(ans)
