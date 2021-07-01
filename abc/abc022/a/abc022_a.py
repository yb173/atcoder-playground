N, S, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

weight = 0
ans = 0
for i in range(N):
    weight += A[i]
    if S <= weight <= T:
        ans += 1

print(ans)
