import math
N = int(input())
ans = math.floor(1.08 * N)
if ans < 206:
    print("Yay!")
elif ans > 206:
    print(":(")
else:
    print("so-so")
