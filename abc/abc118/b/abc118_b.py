N, M = map(int, input().split())

# res = {1, 2, ... , M}
res = set(range(1, M + 1))

for i in range(N):
    K, *A = map(int, input().split())
    # 両方に存在する要素のみが残る
    res &= set(A)

print(len(res))

