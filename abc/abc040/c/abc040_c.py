def cost(x, y):
    return abs(y - x)

n = int(input())
a = list(map(int, input().split()))

dp = [None] * n
dp[0] = 0
dp[1] = cost(a[0], a[1])

for i in range(2, n):
    dp[i] = min(dp[i - 1] + cost(a[i - 1], a[i]), dp[i - 2] + cost(a[i - 2], a[i]))

print(dp[n - 1])
