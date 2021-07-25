N = int(input())
N -= 1

ans = []
while N >= 0:
    ans.append(chr(N % 26 + 97))
    N //= 26
    if N == 0:
        break
    N -= 1

ans = ans[::-1]
print(''.join(ans))
