from math import sin, cos, pi, sqrt

A, B, H, M = map(int, input().split())

# 短針の角度
theta_m = M / 60 * 2 * pi

# 長針の角度
theta_h = (H / 12 + M / 720) * 2 * pi
    
# 短針の先の座標
xm = cos(theta_m) * B
ym = sin(theta_m) * B

# 長針の先の座標
xh = cos(theta_h) * A
yh = sin(theta_h) * A

# 距離
dist = sqrt((xh - xm) ** 2 + (yh - ym) ** 2)

print(dist)
