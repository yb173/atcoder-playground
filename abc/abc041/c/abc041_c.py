n = int(input())
a = list(map(int, input().split()))

ai = [None] * n
for i in range(n):
    ai[i] = (a[i], i + 1)
ai.sort(key=lambda x: x[0], reverse=True)

for i in range(n):
    print(ai[i][1])
