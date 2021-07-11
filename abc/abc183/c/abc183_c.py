import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

nums = list(range(1, N))

ans = 0
for indexes in itertools.permutations(nums):
    indexes = [0] + list(indexes)
    pos = 0
    for i in range(N):
        pos += T[indexes[i]][indexes[(i + 1) % N]]

    if pos == K:
        ans += 1        

print(ans)
