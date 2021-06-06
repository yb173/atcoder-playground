K = int(input())
S = input()

if len(S) <= K:
    print(S)
    exit()

print(S[0:K] + '...')
