N = int(input())
A = list(map(int, input().split()))

p = [(A[i], i + 1) for i in range(len(A))]

while len(p) > 2:
    tmp_p = []
    for i in range(len(p) // 2):
        tmp_p.append(max(p[2 * i], p[2 * i + 1]))
    p = tmp_p[:]

print(min(p)[1])
