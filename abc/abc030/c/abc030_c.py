from bisect import bisect_left

N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t = 0
ans = 0

while True:
    if t > a[-1]:
        break
    else:
        t = a[bisect_left(a, t)] + X
    
    if t > b[-1]:
        break
    else:
        t = b[bisect_left(b, t)] + Y
    
    ans += 1
    
print(ans)
