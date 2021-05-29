N = int(input())

X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

sum = 0
for i in range(0, N):
    for j in range(i + 1, N):
        s = (Y[j] - Y[i]) / (X[j] - X[i])
        if (-1 <= s and s <= 1):
           sum += 1

print(sum)
