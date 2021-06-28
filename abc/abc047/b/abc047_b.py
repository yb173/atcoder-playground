def fill(T, x, y, a):
    if a == 1:
        for i in range(H):
            for j in range(x):
                T[i][j] = False
    if a == 2:
        for i in range(H):
            for j in range(x, W):
                T[i][j] = False
    if a == 3:
        for i in range(y):
            for j in range(W):
                T[i][j] = False
    if a == 4:
        for i in range(y, H):
            for j in range(W):
                T[i][j] = False

W, H, N = map(int, input().split())
T = [[True] * W for i in range(H)]
for i in range(N):
    x, y, a = map(int, input().split())
    fill(T, x, y, a)

ans = 0
for i in range(H):
    ans += sum(T[i])

print(ans)
