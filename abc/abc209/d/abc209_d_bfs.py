from collections import deque

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
depth = [-1] * N

# 全頂点の深さを幅優先探索で求める
q = deque()
q.append(0)
depth[0] = 0
while q:
    v = q.popleft()
    for vv in edges[v]:
        # 深さを計算済みならスキップ
        if not depth[vv] == -1: continue
        depth[vv] = depth[v] + 1
        q.append(vv)

# それぞれのクエリにおいて c と d の経路の偶奇を求める
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    parity = depth[c] + depth[d]
    print("Town" if parity % 2 == 0 else "Road")
