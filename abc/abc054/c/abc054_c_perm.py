from itertools import permutations

N, M = map(int, input().split())
G = [[False] * N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = True
    G[b][a] = True

ans = 0
for v in permutations(range(1, N)):
    t = (0,) + v
    ok = True
    for i in range(N - 1):
        if not G[t[i]][t[i + 1]]:
            ok = False
            break
    if ok:
       ans += 1 

print(ans)
