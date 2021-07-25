N = int(input())

# 人とその人の発言のグラフ
honest = [[] for _ in range(N)]
unkind = [[] for _ in range(N)]
for i in range(N):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        x -= 1
        if y == 0:
            unkind[i].append(x)
        else:
            honest[i].append(x)

ans = 0
for bit in range(1 << N):
    hu = []
    for i in range(N):
        hu.append(bool(bit & (1 << i)))
    ok = True
    for i in range(N):
        # 正直者の発言に矛盾がないか
        if bit & (1 << i):
            for h in honest[i]:
                if not hu[h]:
                    ok = False
                    break
            for u in unkind[i]:
                if hu[u]:
                    ok = False
                    break
    if ok:
        ans = max(ans, sum(hu))

print(ans)
