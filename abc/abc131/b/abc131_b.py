INF = 1 << 60

N, L = map(int, input().split())

min_diff = INF
min_diff_index = -1
for i in range(N):
    tmp_diff = abs(L + i)
    if min_diff > tmp_diff:
        min_diff = tmp_diff
        min_diff_index = i

ans = 0
for i in range(N):
    if i == min_diff_index: continue
    ans += L + i

print(ans)
