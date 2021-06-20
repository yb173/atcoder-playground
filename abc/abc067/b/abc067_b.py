N, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
t = 0
for i in range(K):
    t += l[i]
print(t)
