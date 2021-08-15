from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

ans = 0
for key in C:
    if key <= C[key]:
        ans += C[key] - key
    else:
        ans += C[key]

print(ans)
