from collections import deque

N = int(input())
A = list(map(int, input().split()))

q = deque()

for i in range(N):
    if i % 2 == 0:
        q.append(A[i])
    else:
        q.appendleft(A[i])

if N % 2 == 1:
    q.reverse()

print(*q)
