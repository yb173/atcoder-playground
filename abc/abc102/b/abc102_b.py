N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A[N - 1] - A[0])
