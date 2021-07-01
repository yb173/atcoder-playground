N = int(input())
S = [input() for _ in range(N)]

name = None
n = 0
for s in S:
    if n < S.count(s):
        n = S.count(s)
        name = s

print(name)
