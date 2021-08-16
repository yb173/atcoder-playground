from math import ceil, sqrt

INF = 1 << 60

def large(a: int, b: int) -> int:
    return max(len(str(a)), len(str(b)))

N = int(input())

ans = INF
for a in range(1, ceil(sqrt(N)) + 1):
    if not N % a == 0: continue
    b = N // a
    ans = min(ans, large(a, b))

print(ans)
