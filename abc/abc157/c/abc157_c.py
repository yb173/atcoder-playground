N, M = map(int, input().split())
s, c = [], []
for i in range(M):
    ss, cc = map(int, input().split())
    ss -= 1
    s.append(ss)
    c.append(cc)

start = 10 ** (N - 1) if N > 1 else 0
end = 10 ** (N - 1) * 10

for i in range(start, end):
    i = str(i)
    ok = True
    for j in range(M):
        if not int(i[s[j]]) == c[j]:
            ok = False
            break
    if ok:
        print(i)
        exit()

print(-1)
