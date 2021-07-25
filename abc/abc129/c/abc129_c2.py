# もらうDPその２
MOD = 10 ** 9 + 7
N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
ng = [False] * (N + 1)
for v in a:
    ng[v] = True

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    if ng[i]: continue
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= MOD

print(dp[N])
