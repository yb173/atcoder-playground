N = int(input())
S = input()
S = list(S)

for i in range(N):
    if i % 2 == 0:
        if S[i] == '1':
            print('Takahashi')
            exit()
    else:
        if S[i] == '1':
            print('Aoki')
            exit()
