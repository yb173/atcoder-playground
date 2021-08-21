n, a = map(int, input().split())
x = list(map(int, input().split()))
xmax = 50

dp = [[0] * (2 * n * xmax + 1) for i in range(n + 1)]
dp[0][n * xmax] = 1

for i in range(1, n + 1):
    for j in range(1, 2 * xmax * n + 1):
        y = x[i - 1] - a
        if j - y < 0 or 2 * n * xmax < j - y:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - y]

print(dp[n][n * xmax] - 1)
