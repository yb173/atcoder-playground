X = int(input())

pos = 100
years = 0
while X > pos:
    years += 1
    pos = pos + pos // 100

print(years)
