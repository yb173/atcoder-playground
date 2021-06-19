H, W = map(int, input().split())
a = [input() for _ in range(H)]

h_list = []
for i in range(H):
    foundBlack = False
    for j in range(W):
        if a[i][j] == '#':
            foundBlack = True
            break
    if foundBlack:
        h_list.append(a[i])

w_list = [''] * len(h_list)
for i in range(W):
    foundBlack = False
    for j in range(len(h_list)):
        if h_list[j][i] == '#':
            foundBlack = True
            break
    if foundBlack:
        for k in range(len(h_list)):
            w_list[k] += h_list[k][i]

for i in range(len(w_list)):
    print(w_list[i])
