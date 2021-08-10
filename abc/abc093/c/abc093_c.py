A = list(map(int, input().split()))
A.sort()
X = 2 * A[2] - A[1] - A[0]

if X % 2 == 0:
    print(X // 2)
else:
    print((X + 3) // 2)
