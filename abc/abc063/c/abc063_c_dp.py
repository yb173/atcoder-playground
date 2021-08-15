N = int(input())
S = [int(input()) for _ in range(N)]

P_MAX = 10001

dp = [[False] * (P_MAX) for i in range(N + 1)]

dp[0][0] = True
for i in range(N):
    for j in range(P_MAX):
        if dp[i][j]:
            dp[i + 1][j] = True
            dp[i + 1][j + S[i]] = True

ans = 0
for j in range(P_MAX):
    if dp[N][j] and j % 10 != 0:
        ans = max(ans, j)

print(ans)
