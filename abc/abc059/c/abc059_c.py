n = int(input())
a = list(map(int, input().split()))

# + - + -
t1 = 0
now1 = 0
for i in range(n):
    t1 += a[i]
    if i % 2 == 0:
        # + である必要がある
        if t1 < 1:
            now1 += -t1 + 1
            t1 = 1
    else:
        # - である必要がある
        if t1 > -1:
            now1 += t1 + 1
            t1 = -1

# - + - +
t2 = 0
now2 = 0
for i in range(n):
    t2 += a[i]
    if i % 2 == 0:
        # - である必要がある
        if t2 > -1:
            now2 += t2 + 1
            t2 = -1
    else:
        # + である必要がある
        if t2 < 1:
            now2 += -t2 + 1
            t2 = 1

print(min(now1, now2))
