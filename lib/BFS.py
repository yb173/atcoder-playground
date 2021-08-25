from collections import deque
def bfs(G):
    """ 幅優先探索（コスト）
    """
    n = len(G)
    cost = [0 if i == 0 else -1 for i in range(n)]

    q = deque()
    q.append(0)

    while q:
        v = q.popleft()
        for vv in G[v]:
            if cost[vv] == -1:
                cost[vv] = cost[v] + 1
                q.append(vv)
    return cost
# N, M = map(int, input().split())
# G = [[] for i in range(N)]
# for i in range(M):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     G[a].append(b)
#     G[b].append(a)

from collections import deque
MOD = 10 ** 9 + 7
def bfs_count(G):
    """ 幅優先探索（最短経路の数）
    """
    n = len(G)
    cost = [0 if i == 0 else -1 for i in range(n)]
    count = [1 if i == 0 else 0 for i in range(n)]

    q = deque()
    q.append(0)

    while q:
        v = q.popleft()
        for vv in G[v]:
            if cost[vv] == -1:
                cost[vv] = cost[v] + 1
                q.append(vv)
                count[vv] = count[v]
            else:
                if cost[vv] == cost[v] + 1:
                    count[vv] += count[v]
                    count[vv] %= MOD
    return count
# N, M = map(int, input().split())
# G = [[] for i in range(N)]
# for i in range(M):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     G[a].append(b)
#     G[b].append(a)