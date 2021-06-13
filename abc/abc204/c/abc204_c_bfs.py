from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)

ans = 0
for i in range(N):
    used = [False] * N
    q = deque([])
    used[i] = True
    ans += 1
    q.append(i)
    while len(q) > 0:
        v = q.popleft()
        for vv in G[v]:
            if used[vv]: continue
            used[vv] = True
            ans += 1
            q.append(vv)

print(ans)
