from collections import deque

MOD = 10 ** 9 + 7

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# 都市１(i = 0) から都市 i までの最短経路
dist = [None] * N
# 都市１から都市１までの最短経路は
dist[0] = 0
# 都市１(i = 0) から都市 i までの最短経路の数
cnt = [0] * N
# 都市１から都市１までの最短経路は距離ゼロの１通り
cnt[0] = 1

q = deque([0])
# q.append(0)

# BFS
while q:
    v = q.popleft()
    for vv in G[v]:
        if dist[vv] is None:
            dist[vv] = dist[v] + 1
            q.append(vv)
            cnt[vv] = cnt[v]
        elif dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
            cnt[vv] %= MOD

print(cnt[N - 1])
