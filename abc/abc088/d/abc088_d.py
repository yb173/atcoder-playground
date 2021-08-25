from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

cost = [[-1] * W for _ in range(H)]
cost[0][0] = 0

q = deque([(0, 0)])

while len(q) > 0:
    h, w = q.popleft()
    for dh, dw in [(h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)]:
        if not (0 <= dh < H and 0 <= dw < W):
            continue
        if S[dh][dw] == "#":
            continue
        if cost[dh][dw] == -1:
            cost[dh][dw] = cost[h][w] + 1
            q.append((dh, dw))

if cost[H - 1][W - 1] == -1:
    print(-1)
    exit()

white = 0
for i in range(H):
    white += S[i].count(".")

mi = cost[H - 1][W - 1]

print(white - mi - 1)
