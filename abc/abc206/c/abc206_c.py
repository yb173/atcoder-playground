from collections import defaultdict

def f(x: int) -> int:
    return x * (x - 1) // 2

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(lambda: 0)
for i in range(N):
    d[A[i]] += 1

ans = f(N)
for v in d:
    if d[v] > 1:
        ans -= f(d[v])

print(ans)
