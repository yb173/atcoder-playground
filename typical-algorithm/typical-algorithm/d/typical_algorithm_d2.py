from heapq import heappop, heappush

class Dijkstra:
    def __init__(self, n):
        self.n = n # 頂点の数
        self.G = [[] for _ in range(n)]

    def add(self, u, v, w):
        self.G[u].append((v, w))

    def distance(self, start):
        dist = [-1] * self.n
        dist[start] = 0
        used = [False] * self.n

        q = []
        heappush(q, (start, 0)) # (頂点，距離)
        while len(q) > 0:
            d, v = heappop(q)
            if used[v]:
                continue
            used[v] = True
            for (vv, w) in self.G[v]:
                if dist[vv] == -1 or dist[vv] > dist[v] + w:
                    dist[vv] = dist[v] + w
                    heappush(q, (dist[vv], vv))
        return dist
        
    def count(self, start, mod):
        dist = [-1] * self.n
        dist[start] = 0
        cnt = [0] * self.n
        cnt[start] = 1
        used = [False] * self.n

        q = []
        heappush(q, (start, 0)) # (頂点，距離)
        while len(q) > 0:
            d, v = heappop(q)
            if self.used[v]:
                continue
            used[v] = True
            for (vv, w) in G[v]:
                if dist[vv] == -1 or dist[vv] > dist[v] + w:
                    dist[vv] = dist[v] + w
                    cnt[vv] = cnt[v]
                    heappush(q, (dist[vv], vv))
                else:
                    if dist[vv] == dist[v] + w:
                        cnt[vv] += cnt[v]
                        cnt[vv] %= mod
        return cnt

N, M = map(int, input().split())

d = Dijkstra(N)

for i in range(M):
    u, v, w = map(int, input().split())
    # u -= 1
    # v -= 1
    d.add(u, v, w)

print(d.distance(0)[N - 1])
