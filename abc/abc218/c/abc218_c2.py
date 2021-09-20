def same(A, B, N):
    for i in range(N):
        for j in range(N):
            if A[i] != B[j]:
                return False
    return True

N = int(input())
S = [input() for _ in range(N)]


# まず座標圧縮
