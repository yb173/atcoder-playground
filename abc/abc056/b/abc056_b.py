w, a, b = map(int, input().split())
if a <= b + w and b <= a + w:
    print(0)
    exit()

if a + w < b:
    print(b - (a + w))
elif b + w < a:
    print(a - (b + w))
