INF = 1 << 60

N, M = map(int, input().split())

# 最初は辺が１本も張られていないため，∞の辺が張られているとして INF で初期化しておく
dist = [[INF] * N for _ in range(N)]

for i in range(M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

# 同じ頂点同士の距離は 0 としておく
for i in range(N):
    dist[i][i] = 0

# ワーシャル・フロイド法
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

ans = 0
for i in range(N):
    for j in range(N):
       ans += dist[i][j] 

print(ans)
