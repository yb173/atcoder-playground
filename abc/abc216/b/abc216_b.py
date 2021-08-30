N = int(input())
# S = [None] * N
# T = [None] * N
s = set()
for i in range(N):
    a, b = input().split()
    s.add((a, b))

print("Yes" if len(s) != N else "No")

