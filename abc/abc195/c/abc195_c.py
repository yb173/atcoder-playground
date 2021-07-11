N = int(input())
ans = 0

if 10 ** 3 <= N:
    ans += N - 999

if 10 ** 6 <= N:
    ans += N - 999999

if 10 ** 9 <= N:
    ans += N - 999999999

if 10 ** 12 <= N:
    ans += N - 999999999999

if 10 ** 15 <= N:
    ans += N - 999999999999999

print(ans)
