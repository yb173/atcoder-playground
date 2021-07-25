N = int(input())
H = list(map(int, input().split()))

for i in range(N):
    if i == N - 1:
        continue
    if H[i] < H[i + 1]:
        H[i + 1] -= 1
        continue
    elif H[i] == H[i + 1]:
        continue
    else:
        print("No")
        exit()

print("Yes")
    