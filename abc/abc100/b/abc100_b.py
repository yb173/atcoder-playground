D, N = map(int, input().split())
if N == 100:
    N += 1
ans = str(N)
for i in range(D):
    ans += '00'
print(ans)
