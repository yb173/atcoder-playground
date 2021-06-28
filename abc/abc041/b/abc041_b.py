MOD = 10**9 + 7

A, B, C = map(int, input().split())
ans = A % MOD
ans *= B
ans %= MOD
ans *= C
ans %= MOD
print(ans)
