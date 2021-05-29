N, M, T = map(int, input().split())

A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

rest = N
ok = True
for i in range(M):
    # バッテリー減る
    rest -= A[i] if i == 0 else A[i] - B[i - 1]
    if rest <= 0:
        ok = False
        break

    # バッテリー増える
    rest += B[i] - A[i]
    if rest > N:
        rest = N

rest -= T - B[M - 1]
if rest <= 0:
    ok = False

print("Yes" if ok else "No")
