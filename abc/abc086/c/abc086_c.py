def mdist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

N = int(input())
T = [None] * N
X = [None] * N
Y = [None] * N
for i in range(N):
    T[i], X[i], Y[i] = map(int, input().split())

for i in range(N):
    dt = T[i] - T[i - 1] if i != 0 else T[i]
    dd = mdist(X[i], Y[i], X[i - 1], Y[i - 1]) if i != 0 else mdist(X[i], Y[i], 0, 0)
    if dt % dd != 0:
        print("No")
        exit()

print("Yes")
