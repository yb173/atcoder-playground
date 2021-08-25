from heapq import heappop, heappush

class Dijkstra:
    def __init__(self, n):
        self.n = n # 頂点の数
        self.G = [[] for _ in range(n)] # 隣接リスト

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

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

d = Dijkstra(N + 1)
for i in range(N):
    d.add(0, i + 1, T[i])
    
    start = i + 1
    end = i + 2 if i != N - 1 else 1
    d.add(start, end, S[i])

dist = d.distance(0)

for i in range(1, N + 1):
    print(dist[i])
