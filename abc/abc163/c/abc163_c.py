N = int(input())
A = list(map(int, input().split()))
A = [0] + A

G = [0] * N
for i in range(1, N):
    G[A[i] - 1] += 1

for g in G:
    print(g)
