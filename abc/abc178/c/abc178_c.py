MOD = 10 ** 9 + 7

def powmod(x, n):
    ans = 1
    for i in range(n):
        ans = ans * x % MOD
    return ans

N = int(input())

ans = powmod(10, N) - 2 * powmod(9, N) + powmod(8, N)
ans %= MOD

print(ans) 
