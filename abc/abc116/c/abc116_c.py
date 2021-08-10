N = int(input())
H = list(map(int, input().split()))

ans = 0
active = 0

for h in H:
    if active >= h:
        active = h
    else:
        ans += h - active
        active = h

print(ans)
