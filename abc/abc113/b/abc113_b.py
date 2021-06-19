INF = 1 << 60

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

min_diff = INF
index = 0
for i in range(N):
    tmp_t = T - H[i] * 0.006
    diff = T - tmp_t
    if min_diff > diff:
        min_diff = diff
        index = i + 1

print(index)
