K = int(input())

if K % 2 == 0:
    print(-1)
    exit()

a = [0] * 1000001
# 数列を求める
a[0] = 7 % K
for i in range(1, K):
    a[i] = 10 * a[i - 1] + 7
    a[i] %= K

for i in range(K):
    if a[i] == 0:
        print(i + 1)
        exit()

print(-1)
