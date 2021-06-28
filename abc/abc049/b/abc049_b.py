H, W = map(int, input().split())
C = [input() for _ in range(H)]
for i in range(H * 2):
    print(C[i // 2])
