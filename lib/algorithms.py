def digitSum(N: int):
    """各桁の和を求める関数

    引数で与えられた整数の和を返却します．
    計算量は O(len(N))) です．

    Args:
        num (int): 整数

    Returns:
        int: 各桁の和
    """
    sum = 0
    while N > 0:
        q, mod = divmod(N, 10)
        sum += mod
        N = q
    return sum

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

def divisors_list(num: int):
    """約数の配列を求める関数

    引数で与えられた整数の約数の一覧を昇順にソートされた配列型で返却します．
    計算量は O(N^0.5 * log(N)) です．

    Args:
        num (int): 約数を求める整数

    Returns:
        list of int: 昇順にソートされた約数の配列
    """
    divisors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return sorted(list(divisors))

def prime_number_list(limit: int):
    """素数の配列を求める関数

    引数で与えられた上限値まで素数を計算し配列で返却します．

    Args:
        limit (int): 上限値

    Returns:
        list of int: 昇順にソートされた素数の配列
    """
    prime_numbers = []
    for num in range(2, limit + 1):
        for i in range(3, num ** .5 + 1, 2):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers

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

from math import floor
def next_prime_number(now: int):
    """次の素数を求める関数

    引数で与えられた数値以上の素数の内，最小のものを返却します．

    Args:
        now (int): 現在の値

    Returns:
        int: 次の素数
    """
    if now == 2:
        return now
    
    if now % 2 == 0:
        now += 1
    
    while True:
        for i in range(3, floor(now ** .5) + 1, 2):
            if now % i == 0:
                break
        else:
            return now
        now += 2

from math import gcd
def lcm(a: int, b: int):
    """最小公倍数求める関数

    a と b の最小公倍数を求めます．

    Args:
        a (int): 一つ目の値
        b (int): 二つ目の値

    Returns:
        int: a と b の最小公倍数
    """
    return a * b // gcd(a, b)
