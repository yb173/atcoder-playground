from itertools import permutations

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

for (x1, y1), (x2, y2), (x3, y3) in permutations(xy, 3):
    x2 -= x1
    y2 -= y1
    x3 -= x1
    y3 -= y1
    
    if x2 * y3 == x3 * y2:
        print("Yes")
        exit()

print("No")
