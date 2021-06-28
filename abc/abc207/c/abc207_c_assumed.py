N = int(input())
L = []
R = []
for i in range(N):
    t, l, r = map(int, input().split())
    # 開区間を閉区間に変換する
    # t = 1: []
    # t = 2: [)
    # t = 3: (]
    # t = 4: ()
    if t == 3 or t == 4:
        l += 0.1
    if t % 2 == 0:
        r -= 0.1
    L.append(l)
    R.append(r)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if R[i] < L[j]: continue
        if R[j] < L[i]: continue
        ans += 1

print(ans)
