N = int(input())
S = [input() for _ in range(N)]
G = [[''] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        G[j][N - 1 - i] = S[i][j]

for i in range(N):
    print(''.join(G[i]))
