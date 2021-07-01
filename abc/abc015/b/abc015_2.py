from math import ceil

N = int(input())
A = list(map(int, input().split()))
AA = s = [d for d in A if d > 0]
print(ceil(sum(AA) / len(AA)))
