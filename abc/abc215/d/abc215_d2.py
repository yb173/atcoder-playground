N, M = map(int, input().split())
A = list(map(int, input().split()))
max_A = max(max(A), M)

k = [True] * (max_A + 1) # i が条件を満たす k か（i が使えるか）
is_prime = [True] * (max_A + 1) # i が素数か
prime = [] # A の素因数

# A の要素は使えない
for a in A:
    k[a] = False

# エラトステネスの篩
for i in range(2, max_A + 1):
    if not is_prime[i]:
        continue
    for j in range(i * 2, max_A, i):
        is_prime[j] = False
        # i は j の素因数
        # j が A の要素なら i は使えない素数
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)

# 使えない素数 p に関して，p の倍数も使えなくする
for p in prime:
    for j in range(p * 2, M + 1, p):
        k[j] = k[j] and k[p]
print(k)

# 使える数を ans に入れる
ans = [1]
for i in range(2, M + 1):
    if k[i]:
        ans.append(i)

print(len(ans))
for v in ans:
    print(v)
