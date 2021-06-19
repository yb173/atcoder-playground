N = int(input())
A = list(map(int, input().split()))
A.sort()

B = []
for i in range(N):
    B.append(i + 1)

print("Yes" if A == B else "No")