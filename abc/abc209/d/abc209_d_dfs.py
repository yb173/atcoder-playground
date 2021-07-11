import sys
sys.setrecursionlimit(10 ** 9)

def dfs(v: int, dep = 0, parent = -1):
    depth[v] = dep
    for vv in edges[v]:
        # 親に戻るルートの場合はスキップ（無限再帰を防ぐ）
        if vv == parent: continue
        dfs(vv, dep + 1, v)

N, Q = map(int, input().split())

# 無向グラフ
edges = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

# 全頂点の深さを格納する配列
depth = [0] * N

# 全頂点の深さを深さ優先探索で求める
dfs(0)

# それぞれのクエリにおいて c と d の経路の偶奇を求める
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    parity = depth[c] + depth[d]
    print("Town" if parity % 2 == 0 else "Road")
