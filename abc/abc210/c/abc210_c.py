import sys

from math import pi, factorial, sin, cos, tan, ceil, floor, sqrt, gcd
from statistics import mode
from collections import defaultdict, Counter, deque
from itertools import product, permutations

sys.setrecursionlimit(10 ** 9)

INF = 1 << 60
MOD = 10 ** 9 + 7



N, K = map(int, input().split())
c = list(map(int, input().split()))

bubunwa = []
for i in range(K):
    bubunwa.append(c[i])

ans = 0
for i in range(N - K + 1):
    if not i == 0:
        bubunwa.pop(0)
        bubunwa.append(c[i + K - 1])
    ans = max(ans, len(set(bubunwa)))

print(ans)
