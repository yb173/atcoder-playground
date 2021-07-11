r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r = r2 - r1
c = c2 - c1

if r == 0 and c == 0:
    ans = 0
elif r == c or r == -c:
    ans = 1
elif abs(r) + abs(c) <= 3:
    ans = 1
# パリティが変わらない（r, c = 偶, 偶 or 奇，奇の場合のみ true となる）
elif (r ^ c ^ 1) & 1:
    ans = 2
# マンハッタン距離が6以下
elif abs(r) + abs(c) <= 6:
    ans = 2
# ???
elif abs(r + c) <= 3 or abs(r - c) <= 3:
    ans = 2
else:
    ans = 3

print(ans)
