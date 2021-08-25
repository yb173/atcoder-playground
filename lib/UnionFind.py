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

    def unite(self, x: int, y: int) -> int:
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
