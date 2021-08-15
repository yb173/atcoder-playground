A, B, C, D, E, F = map(int, input().split())
A *= 100
B *= 100

water = []
sugar = []

for i in range(1, 1 + F // A): # 水の初期値は 100 * A
    for j in range(1 + F // B):
        w = A * i + B * j
        if w > F: break
        water.append(w)

for i in range(1 + F // C):
    for j in range(1 + F // D):
        s = C * i + D * j
        if s > F: break
        sugar.append(s)

water.sort()
sugar.sort()

ans_per = 0
ans_w = 0
ans_s = 0

for w in water:
    for s in sugar:
        if w + s > F: break
        if s > w * E / 100: continue

        per = s / (w + s)
        if ans_per <= per:
            ans_per = per
            ans_w = w
            ans_s = s

print(ans_w + ans_s, ans_s)
