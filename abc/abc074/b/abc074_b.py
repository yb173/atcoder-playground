import sys

def debug(var):
    for k,v in globals().items():
        if id(v) == id(var):
            name = k
    print(name + ' = ' + str(var), file=sys.stderr)

N = int(input())
debug(N)
K = int(input())
debug(K)

x = list(map(int, input().split()))
debug(x)
ans = 0
for i in range(N):
    a_dist = x[i] * 2
    b_dist = (K - x[i]) * 2
    debug(a_dist)
    debug(b_dist)
    ans += min(a_dist, b_dist)
print(ans)
