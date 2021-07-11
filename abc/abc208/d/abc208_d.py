import inspect
import re
import sys

from math import pi, factorial, sin, cos, tan, ceil, floor
from statistics import mode
from collections import defaultdict, Counter, deque

sys.setrecursionlimit(10 ** 9)

INF = 1 << 60
MOD = 10**9 + 7

def debug(var):
    cf = inspect.currentframe()
    cfc = cf.f_code
    bf = cf.f_back
    bfi = inspect.getframeinfo(bf)
    e_0 = bfi.code_context[0]
    matched = re.match(r'.*{0}\((.+)\)[^)]*'.format(cfc.co_name), e_0)
    arg_name = matched.group(1)
    print(arg_name + ' = ' + str(var), file=sys.stderr)

def f(s, t, k):
    if s == t: return 0
    

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)]
debug(G)