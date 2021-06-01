N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()

pos = K
for a, b in AB:
    if a <= pos:
        pos += b

print(pos)
