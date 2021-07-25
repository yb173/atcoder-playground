# くばるDP
MOD = 10**9 + 7
S = input()
N = len(S)
T = 'chokudai'
M = len(T)
dp = [[0] * (M + 1) for _ in range(N + 1)]

# 初期化
dp[0][0] = 1

for i in range(N):
    for j in range(M + 1):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        if j < M and S[i] == T[j]:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

print(dp[N][M])
