from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = [a % 200 for a in A]

C = Counter(B)

ans = 0
for c in C:
    ans += C[c] * (C[c] - 1) // 2

print(ans)
