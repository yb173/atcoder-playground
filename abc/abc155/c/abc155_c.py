from statistics import multimode

N = int(input())
S = [input() for _ in range(N)]

ans = multimode(S)
ans.sort()
for v in ans:
    print(v)
