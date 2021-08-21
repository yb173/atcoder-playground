from itertools import combinations

A = list(map(int, input().split()))

ans = []
for v in combinations(A, 3):
    ans.append(sum(v))

ans.sort()
print(ans[-3])
