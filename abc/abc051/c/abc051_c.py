sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

path1 = 'R' * dx + 'U' * dy + 'L' * dx + 'D' * dy
path2 = 'D' + 'R' * (dx + 1) + 'U' * (dy + 1) + 'L'
path3 = 'U' + 'L' * (dx + 1) + 'D' * (dy + 1) + 'R'

print(path1 + path2 + path3)
