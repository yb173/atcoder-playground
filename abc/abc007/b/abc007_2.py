a = input()

if len(a) > 1:
    print(a[:-1])
    exit()

if a != 'a':
    print(chr(ord(a) - 1))
    exit()

print(-1)
