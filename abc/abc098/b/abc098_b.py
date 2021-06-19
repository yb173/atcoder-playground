N = int(input())
S = input()

ans = 0
for i in range(N + 1):
    start = S[:i]
    end = S[i:]
    start_set = set(start)
    end_set = set(end)
    ans = max(ans, len(start_set & end_set))
print(ans)
