def read(Q):
    R = set()
    for i in range(N):
        for j in range(N):
            if Q[i][j] == '#':
                R.add((i, j))
    return R

N = int(input())

S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

S = read(S)
T = read(T)

if not len(S) == len(T):
    print("No")
    exit()

for _ in range(4):
    # 最も左（複数あればそのうち最も上）の # を (0, 0) の位置にずらす
    min_x, min_y = min(S)
    S = set((x - min_x, y - min_y) for x, y in S)
    min_x, min_y = min(T)
    T = set((x - min_x, y - min_y) for x, y in T)

    if S == T:
        print("Yes")
        exit()
    
    # T を回転
    T = set((y, -x) for x, y in T)

print("No")
