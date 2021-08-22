N = int(input())

if N == 0:
    print(0)
    exit()

k = 0
while True:
    k += 1
    if 2 ** k > N:
        break

print(k - 1)
