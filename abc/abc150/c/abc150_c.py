from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

l = [v for v in range(1, N + 1)]

count = 0
for v in permutations(l, N):
    count += 1
    if P == v:
        p_index = count
    if Q == v:
        v_index = count

print(abs(p_index - v_index))
