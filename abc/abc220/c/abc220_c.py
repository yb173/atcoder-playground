N = int(input())
A = list(map(int, input().split()))
X = int(input())

R = sum(A)
ans = X // R * N
X -= X // R * R

for i in range(N):
    ans += 1
    X -= A[i]
    if X < 0:
        break

if X == 0:
    ans += 1

print(ans)
