INF = 1 << 60

N, T = map(int, input().split())
t = list(map(int, input().split()))
t.append(INF)

ans = 0
for i in range(N):
    diff = min(t[i + 1] - t[i], T)
    ans += diff

print(ans)

