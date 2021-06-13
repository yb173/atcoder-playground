import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())

# 都市 i から伸びる道は複数あるため要素が配列になっている
G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)

# dfs
def dfs(v: int):
    if used[v]: return # 同じ頂点を２度調べないための return
    used[v] = True
    for vv in G[v]: dfs(vv)

ans = 0

# 都市 i からスタートする場合
for i in range(N):
    used = [False] * N
    # used[j] は都市 j に到達可能かどうかを表す
    dfs(i)
    ans += sum(used) 

print(ans)
