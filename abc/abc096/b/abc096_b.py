A = list(map(int, input().split()))
A.sort()
K = int(input())
print(A[0] + A[1] + A[2] * 2 ** K)
