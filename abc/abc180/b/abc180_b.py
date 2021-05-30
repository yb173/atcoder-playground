import math
N = int(input())
X = list(map(int, input().split()))

m = 0
y = 0
c = 0
for i in range(N):
    m += abs(X[i])
    y += abs(X[i])**2
    c = max(c, abs(X[i]))

y = math.sqrt(y)

print(m)
print(y)
print(c)
