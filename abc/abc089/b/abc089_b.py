N = int(input())
S = list(input().split())
print("Three" if len(set(S)) == 3 else "Four")
