A, B = map(int, input().split())
S = input()

if not S[:A].isnumeric():
    print("No")
    exit()

if not S[A:A + 1] == '-':
    print("No")
    exit()

if not S[A + 1:].isnumeric():
    print("No")
    exit()

print("Yes")
