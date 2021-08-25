from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1
sx -= 1
gy, gx = map(int, input().split())
gy -= 1
gx -= 1

S = [input() for _ in range(R)]

# 始点からの最小移動コストを管理する２次元配列．-1 であれば未訪問．
cost = [[-1] * C for i in range(R)]
cost[sy][sx] = 0

q = deque()
q.append((sy, sx))

while len(q) > 0:
    y, x = q.popleft()
    # 隣接うる上下左右の４マスを確認する
    for dy, dx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        # 盤面の範囲内でなければ無視
        if not (0 <= dy < R and 0 <= dx < C):
            continue
        # 壁マスであれば無視
        if S[dy][dx] == '#':
            continue
        if cost[dy][dx] == -1:
            cost[dy][dx] = cost[y][x] + 1
            q.append((dy, dx))

# 始点から終点までの最小コストを出力
print(cost[gy][gx])
