N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0
for bit in range(1 << K):
    used = [0] * (N + 1)
    for k in range(K):
        c, d = CD[k]
        if bit & 1 << k:
        # if bit >> k & 1:
            used[c] += 1
        else:
            used[d] += 1
    cnt = 0
    for a, b in AB:
        if used[a] and used[b]:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
