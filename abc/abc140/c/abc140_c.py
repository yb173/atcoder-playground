N = int(input())
B = list(map(int, input().split()))

A = []
for i in range(N):
    if i == 0:
        A.append(B[0])
        continue
    if i == N - 1:
        A.append(B[N - 2])
        continue
    A.append(min(B[i - 1], B[i]))

print(sum(A))
