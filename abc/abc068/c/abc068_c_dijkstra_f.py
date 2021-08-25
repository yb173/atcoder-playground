import heapq

def dijkstra(G):
    n = len(G)
    dist = [-1] * n
    dist[0] = 0

    used = [False] * n

    q = []
    # (距離, 頂点) 
    heapq.heappush(q, (0, 0))

    while q:
        d, v = heapq.heappop(q)

        if used[v]:
            continue

        used[v] = True
        for vv in G[v]:
            # 重みは常に 1 
            w = 1

            # vv が未訪問だったとき，あるいは vv への最短距離が更新可能だったとき，
            # vv への最短距離を更新して，ヒープの末尾に追加する
            if dist[vv] == -1 or dist[vv] > dist[v] + w:
                dist[vv] = dist[v] + w
                heapq.heappush(q, (dist[vv], vv))

    return dist

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

print("POSSIBLE" if dijkstra(G)[N - 1] == 2 else "IMPOSSIBLE")
