from heapq import heapify, heappop, heappush

N = int(input())
Q = [tuple(map(int, input().split())) for _ in range(N)]

diff = 0
hq = []
heapify(hq)

for q in Q:
    if q[0] == 1:
        heappush(hq, q[1] - diff)
    elif q[0] == 2:
        diff += q[1]
    else:
        print(heappop(hq) + diff)
