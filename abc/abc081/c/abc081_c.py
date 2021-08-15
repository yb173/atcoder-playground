from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
sorted_C = sorted(C.items(), key=lambda x: x[1])
L = len(sorted_C)

if K >= L:
    print(0)
else:
    diff = L - K
    ans = 0
    for i in range(diff):
        ans += sorted_C[i][1]
    print(ans)
