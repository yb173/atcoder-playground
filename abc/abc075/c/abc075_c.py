def dfs(v: int):
    if used[v]: return
    used[v] = True
    for i in range(N):
        if G[v][i]:
            dfs(i)

N, M = map(int, input().split())
G = [[False] * N for i in range(N)]
A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
    G[A[i]][B[i]] = True
    G[B[i]][A[i]] = True
    
ans = 0
for i in range(M):
    G[A[i]][B[i]] = False
    G[B[i]][A[i]] = False
    used = [False] * N

    dfs(0)

    if not sum(used) == N:
        ans += 1

    G[A[i]][B[i]] = True
    G[B[i]][A[i]] = True

print(ans)
