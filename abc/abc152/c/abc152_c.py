N = int(input())
P = list(map(int, input().split()))
INF = 1 << 60

mi = [INF]
for i in range(1, N + 1):
    mi.append(min(mi[i - 1], P[i - 1]))

ans = 0
for i in range(N):
    if P[i] <= mi[i + 1]:
       ans += 1 

print(ans)
