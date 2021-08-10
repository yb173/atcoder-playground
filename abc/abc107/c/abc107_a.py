N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 1 << 60
for i in range(N - K + 1):
    # 左端に行って右端まで行く場合
    left = abs(X[i]) + X[i + K - 1] - X[i]
    # 右端に行って左端まで行く場合
    right = abs(X[i + K - 1]) + X[i + K - 1] - X[i]
    ans = min(ans, left, right)

print(ans)
