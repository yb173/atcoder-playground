def calc(T):
    global ans
    a = 0
    b = 0
    c = 0
    tot = 0
    for i in range(len(T)):
        if T[i] == 'A':
            if not a == 0:
                tot += 10
            a += D[i]
        elif T[i] == 'B':
            if not b == 0:
                tot += 10
            b += D[i]
        elif T[i] == 'C':
            if not c == 0:
                tot += 10
            c += D[i]
    if a == 0 or b == 0 or c == 0:
        return
    tot += abs(A - a)
    tot += abs(B - b)
    tot += abs(C - c)
    ans = min(ans, tot)
    return

def dfs(T):
    if len(T) == N:
        calc(T)
        return
    for i in range(4):
        dfs(T + (L[i],))

N, A, B, C = map(int, input().split())
D = [int(input()) for _ in range(N)]

L = ['A', 'B', 'C', 'X']

ans = 1 << 60
dfs(())
print(ans)
