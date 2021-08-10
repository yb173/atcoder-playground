N = int(input())

if N == 0:
    print(0)
    exit()

s = ''
while N != 0:
    if N % 2 != 0:
        N -= 1
        s = '1' + s
    else:
        s = '0' + s
    N //= -2

print(s)
