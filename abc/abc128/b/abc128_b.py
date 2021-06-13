N = int(input())
d = []
for i in range(N):
    s, p = input().split()
    p = int(p)
    d.append([s, -p, i + 1])
d.sort()

for item in d:
    print(item[2])
