MOD = 10**9 + 7

N = int(input())

ans = 1

for i in range(1, N + 1):
    ans *= i
    ans %= MOD

print(ans)
