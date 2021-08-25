INF = 1 << 60

N, M = map(int, input().split())

# 最初は辺が１本も張られていないため，∞の辺が張られているとして INF で初期化しておく
dist = [[INF] * N for _ in range(N)]

for i in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    dist[u][v] = c

# 同じ頂点同士の距離は 0 としておく
for i in range(N):
    dist[i][i] = 0

# ワーシャル・フロイド法
ans = 0
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])
    # k 時点の和を足していく
    for i in range(N):
        for j in range(N):
            if dist[i][j] != INF:
                ans += dist[i][j] 

print(ans)
