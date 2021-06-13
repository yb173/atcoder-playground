def is_integer_dist(x, y):
    inner = 0
    for i in range(len(x)):
        inner += (y[i] - x[i])**2
    return (inner ** 0.5).is_integer()

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if is_integer_dist(X[i], X[j]):
            cnt += 1

print(cnt)
