def compress(X):
    Y = sorted(list(set(X)))
    d = {}
    for i in range(len(Y)):
        d[Y[i]] = i
    return [d[X[i]] for i in range(len(X))]

n = int(input())
a = [int(input()) for _ in range(n)]

ans = compress(a)

for v in ans:
    print(v)
