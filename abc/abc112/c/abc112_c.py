N = int(input())
X, Y, H = [], [], []
for i in range(N):
    x, y, h = map(int, input().split())
    X.append(x)
    Y.append(y)
    H.append(h)

for cx in range(101):
    for cy in range(101):
        # 高さ候補を求める
        vertex_height = None
        for i in range(N):
            if H[i]:
                if vertex_height == None:
                    vertex_height = H[i] + abs(cx - X[i]) + abs(cy - Y[i])
                else:
                    tmp_vertex_height = H[i] + abs(cx - X[i]) + abs(cy - Y[i])
                    if not vertex_height == tmp_vertex_height:
                        vertex_height = -1
                        break
        if vertex_height == None or vertex_height == -1:
            continue
        # 高さがすべてのクエリを満たしていればそれが答え
        ok = True
        for i in range(N):
            if max(vertex_height - abs(X[i] - cx) - abs(Y[i] - cy), 0) != H[i]:
                ok = False
        if ok:
            print('{} {} {}'.format(cx, cy, vertex_height))
            exit()
