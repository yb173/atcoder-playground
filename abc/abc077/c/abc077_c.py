N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

ans = 0
for i in range(N):
    b = B[i]

    ok = -1
    ng = N
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if A[mid] < b:
            ok = mid
        else:
            ng = mid
    if ok == -1: continue
    a_count = ok + 1

    ng = -1
    ok = N
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if b < C[mid]:
            ok = mid
        else:
            ng = mid
    if ok == N: continue
    c_count = N - ok

    ans += a_count * c_count

print(ans)
