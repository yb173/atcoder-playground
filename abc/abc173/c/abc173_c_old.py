H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(1 << H): # bit全探索 2^H 通り
    for j in range(1 << W): # bit全探索 2^W 通り
        black_cnt = 0
        for x in range(H):
            for y in range(W):
                # 列挙に x が含まれていたら（塗り潰される対象だったら）スキップ
                if i & (1 << x) > 0:
                    continue
                # 列挙に x が含まれていたら（塗り潰される対象だったら）スキップ                    
                if j & (1 << y) > 0:
                    continue
                
                # 塗り潰される対象じゃなかったら処理をおこなう
                if S[x][y] == '#':
                    black_cnt += 1
        if black_cnt == K:
            ans += 1

print(ans)
