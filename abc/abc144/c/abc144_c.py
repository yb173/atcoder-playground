from math import floor
def is_prime(n: int):
    """素数かどうかを判定する関数

    引数で与えられた値が素数かどうかを判定します．

    Args:
        n (int): 判定する数値

    Returns:
        bool: 与えられた数値が素数かどうか
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    m = floor(n ** .5) + 1
    for i in range(3, m, 2):
        if n % i == 0:
            return False
    return True

def divisors_set(num: int):
    """約数のセットを求める関数

    引数で与えられた整数の約数の一覧をセット型で返却します．
    計算量は O(N^0.5) です．

    Args:
        num (int): 約数を求める整数

    Returns:
        set<int>: 約数のセット
    """
    divisors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

N = int(input())
if is_prime(N):
    print(N - 1)
    exit()

s = divisors_set(N)
s.remove(1)
s.remove(N)

ans = 1 << 60
for v in s:
    w = N // v
    ans = min(ans, v + w - 2)

print(ans)
