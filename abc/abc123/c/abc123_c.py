N, *A = [int(input()) for _ in range(6)]
A.sort()
mi = A[0]
ans = (N + mi - 1) // mi + 4
print(ans)
