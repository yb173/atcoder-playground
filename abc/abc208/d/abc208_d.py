def f(s, t, k):
    if s == t: return 0
    
N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)]


