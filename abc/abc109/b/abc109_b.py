N = int(input())
W = [input() for _ in range(N)]

if not len(set(W)) == N:
    print("No")
    exit()

for i in range(1, N):
    if not W[i - 1][-1] == W[i][:1]:
        print("No")
        exit()

print("Yes")
