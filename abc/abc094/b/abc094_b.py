N, M, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
b = 0
c = 0
for i in range(M):
    if A[i] < X:
        b += 1
    else:
        c += 1

print(min(b, c))
