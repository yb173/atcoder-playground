x1, y1, x2, y2 = map(int, input().split())

# 点1から点2へのベクトル
dx = x2 - x1
dy = y2 - y1

# 点2から点3へのベクトル
dx, dy = -dy, dx
x3 = x2 + dx
y3 = y2 + dy

# 点3から点4へのベクトル
dx, dy = -dy, dx
x4 = x3 + dx
y4 = y3 + dy

print(x3, y3, x4, y4)
