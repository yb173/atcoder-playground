def isBingo(P):
    # 縦
    if (P[0][0] and P[0][1] and P[0][2]):
        return True
    if (P[1][0] and P[1][1] and P[1][2]):
        return True
    if (P[2][0] and P[2][1] and P[2][2]):
        return True
    # 横
    if (P[0][0] and P[1][0] and P[2][0]):
        return True
    if (P[0][1] and P[1][1] and P[2][1]):
        return True
    if (P[0][2] and P[1][2] and P[2][2]):
        return True
    # 斜め
    if (P[0][0] and P[1][1] and P[2][2]):
        return True
    if (P[2][0] and P[1][1] and P[0][2]):
        return True
    
    return False

def panch(A, P, target):
    for i in range(3):
        for j in range(3):
            if A[i][j] != target:
                continue
            P[i][j] = True

A = []
for i in range(3):
    a1, a2, a3 = map(int, input().split())
    A.append([a1, a2, a3])

P = [ [False] * 3 for _ in range(3) ]

N = int(input())
b = [int(input()) for _ in range(N)]

for i in range(N):
    panch(A, P, b[i])

print("Yes" if isBingo(P) else "No")
