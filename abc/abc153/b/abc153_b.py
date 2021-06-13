H, N = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)

print("Yes" if H <= total else "No")
