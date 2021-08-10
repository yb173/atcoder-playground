import sys

sys.setrecursionlimit(10 ** 9)

def dfs(v, parent):
    ans.append(v + 1)
    for vv in G[v]:
        if vv == parent:
            continue
        dfs(vv, v)
        ans.append(v + 1)

N = int(input())

G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    G[i].sort()

ans = []
dfs(0, -1)

print(*ans)
