A, B = map(int, input().split())
pos = A + B
if pos % 2 != 0:
    print("IMPOSSIBLE")
    exit()

print(pos // 2)
