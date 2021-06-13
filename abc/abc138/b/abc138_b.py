N = int(input())
A = list(map(int, input().split()))

denominator = 0
for i in range(N):
    denominator += 1 / A[i]

print(1 / denominator)
