from bisect import bisect_left, bisect_right

L, Q = map(int, input().split())
L = [1] * (L + 1)
# C = [None] * Q
# X = [None] * Q
for i in range(Q):
    # C[i], X[i] = map(int, input().split())
    c, x = map(int, input().split())
    if c == 1:
        L[x] = 0
    else:
        left = bisect_left(L[:x], 0)
        right = bisect_right(L[x:], 1)
        print(right + x - left - 1)
