def g1(N: int) -> int:
    return int(''.join(sorted(str(N), reverse=True)))

def g2(N: int) -> int:
    return int(''.join(sorted(str(N))))

def f(N: int) -> int:
    return g1(N) - g2(N)

N, K = map(int, input().split())


a = N
for i in range(K):
    a = f(a)

print(a)
