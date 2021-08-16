def dfs(v, visited):
    visited = visited[:]
    global ans

    if visited[v]:
        return
    visited[v] = True

    if sum(visited) == N:
        ans += 1
        return

    for vv in G[v]:
        dfs(vv, visited)

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = 0
visited = [False] * N
dfs(0, visited)

print(ans)
