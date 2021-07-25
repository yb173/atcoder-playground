N = int(input())
d = list(map(int, input().split()))
d.sort()
l = d[N // 2 - 1]
r = d[N // 2]
print(r - l)

