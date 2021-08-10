N, M = map(int, input().split())
nl, nr = 0, 10 ** 5 + 1

for i in range(M):
    l, r = map(int, input().split())
    if nr < l or r < nl:
        print(0)
        exit()
    else:
        nl = max(nl, l)
        nr = min(nr, r)

print(nr - nl + 1)
