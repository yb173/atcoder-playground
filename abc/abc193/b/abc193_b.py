from collections import defaultdict
import math

INF = 1 << 60

N = int(input())
A, P, X = [], [], []
for i in range(N):
    a, p, x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)

ans = INF
for i in range(N):
    if X[i] - A[i] > 0:
        ans = min(ans, P[i])

if ans == INF:
    print(-1)
else:
    print(ans)
