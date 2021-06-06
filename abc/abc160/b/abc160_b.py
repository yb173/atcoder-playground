X = int(input())

ans = 0

q, mod = divmod(X, 500)

ans += q * 1000

q, mod = divmod(mod, 5)

ans += q * 5

print(ans)
