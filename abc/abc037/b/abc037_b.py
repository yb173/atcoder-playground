N, Q = map(int, input().split())
G = [0] * N
for i in range(Q):
    L, R, T = map(int, input().split())
    L -= 1
    R -= 1
    for j in range(L, R + 1):
        G[j] = T

for i in range(N):
    print(G[i])
