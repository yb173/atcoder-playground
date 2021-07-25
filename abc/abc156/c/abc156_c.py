INF = 1 << 60

N = int(input())
X = list(map(int, input().split()))
X.sort()

ans = INF
for i in range(X[0], X[-1] + 1):
    now = 0
    for j in range(N):
        now += (X[j] - i) ** 2
    ans = min(ans, now)

print(ans)

