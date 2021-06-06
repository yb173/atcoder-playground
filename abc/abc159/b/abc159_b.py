S = input()
N = len(S)

rs = S[::-1]
if rs != S:
    print("No")
    exit()

a = S[0:(N - 1) // 2]
ra = a[::-1]
if ra != a:
    print("No")
    exit()

b = S[(N + 3) // 2 - 1:N]
rb = b[::-1]
if rb != b:
    print("No")
    exit()

print("Yes")