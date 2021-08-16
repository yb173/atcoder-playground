s, c = map(int, input().split())

if 2 * s > c:
    print(c // 2)
    exit()

ans = s
c -= 2 * s
ans += c // 4
print(ans)
