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

from itertools import chain
def fast_prime_set(n: int):
    """ n までの素数のセットを求める関数
    
    引数で与えられた n までの素数のセットを返却します．

    Args:
        n (int): 最大値

    Returns:
        Set[int]: 素数のセット
    """
    if n < 4:
        return ({}, {}, {2}, {2, 3})[n]
    n_sqrt = int(n ** 0.5) + 1
    primes = {2, 3} | set(chain(range(5, n + 1, 6), range(7, n + 1, 6)))
    for i in range(5, n_sqrt, 2):
        if i in primes:
            primes.difference_update(range(i * i, n, i * 2))
    return primes

from collections import defaultdict
def prime_factorization(x: int):
    """ x の素因数分解をおこなう関数
    
    引数で与えられた値の素因数分解をおこないます．

    Args:
        x (int): 素因数分解の対象

    Returns:
        DefaultDict[int, int]: 素因数がキー，冪乗数が値の辞書
    """
    primes = fast_prime_set(1000)

    fact = defaultdict(int)
    for prime in primes:
        while x % prime == 0:
            fact[prime] += 1
            x //= prime
        if x == 1:
            break
        if x in primes:
            fact[x] += 1
            break
    return fact

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


def compress(X):
    """座標を圧縮する関数
    
    Args:
        X (list of int): 座標の配列
    Returns:
        list of int: 圧縮された座標
    """
    d = {}
    Y = sorted(list(set(X)))
    for i in range(len(Y)):
        d[Y[i]] = i + 1
    return [d[X[i]] for i in range(len(X))]
