
### >>> Debugger ========================================================
import inspect
import re
import sys

def debug(var):
    cf = inspect.currentframe()
    cfc = cf.f_code
    bf = cf.f_back
    bfi = inspect.getframeinfo(bf)
    e_0 = bfi.code_context[0]
    matched = re.match(r'.*{0}\((.+)\)[^)]*'.format(cfc.co_name), e_0)
    arg_name = matched.group(1)
    print(arg_name + ' = ' + str(var), file=sys.stderr)
### ======================================================== Debugger <<<

from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

q = deque()
debug(q)

q = deque([0])
debug(q)

q = deque()
q.append(0)
debug(q)

q = deque([0])
q.append(1)
q.append(2)
debug(q)
debug(q.pop())
debug(q)

q = deque([0])
q.append(1)
q.append(2)
debug(q)
debug(q.popleft())
debug(q)