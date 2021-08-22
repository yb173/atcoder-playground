from itertools import permutations

S, K = input().split()
S = list(S)
K = int(K)

s = set()
for v in permutations(S):
    s.add(''.join(v))

T = list(s)
T.sort()

print(T[K - 1])
