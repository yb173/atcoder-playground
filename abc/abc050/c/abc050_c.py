from collections import Counter

MOD = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)

if N % 2 == 1:
    for i in range(N // 2 + 1):
        v = i * 2
        if v == 0:
            if not c[0] == 1:
                print(0)
                exit()
        else:
            if not c[v] == 2:
                print(0)
                exit()
else:
    for i in range(N // 2):
        v = i * 2 + 1
        if not c[v] == 2:
            print(0)
            exit()

ans = 1
for i in range(N // 2):
    ans *= 2
    ans %= MOD

print(ans)
