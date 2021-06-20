import sys

def debug(var):
    for k,v in globals().items():
        if id(v) == id(var):
            name = k
    print(name + ' = ' + str(var), file=sys.stderr)

s = input()
debug(s)

ss = [d for index, d in enumerate(list(s)) if index % 2 == 0]
debug(ss)

print("".join(ss))
