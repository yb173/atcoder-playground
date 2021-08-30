S = input()

S = S.split('.')

x = S[0]
y = int(S[1])

if 0 <= y <= 2:
    print(x + '-')
elif 3 <= y <= 6:
    print(x)
else:
    print(x + '+')
