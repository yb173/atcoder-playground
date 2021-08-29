INF = 1 << 60

N, L = map(int, input().split())
x = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

# ハードルが存在する座標において True となる配列
H = [False] * (L + 1)
for i in range(N):
    H[x[i]] = True

# dp[i]: 座標 i で行動を終了するまでの最小所要時間
dp = [INF] * (L + 1)

# 初期条件
dp[0] = 0

for i in range(1, L + 1):
    # 行動１
    dp[i] = min(dp[i], dp[i - 1] + T1)
    
    # 行動２
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + T1 + T2)
    
    # 行動３
    if i >= 4:
        dp[i] = min(dp[i], dp[i - 4] + T1 + 3 * T2)
    
    # ハードルがあれば加算
    if H[i]:
        dp[i] += T3

# 答えは座標 L にぴったり止まるか，座標(L - 3) 〜 (L - 1) からジャンプ中にゴールしたもの
ans = dp[L]
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        ans = min(ans, dp[i] + T1 // 2 + T2 * (2 * (L - i) - 1) // 2)

print(ans)
