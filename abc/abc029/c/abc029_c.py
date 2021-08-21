from itertools import product

N = int(input())

for v in product(['a', 'b', 'c'], repeat=N):
    print(''.join(v))
