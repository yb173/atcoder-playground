N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

all = sum(A)

count = 0
for i in range(N):
    if A[i] < all / (4 * M):
        continue
    count += 1

print("Yes" if count >= M else "No")
