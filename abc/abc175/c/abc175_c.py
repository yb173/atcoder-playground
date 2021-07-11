X, K, D = map(int, input().split())
X = abs(X)

count = X // D
if count > K:
    print(X - K * D)
    exit()

# K の残弾
K -= count 
# 移動後の位置
X -= count * D

if K % 2 == 0:
    print(X)
else:
    print(D - X)
