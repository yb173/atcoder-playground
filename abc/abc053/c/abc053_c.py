x = int(input())

q, mod = divmod(x, 11)

ans = 2 * q

if mod == 0:
    print(ans)
    exit()

elif mod <= 6:
    ans += 1
else:
    ans += 2

print(ans)
