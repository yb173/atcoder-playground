from bisect import bisect_left, bisect_right

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
    a_index = bisect_left(A, b)
    c_index = bisect_right(C, b)
    ans += a_index * (N - c_index)

print(ans)
