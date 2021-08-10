N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[0])
tot = 0
price = 0
for i in range(N):
    tot += AB[i][1]
    price += AB[i][0] * AB[i][1]
    if tot >= M:
        diff = tot - M
        price -= diff * AB[i][0]
        print(price)
        exit()
