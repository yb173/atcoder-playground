a = list(input())
b = list(input())
c = list(input())

d = {'a':a, 'b':b, 'c':c}

p = 'a'
while True:
    if len(d[p]) == 0:
        print(p.upper())
        exit()
    p = d[p].pop(0)
