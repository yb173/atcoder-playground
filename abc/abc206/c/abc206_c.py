from collections import defaultdict

def wa(N):
    ans = 0
    for i in range(1, N):
        ans += i
    return ans

N = int(input())
A = list(map(int, input().split()))

a = 0
for i in range(1, N):
    a += i

d = defaultdict(lambda: 0)
for i in range(N):
    d[A[i]] += 1

tmp = 0
for v in d.values():
    if v > 1:
        tmp += wa(v)

print(a - tmp)
