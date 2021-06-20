N = int(input())

t = 0
for i in range(1, 10000000):
    t += i
    if N <= t:
        print(i)
        exit()        
