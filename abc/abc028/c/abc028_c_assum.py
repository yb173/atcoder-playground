from itertools import combinations

A = list(map(int, input().split()))
A.sort()

print(max(A[0] + A[3] + A[4], A[1] + A[2] + A[4]))
