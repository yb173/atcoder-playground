from collections import defaultdict
import math

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

b_cnt = defaultdict(lambda: 0)

for c in C:
    b_cnt[B[c - 1]] += 1

ans = 0
for i in range(N):
    ans += b_cnt[A[i]]

print(ans)
