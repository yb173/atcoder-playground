S = input()

for i in range(len(S)):
    s = S[i]
    if (i + 1) % 2 == 0:
        if s == 'R':
            print('No')
            exit()
    else:
        if s == 'L':
            print('No')
            exit()

print('Yes')
