import sys
H, W = map(int, input().split())
S = [input() for _ in range(H)]
print(S, file=sys.stderr)

T = [["#"] * W for i in range(H)]
print(T, file=sys.stderr)

for i in range(H):
    for j in range(W):
        # 自身が爆弾の場合はスキップ
        if S[i][j] == "#": continue
        # 自身の周囲９マスを調べる
        ans = 0
        lx = [i - 1, i, i + 1]
        ly = [j - 1, j, j + 1]
        for x in lx:
            for y in ly:
                if x < 0 or H <= x: continue
                if y < 0 or W <= y: continue
                if S[x][y] == '#':
                    ans += 1
        T[i][j] = str(ans)

for i in range(H):
    print("".join(T[i]))
