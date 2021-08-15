class UnionFind:
    def __init__(self, n: int) -> None:
        assert 0 <= n
        
        self.n = n # ノード数
        self.parent_or_size = [-1] * n # 親，自分自身が親であればその要素数 * (-1)

    def find(self, x):
        assert 0 <= x < self.n

        if self.parent_or_size[x] < 0:
            return x
        else:
            self.parent_or_size[x] = self.find(self.parent_or_size[x]) # 経路圧縮
            return self.parent_or_size[x]
    
    def same(self, x: int, y: int) -> bool:
        assert 0 <= x < self.n
        assert 0 <= y < self.n

        return self.find(y) == self.find(y)

    def union(self, x: int, y: int) -> int:
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        
        return x

    def size(self, x):
        assert 0 <= x < self.n

        return -self.parent_or_size[self.find(x)]

N, M = map(int, input().split())

A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1

ans = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if j == i: continue
        uf.union(A[j], B[j])
    if uf.size(0) != N:
        ans += 1

print(ans)
