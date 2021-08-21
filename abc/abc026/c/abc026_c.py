INF = 1 << 60

N = int(input())
B = [int(input()) for _ in range(N - 1)]

sub = [[] for i in range(N)]

for i in range(N - 1):
    sub[B[i] - 1].append(i + 1)

p = [None] * N
p_max = [None] * N
p_min = [None] * N
for i in reversed(range(N)):
    if len(sub[i]) == 0:
        p[i] = 1
        continue
    p_max[i] = 0
    p_min[i] = INF
    for v in sub[i]:
        p_max[i] = max(p_max[i], p[v])
        p_min[i] = min(p_min[i], p[v])
    p[i] = p_max[i] + p_min[i] + 1

print(p[0])
