N = int(input())
S = [int(input()) for _ in range(N)]

t = sum(S)

if t % 10 != 0:
    print(t)
    exit()

S.sort()
T = [S[i] for i in range(N) if S[i] % 10 != 0]

if len(T) == 0:
    print(0)
    exit()

print(t - T[0])
