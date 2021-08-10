N, K = map(int, input().split())

total = 0
for i in range(1, N + 1):
    now = i
    cnt = 0
    while now < K:
        now *= 2
        cnt += 1
    total += 0.5 ** cnt

print(total / N)
