from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

l = list(permutations(range(1, N + 1)))
a = l.index(P)
b = l.index(Q)

print(abs(b - a))
