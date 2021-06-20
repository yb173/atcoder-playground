N = int(input())

if N == 1:
    print(1)
    exit()

a, b = 2, 1
for i in range(N - 1):
    a, b = b, a + b

print(b)
