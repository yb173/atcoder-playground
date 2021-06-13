s = int(input())
f = 0
used = set()
for i in range(1, 1000001):
    if i == 1:
        f = s
    else:
        f = f // 2 if f % 2 == 0 else 3 * f + 1
    if f in used:
        print(i)
        exit()
    used.add(f)
