N = int(input())
A = list(map(int, input().split()))

D = abs(A[0])
for i in range(1, N):
    D += abs(A[i] - A[i - 1])
D += abs(A[N - 1])

for i in range(N):
    prev = A[i - 1] if i != 0 else 0
    now = A[i]
    next = A[i + 1] if i != N - 1 else 0
    ans = D - abs(now - prev) - abs(next - now) + abs(next - prev)
    print(ans)
