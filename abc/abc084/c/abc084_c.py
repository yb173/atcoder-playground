N = int(input())
C = [None] * (N - 1)
S = [None] * (N - 1)
F = [None] * (N - 1)
for i in range(N - 1):
    C[i], S[i], F[i] = map(int, input().split())

for x in range(N):
    t = 0
    for i in range(x, N - 1):
        if t <= S[i]:
            t = S[i]
        else:    
            t = (t + F[i] - 1) // F[i] * F[i]
        t += C[i]
    print(t)
