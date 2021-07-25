# もらうDP
MOD = 10**9 + 7
S = input()
N = len(S)
T = 'chokudai'
M = len(T)
dp = [[0] * (M + 1) for _ in range(N + 1)]

# 初期化
for i in range(N + 1):
    dp[i][0] = 1

for i in range(N):
    for j in range(M):
        if not S[i] == T[j]:
            dp[i + 1][j + 1] = dp[i][j + 1]
        else:
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD

print(dp[N][M])
