import sys
sys.setrecursionlimit(10 ** 9)

H, W = map(int, input().split())
S = [input() for _ in range(H)]

sh, sw, gh, gw = None, None, None, None
for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            sh, sw = i, j
        if S[i][j] == 'g':
            gh, gw = i, j

visited = [[False] * W for _ in range(H)]

def dfs(h, w):
    if visited[h][w]: return
    visited[h][w] = True
    for dh, dw in [(h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)]:
        if not (0 <= dh < H and 0 <= dw < W):
            continue
        if S[dh][dw] == '#':
            continue
        dfs(dh, dw)

dfs(sh, sw)

print("Yes" if visited[gh][gw] else "No")
