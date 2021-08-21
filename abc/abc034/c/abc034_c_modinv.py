def factorial_mod(n, mod):
    a = 1
    for i in range(1, n + 1):
        a *= i
        a %= mod
    return a

MOD = 10 ** 9 + 7

w, h = map(int, input().split())
w -= 1
h -= 1

a = factorial_mod(w + h, MOD)
b = factorial_mod(w, MOD)
c = factorial_mod(h, MOD)

ans = a * pow(b, -1, MOD) * pow(c, -1, MOD)
# ans = whf * pow(wf, MOD - 2, MOD) * pow(hf, MOD - 2, MOD)
ans %= MOD

print(ans)
