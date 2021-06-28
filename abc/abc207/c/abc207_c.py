def isOverlap(t1, l1, r1, t2, l2, r2):
    if t1 == 1:
        if t2 == 1:
            return l2 <= r1 and l1 <= r2
        elif t2 == 2:
            return l2 <= r1 and l1 < r2
        elif t2 == 3:
            return l2 < r1 and l1 <= r2
        else:
            return l2 < r1 and l1 < r2
    elif t1 == 2:
        if t2 == 1:
            return l2 < r1 and l1 <= r2
        elif t2 == 2:
            return l2 < r1 and l1 < r2
        elif t2 == 3:
            return l2 < r1 and l1 <= r2
        else:
            return l2 < r1 and l1 < r2
    elif t1 == 3:
        if t2 == 1:
            return l2 <= r1 and l1 < r2
        elif t2 == 2:
            return l2 <= r1 and l1 < r2
        elif t2 == 3:
            return l2 < r1 and l1 < r2
        else:
            return l2 < r1 and l1 < r2
    else:
        if t2 == 1:
            return l2 < r1 and l1 < r2
        elif t2 == 2:
            return l2 < r1 and l1 < r2
        elif t2 == 3:
            return l2 < r1 and l1 < r2
        else:
            return l2 < r1 and l1 < r2

N = int(input())
d = []
for i in range(N):
    t, l, r = map(int, input().split())
    d.append([t, l, r])

ans = []
for i in range(N):
    for j in range(i + 1, N):
        ans.append(isOverlap(d[i][0], d[i][1], d[i][2], d[j][0], d[j][1], d[j][2]))

print(sum(ans))
