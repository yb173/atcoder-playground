N, K = map(int, input().split())
A_MAX = 10 ** 5
cnt = [0] * (A_MAX)
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    cnt[a] += b

t = 0
for i in range(A_MAX):
    t += cnt[i]
    if K <= t:
        print(i + 1)
        exit()
