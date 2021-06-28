H, W = map(int, input().split())
a = [input() for _ in range(H)]
print('#' * (W + 2))

for i in range(H):
    print('#' + a[i] + '#')

print('#' * (W + 2))
