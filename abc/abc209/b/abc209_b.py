N, X = map(int, input().split())
A = list(map(int, input().split()))

total = 0
for i in range(N):
    if i % 2 == 1:
        A[i] -= 1
    total += A[i]

print("Yes" if total <= X else "No")
