S = input()

s = set(S)
if len(s) == 1:
    print('Weak')
    exit()

w = True
for i in range(3):
    if (int(S[i]) + 1) % 10 == int(S[i + 1]):
        continue
    else:
        w = False
        break

if w:
    print('Weak')
    exit()

print('Strong')
