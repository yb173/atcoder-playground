import math

def next_prime_number(now: int):
    if now == 2:
        return now
    
    if now % 2 == 0:
        now += 1
    
    while True:
        for i in range(3, math.ceil(now ** .5) + 1, 2):
            if now % i == 0:
                break
        else:
            return now
        now += 2

X = int(input())

print(next_prime_number(X))
