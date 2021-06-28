N, M = map(int, input().split())

G = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a] += 1
    G[b] += 1

for i in range(N):
    print(G[i])
