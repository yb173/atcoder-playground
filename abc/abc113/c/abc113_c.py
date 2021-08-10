N, M = map(int, input().split())

# 県が key，その県に所属する市とインデックスのタプルの配列が value
G = [[] for _ in range(N)]

for i in range(M):
    p, y = map(int, input().split())
    p -= 1
    G[p].append((y, i))

# 完成した値とインデックスがタプルになった配列
F = []
for i in range(len(G)):
    G[i].sort(key=lambda x: x[0])
    pre = str(i + 1).zfill(6)
    for j in range(len(G[i])):
        su = str(j + 1).zfill(6)
        F.append((pre + su, G[i][j][1]))

F.sort(key=lambda x: x[1])

for f in F:
    print(f[0])
