import inspect
import re
import sys
import math

from collections import defaultdict
from collections import deque

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

S = input()
d = defaultdict(lambda: 0)
for v in S:
    d[v] += 1
debug(d)

if d['o'] > 4:
    print(0)
    exit()

if d['o'] == 4:
    print(1)
    exit()

