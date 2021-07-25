N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append((A[i], str(i + 1)))
B.sort(key=lambda x: x[0])
print(B)
print(' '.join(map(lambda x: x[1], B)))

