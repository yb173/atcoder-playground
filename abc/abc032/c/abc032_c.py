N, K = map(int,input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
    exit()

# S に 0 が含まれておらず，K が 0 の場合，答えは 0
if K == 0:
    print(0)
    exit()

l, r = 0, 0
m = 1
ans = 0

# [l, r]
while True:
    if m <= K:
        ### K を超えていない場合
        
        # 答えを更新
        ans = max(ans, r - l)

        if r == N:
            break
        
        # 右端の積を追加
        m *= S[r]

        # 右を伸ばす
        r += 1

    else:
        ### K を超えた場合

        # 左端の積を除外
        m //= S[l]

        # 左を１つ進める
        l += 1
        
        # 左が右を追い越したら右を左にする
        if l > r:
            r = l

print(ans)
