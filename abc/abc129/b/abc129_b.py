INF = 1 << 60

N = int(input())
W = list(map(int, input().split()))

min_diff = INF
for i in range(N):
    sum_first = 0
    sum_second = 0
    for j in range(N):
        if j <= i:
            sum_first += W[j]
        else:
            sum_second += W[j]
    min_diff = min(min_diff, abs(sum_second - sum_first))

print(min_diff)
        