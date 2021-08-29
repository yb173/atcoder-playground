INF = 1 << 60

N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [INF] * N
dp[0] = 0

for i in range(N):
    for j in range(i + 1, i + K + 1):
        if j == N:
            break
        dp[j] = min(dp[j], dp[i] + abs(h[j] - h[i]))

print(dp[N - 1])
