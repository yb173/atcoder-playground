H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        cnt = 0
        if S[i][j] == '#': cnt += 1
        if S[i + 1][j] == '#': cnt += 1
        if S[i][j + 1] == '#': cnt += 1
        if S[i + 1][j + 1] == '#': cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1

print(ans)
