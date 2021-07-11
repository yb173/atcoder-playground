N = int(input())
S = [input() for _ in range(N)]

ex = [s for s in S if s.startswith('!')]
not_ex = [s for s in S if not s.startswith('!')]
not_ex = set(not_ex)

for e in ex:
    word = e[1:]
    if word in not_ex:
        print(word)
        exit()

print("satisfiable")
