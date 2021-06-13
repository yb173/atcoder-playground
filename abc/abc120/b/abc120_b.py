A, B, K = map(int, input().split())

d = []
for i in range(1, 101):
    if A % i == 0 and B % i == 0:
        d.append(i)
d.sort(reverse=True)
print(d[K - 1])
