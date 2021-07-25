N = int(input())
A = [int(input()) for _ in range(N)]

lft = [0] * N
for i in range(N):
    if i == 0:
        lft[i] = A[i]
    else:
        lft[i] = max(lft[i - 1], A[i])

rht = [0] * N
for i in reversed(range(N)):
    if i == N - 1:
        rht[i] = A[i]
    else:
        rht[i] = max(rht[i + 1], A[i])

for i in range(N):
    l = lft[i - 1] if i != 0 else 0
    r = rht[i + 1] if i != N - 1 else 0
    print(max(l, r))
