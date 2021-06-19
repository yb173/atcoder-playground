def compute_divisors(num):
    divisors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

N = int(input())

list = [len(compute_divisors(i)) == 8 for i in range(1, N + 1, 2)]

print(sum(list))
