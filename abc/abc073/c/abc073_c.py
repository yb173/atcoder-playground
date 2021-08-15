N = int(input())
A = [int(input()) for _ in range(N)]

s = set()
for a in A:
    if a in s:
        s.remove(a)
    else:
        s.add(a)

print(len(s))
