S = input()

ans = 0
for i in range(10000):
    used = [False] * 10
    v = i

    for j in range(4):
        used[v % 10] = True
        v = v // 10

    ok = True
    for i in range(10):
        if S[i] == 'o' and not used[i]:
            ok = False
            break
        if S[i] == 'x' and used[i]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
