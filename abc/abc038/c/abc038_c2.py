n = int(input())
a = list(map(int, input().split()))

prev = 0
x = 0
ans = 0

for v in a:
    if v > prev:
        x += 1
    else:
        x = 1
    ans += x
    prev = v

print(ans)
