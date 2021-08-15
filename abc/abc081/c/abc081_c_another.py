from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
c = Counter(A)

arr = c.most_common()[K:]

ans = 0
for v in arr:
    ans += v[1]

print(ans)
