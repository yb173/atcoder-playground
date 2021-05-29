from collections import defaultdict
import math

INF = 1 << 60
MOD = 10**9 + 7

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += A[i] * B[i]

if sum == 0:
    print("Yes")
else:
    print("No")
