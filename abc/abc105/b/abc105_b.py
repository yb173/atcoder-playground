N = int(input())

for i in range(0, N // 4 + 1):
    for j in range(0, N // 7 + 1):
        if N == i * 4 + j * 7:
            print("Yes")
            exit()

print("No")
