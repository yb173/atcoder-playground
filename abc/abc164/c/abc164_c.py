N = int(input())
S = [input() for _ in range(N)]

s = set()
for item in S:
    s.add(item)

print(len(s))
