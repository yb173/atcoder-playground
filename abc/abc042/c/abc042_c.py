n, k = map(int, input().split())

d = list(map(int, input().split()))
d = set(d)

while True:
    m = str(n)
    ok = True
    for v in m:
        if int(v) in d:
            ok = False
            break
    if ok:
        print(n)
        exit()

    n += 1
