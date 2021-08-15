from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)

ans = 0
for x in range(10 ** 5):
    now = c[x - 1] + c[x] + c[x + 1]
    ans = max(ans, now)

print(ans)
