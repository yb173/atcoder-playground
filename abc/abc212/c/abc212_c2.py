
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G = []
for i in range(N):
    G.append((A[i], 0))
for i in range(M):
    G.append((B[i], 1))

G.sort(key=lambda x: x[0])

ans = 1 << 60
for i in range(len(G)):
    if i == 0:
        now = G[i][0]
        ab = G[i][1]
        continue
    if not G[i][1] == ab:
        diff = abs(G[i][0] - now)
        ans = min(diff, ans)
    now = G[i][0]
    ab = G[i][1]
    
print(ans)
