x = input()

if x == '':
    print("YES")
    exit()

while len(x) > 0:
    if x.startswith('ch'):
        x = x[2:]
        continue
    if x.startswith('o') or x.startswith('k') or x.startswith('u'):
        x = x[1:]
        continue
    print('NO')
    exit()

print("YES")
