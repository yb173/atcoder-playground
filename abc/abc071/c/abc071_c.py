from collections import Counter

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

c = Counter(A)

c4 = [k for k in c if c[k] >= 4]
c2 = [k for k in c if c[k] >= 2]

ans = 0

if len(c4) > 0:
    ans = max(ans, c4[0] ** 2)

if len(c2) > 1:
    ans = max(ans, c2[0] * c2[1])

print(ans)
