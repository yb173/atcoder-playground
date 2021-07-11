INF = 1 << 60
N = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(N):
    x = INF
    for r in range(l, N):
        x = min(x, A[r])
        ans = max(ans, x * (r - l + 1))

print(ans)
