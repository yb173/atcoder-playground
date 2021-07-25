H, W, K = map(int, input().split())
c = [input() for _ in range(H)]

ans = 0
for bith in range(1 << H):
    for bitw in range(1 << W):
        total = 0
        for h in range(H):
            for w in range(W):
                # 赤に塗るマスはスキップ
                if bith & (1 << h): continue
                if bitw & (1 << w): continue
                if c[h][w] == '#':
                    total += 1
        if total == K:
            ans += 1

print(ans)
