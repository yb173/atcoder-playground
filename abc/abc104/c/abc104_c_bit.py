D, G = map(int, input().split())
P, C = [], []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

ans = 1 << 60

for bit in range(1 << D):
    s = 0
    num = 0
    rest_max = -1
    for i in range(D):
        if bit & (1 << i):
            s += 100 * (i + 1) * P[i] + C[i]
            num += P[i]
        else:
            rest_max = i
    if s < G:
        s1 = 100 * (rest_max + 1)
        need = (G - s + s1 - 1) // s1
        if need >= P[rest_max]:
            continue
        num += need
    ans = min(ans, num)

print(ans)
