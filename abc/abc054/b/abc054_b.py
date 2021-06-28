def isOverlap(A, B, diff) -> bool:
    for d in range(diff + 1):
        for e in range(diff + 1):
            ok = True
            for i in range(len(B)):
                if not A[i + e][d:d + len(B)] == B[i]:
                    ok = False
                    break
            if ok:
                return True
    return False

N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

print("Yes" if isOverlap(A, B, len(A) - len(B)) else "No")
