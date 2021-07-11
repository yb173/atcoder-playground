from collections import Counter

def f(x):
    return x * (x - 1) // 2

N = int(input())
A = list(map(int, input().split()))

d = Counter(A)

ans = f(N)
for v in d:
    ans -= f(d[v])

print(ans)
