from collections import deque

class DAG:
    def __init__(self, n: int) -> None:

        assert 0 <= n

        self.n = n # 頂点数
        self.G = [[] for _ in  range(n)] # 有向グラフの隣接リスト
        self.in_degree = [0] * n # 各頂点の入次数

    def add(self, s: int, t: int) -> None:
        """ 有向辺の追加

        有向辺 s → t を追加する.

        Args:
            s: source となる頂点
            t: target となる頂点
        Returns:
            None
        """

        assert 0 <= s < self.n
        assert 0 <= t < self.n

        self.G[s].append(t)
        self.in_degree[t] += 1

    def sort(self) -> list or None:
        """ トポロジカルソート

        Return:
            list of int: トポロジカルソート
        """

        q = deque()
        for i in range(self.n):
            if self.in_degree[i] == 0:
                q.append(i)

        s = []
        while len(q) > 0:
            v = q.popleft()
            s.append(v)

            for vv in self.G[v]:
                self.in_degree[vv] -= 1
                if self.in_degree[vv] == 0:
                    q.append(vv)
        return s

    def is_DAG(self) -> bool:
        """ DAG かどうかの判定

        Return:
            bool: グラフが DAG なら True, そうでないなら False
        """
        return len(self.sort()) == self.n

N, M = map(int, input().split())

dag = DAG(N)

for i in range(M):
    k = int(input())
    A = list(map(int, input().split()))
    for i in range(k - 1):
        dag.add(A[i] - 1, A[i + 1] - 1)

print("Yes" if dag.is_DAG() else "No")
