S = input()
K = int(input())
N = len(S)

s = set()
for i in range(N):
    for j in range(1, 6):
        s.add(S[i:i + j])

t = list(s)
t.sort()

print(t[K - 1])
