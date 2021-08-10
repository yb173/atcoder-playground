INF = 1 << 60

N = int(input())
dp = [INF] * (N + 1)
dp[0] = 0
for n in range(1, N + 1):
    dp[n] = dp[n - 1] + 1
    k = 6
    while k <= n:
        dp[n] = min(dp[n], dp[n - k] + 1)
        k *= 6
    k = 9
    while k <= n:
        dp[n] = min(dp[n], dp[n - k] + 1)
        k *= 9

print(dp[N])
