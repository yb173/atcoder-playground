from heapq import heappop, heappush

class Dijkstra:
    def __init__(self, G: list, start: int, mod: int = 10 ** 9 + 7) -> None:
        self.n = len(G) # 頂点の数
        self.G =  G # 隣接リスト
        self.start = start # スタート地点
        self.mod = mod

        # start から各頂点への最短距離（コスト）
        self.cost = [0 if i == self.start else -1 for i in range(self.n)]
        # start から各頂点への最短距離の個数
        self.count = [1 if i == self.start else 0 for i in range(self.n)]

        self.visited = [False] * self.n
        self.prev = [-1] * self.n
        
        # ダイクストラ法を実行
        self.__dijkstra()

    def __dijkstra(self) -> list:
        q = []
        heappush(q, (self.start, 0)) # (頂点，距離)
        while len(q) > 0:
            d, v = heappop(q)
            if self.visited[v]:
                continue
            self.visited[v] = True
            for (vv, w) in self.G[v]:
                if self.cost[vv] == -1 or self.cost[vv] > self.cost[v] + w:
                    self.cost[vv] = self.cost[v] + w
                    heappush(q, (self.cost[vv], vv))
                    self.count[vv] = self.count[v]
                    self.prev[vv] = v
                else:
                     if self.cost[vv] == self.cost[v] + w:
                         self.count[vv] += self.count[v]
                         self.count[vv] %= self.mod

    def get_costs(self) -> list:
        return self.cost

    def get_counts(self) -> list:
        return self.count

    def get_path(self, t: int) -> list:
        path = []
        while t != -1:
            path.append(t) # t が始点になるまで prev[t] を辿っていく
            t = self.prev[t]
        path.reverse()
        return path

# N, M = map(int, input().split())
# G = [[] for i in range(N)]
# for i in range(M):
#     u, v, w = map(int, input().split())
#     G[u].append((v, w))
