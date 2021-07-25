W, H, x, y = map(int, input().split())

S = W * H / 2
multi = 1 if x * 2 == W and y * 2 == H else 0

print(S, multi)
