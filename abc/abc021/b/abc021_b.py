N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

s = set(P)
s.add(a)
s.add(b)
print("YES" if len(s) == K + 2 else "NO")
