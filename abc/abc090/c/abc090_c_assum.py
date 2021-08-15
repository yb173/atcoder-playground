N, M = map(int, input().split())

# M が大きくなるようにする
if N > M:
    N, M = M, N

if N == 1:
    if M == 1:
        print(1)
    else:
        print(M - 2)
else:
    ans = (N - 2) * (M - 2)
    print(ans)
