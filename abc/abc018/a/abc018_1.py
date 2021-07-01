a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))

for i in range(3):
    rank = 1
    for j in range(3):
        if a[i] < a[j]:
            rank += 1
    print(rank)
