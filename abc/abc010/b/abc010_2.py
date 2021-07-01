n = int(input())
a = list(map(int, input().split()))

ok = [1, 3, 7, 9]

ans = 0
for f in a:
    need = 10
    for o in ok:
        if o <= f:
            need = min(need, f - o)
    ans += need

print(ans)
