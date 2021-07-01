m = int(input())

if m < 100:
    print('00')

if 100 <= m <= 5000:
    ans = m // 100
    print('{:02}'.format(ans))

if 6000 <= m <= 30000:
    ans = m // 1000 + 50
    print(ans)

if 35000 <= m <= 70000:
    ans = (m // 1000 - 30) // 5 + 80
    print(ans)

if 70000 < m:
    print('89')
