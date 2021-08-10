from itertools import product

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

N, A, B, C = map(int, input().split())
D = [int(input()) for _ in range(N)]

L = ['A', 'B', 'C', 'X']

ans = 1 << 60

for v in product(L, repeat=N):
    calc(v)

print(ans)
    

