N = int(input())
L = list(map(int, input().split()))
L.sort()

sum = 0
for i in range(N - 1):
    sum += L[i]

print("Yes" if L[N - 1] < sum else "No")
