N = int(input())
p = [int(input()) for _ in range(N)]
p.sort()
p[N - 1] = p[N - 1] // 2
print(sum(p))
