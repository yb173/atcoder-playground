N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for i in range(N):
    if K <= h[i]:
        ans += 1

print(ans)
