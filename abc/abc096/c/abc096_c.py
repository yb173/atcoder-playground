H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            continue
        di_list = [i, i + 1, i, i -1]
        dj_list = [j + 1, j, j - 1, j]
        ok = False
        for di, dj in zip(di_list, dj_list):
            if di < 0 or H <= di: continue
            if dj < 0 or W <= dj: continue
            if S[di][dj] == '#':
                ok = True
                break
        if not ok:
            print('No')
            exit()

print('Yes')
