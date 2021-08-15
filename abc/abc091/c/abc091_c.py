N = int(input())

# 赤
red = [None] * N
# 青
blue = [None] * N

for i in range(N):
    a, b = map(int, input().split())
    red[i] = (a, b)

for i in range(N):
    c, d = map(int, input().split())
    blue[i] = (c, d)
blue.sort(key=lambda x: x[0])

used_red = [False] * N
used_blue = [False] * N
while True:
    found = False
    for i in range(len(blue)):
        if used_blue[i]:
            continue
        max_red_height_j = -1
        max_red_height = -1
        for j in range(len(red)):
            if used_red[j]:
                continue
            if red[j][0] < blue[i][0] and red[j][1] < blue[i][1]:
                if red[j][1] > max_red_height:
                    max_red_height_j = j
                    max_red_height = red[j][1]
        if not max_red_height_j == -1:
            used_blue[i] = True
            used_red[max_red_height_j] = True
            found = True
    if not found:
        break

print(sum(used_blue))
