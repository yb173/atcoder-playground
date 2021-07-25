N, M = map(int, input().split())
H = list(map(int, input().split()))

to_undirected = [set() for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to_undirected[a].add(b)
    to_undirected[b].add(a)

ans = 0
for i in range(N):
    ok = True
    for j in to_undirected[i]:
        if H[j] >= H[i]:
            ok = False
            break
    if ok:
       ans += 1

print(ans)
