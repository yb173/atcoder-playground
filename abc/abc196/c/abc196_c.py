N = int(input())
for i in range(1, 1000001):
    p = int(str(i) * 2)
    if p > N:
        print(i - 1)
        exit()
