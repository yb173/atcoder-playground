N = int(input())
P = list(map(int, input().split()))
Q = [None] * N
for i in range(N):
    Q[P[i] - 1] = i + 1

print(*Q)
