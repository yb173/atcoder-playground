from itertools import permutations
from math import factorial

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

N = int(input())
x, y = [], []
for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

total = 0
for li in permutations(range(N)):
    for i in range(N):
        if i == N - 1: continue
        total += dist(x[li[i]], y[li[i]], x[li[i + 1]], y[li[i + 1]])
ans = total / factorial(N)

print(ans)
