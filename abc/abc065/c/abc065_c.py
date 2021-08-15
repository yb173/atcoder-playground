from math import factorial

MOD = 10 ** 9 + 7

N, M = map(int, input().split())

if abs(N - M) > 1:
    print(0)
    exit()

ans = factorial(N) % MOD
ans *= factorial(M) % MOD
ans %= MOD

if abs(N - M) == 0:
    ans *= 2
    ans %= MOD

print(ans)
