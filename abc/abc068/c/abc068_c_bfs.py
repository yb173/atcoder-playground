from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# 頂点 0 から各頂点への最短距離を保持する配列
# -1 は未到達であることを表す
dist = [-1] * N

# 0 から 0 への距離は 0
dist[0] = 0

q = deque()
q.append(0)

while q:
    v = q.popleft()
    for vv in G[v]:
        # vv が未訪問だったとき， vv への距離を更新して，キューの末尾に追加する
        if dist[vv] == -1:
            dist[vv] = dist[v] + 1
            q.append(vv)

print("POSSIBLE" if dist[N - 1] == 2 else "IMPOSSIBLE")
