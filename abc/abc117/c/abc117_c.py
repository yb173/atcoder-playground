N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

edge = []
for i in range(1, M):
    edge.append(X[i] - X[i - 1])
edge.sort()

ans = 0
for i in range(max(0, M - N)):
    ans += edge[i]

print(ans)
