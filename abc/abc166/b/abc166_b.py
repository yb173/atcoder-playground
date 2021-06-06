from collections import defaultdict

N, K = map(int, input().split())

# dict = defaultdict(lambda: 0)
s = set()
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for item in A:
        # dict[item] += 1
        s.add(item)
ans = 0
for i in range(N):
    index = i + 1
    if index not in s:
        ans += 1

print(ans)
