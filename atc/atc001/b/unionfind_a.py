class UnionFind:
    def __init__(self, num):
        self.rank = [0] * num # 木の深さ
        self.parents = [i for i in range(num)] # 親（自分自身で初期化）
        self.n = num

    def find(self, node):
        if self.parents[node] == node:
            return node
        else:
            self.parents[node] = self.find(self.parents[node]) # 経路圧縮
            return self.parents[node]
    
    def same(self, node1, node2):
        return self.find(node1) == self.find(node2)

    def union(self, node1, node2):
        x = self.find(node1)
        y = self.find(node2)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

N, Q = map(int, input().split())

uf = UnionFind(N)

for i in range(Q):
    p, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if p == 0:
        uf.union(a, b)
    else:
        print("Yes" if uf.same(a, b) else "No")
