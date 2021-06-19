a, b = input().split()
c = int(a + b)
cc = c ** .5
print("Yes" if cc.is_integer() else "No")
