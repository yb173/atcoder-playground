X, N = map(int, input().split())
p = list(map(int, input().split()))
p = set(p)

if N == 0:
    print(X)
    exit()

mini = 10 ** 9
mini_index = 10 ** 9
for i in range(0, 102):
    if i in p:
        continue
    diff = abs(X - i)
    if mini > diff:
        mini_index = i
        mini = diff

print(mini_index)
