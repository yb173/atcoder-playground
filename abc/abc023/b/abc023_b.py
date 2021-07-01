N = int(input())
S = input()
ans = 'b'

if S == ans:
    print(0)
    exit()

cnt = 0
while len(ans) < N:
    if (cnt + 1) % 3 == 1:
        ans = 'a' + ans + 'c'
    elif (cnt + 1) % 3 == 2:
        ans = 'c' + ans + 'a'
    else:
        ans = 'b' + ans + 'b'

    cnt += 1

    if ans == S:
        print(cnt)
        exit()

print(-1)
