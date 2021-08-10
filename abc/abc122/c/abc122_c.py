N, Q = map(int, input().split())
S = input()

tot = [0] * (N + 1)
for i in range(1, N):
    tot[i + 1] = tot[i]
    if S[i - 1] == 'A' and S[i] == 'C':
        tot[i + 1] += 1
        
for i in range(Q):
    l, r = map(int, input().split())
    print(tot[r] - tot[l])
