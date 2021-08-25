from collections import deque

def bfs(G):
    dist = [-1] * len(G)
    dist[0] = 0

    q = deque()
    q.append(0)

    while q:
        v = q.popleft()
        for vv in G[v]:
            if dist[vv] == -1:
                dist[vv] = dist[v] + 1
                q.append(vv)

    return dist

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

print("POSSIBLE" if bfs(G)[N - 1] == 2 else "IMPOSSIBLE")
