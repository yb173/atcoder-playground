n = int(input())
a = list(map(int, input().split()))

ans = 0
l = 0
r = 0
while l < n:
    while r < n - 1:
        if r < l:
            r = l
            continue

        if a[r] < a[r + 1]:
            r += 1
        else:
            break
    # この時点での r は，区間 (l, r) で条件を満たす最大の r

    ans += r - l + 1
    l += 1

print(ans)
