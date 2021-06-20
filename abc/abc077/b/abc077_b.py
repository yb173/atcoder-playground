import math
N = int(input())

ans = -1
for i in range(1, math.ceil(N ** .5) + 1):
    a = i * i
    if a > N:
        break
    ans = a
    
print(ans)
