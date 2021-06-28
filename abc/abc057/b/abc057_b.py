def m_dist(a1, b1, a2, b2):
    return abs(a1 - a2) + abs(b1 - b2)

n, m = map(int, input().split())

ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
    
cd = []
for j in range(m):
    c, d = map(int, input().split())
    cd.append([c, d])

for i in range(n):
    min_dist = 10 ** 9
    min_index = -1
    for j in range(m):
        dist = m_dist(ab[i][0], ab[i][1], cd[j][0], cd[j][1])
        if dist < min_dist:
            min_dist = dist
            min_index = j + 1
    print(min_index)
