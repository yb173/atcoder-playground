H, W, N = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB.append((a, b, i + 1))


AB.sort(key=lambda x: x[0])
ad = []

for i in range(N):
    if i == 0:
        index = 1
    else:
        if not AB[i - 1][0] == AB[i][0]:
            index += 1
    ad.append((index, AB[i][2]))
ad.sort(key=lambda x: x[1])


AB.sort(key=lambda x: x[1])
bd = []
for i in range(N):
    if i == 0:
        index = 1
    else:
        if not AB[i - 1][1] == AB[i][1]:
            index += 1
    bd.append((index, AB[i][2]))
bd.sort(key=lambda x: x[1])


for i in range(N):
    print('{} {}'.format(ad[i][0], bd[i][0]))
