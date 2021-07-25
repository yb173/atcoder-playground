from collections import defaultdict

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]
d = defaultdict(lambda: 0)
for a in A:
    d[a - 1] += 1

ans = []
for i in range(N):
    print("Yes" if K - Q + d[i] > 0 else "No")
