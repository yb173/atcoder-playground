N = int(input())
A = list(map(int, input().split()))

p = [(A[i], i + 1) for i in range(len(A))]

while len(p) > 2:
    p = [max(p[2 * i], p[2 * i + 1]) for i in range(len(p) // 2)]

print(min(p)[1])
