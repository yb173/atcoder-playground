from collections import defaultdict

class UnionFind:
    def __init__(self, n: int) -> None:
        assert 0 <= n
        
        self.n = n # ノード数
        self.parent_or_size = [-1] * n # 親，自分自身が親であればその要素数 * (-1)

    def find(self, x: int) -> int:
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

    def size(self, x: int) -> int:
        assert 0 <= x < self.n

        return -self.parent_or_size[self.find(x)]

N, K, L = map(int, input().split())

PQ = [None] * K
for i in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    PQ[i] = (p, q)

RS = [None] * L
for i in range(L):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    RS[i] = (r, s)

uf1 = UnionFind(N)
for p, q in PQ:
    uf1.union(p, q)
    
uf2 = UnionFind(N)
for r, s in RS:
    uf2.union(r, s)

d = defaultdict(lambda: 0)
for i in range(N):
    d[(uf1.find(i), uf2.find(i))] += 1

ans = []
for i in range(N):
    ans.append(d[(uf1.find(i), uf2.find(i))])

print(*ans)
