from collections import defaultdict

N = int(input())
V = list(map(int, input().split()))

even = [V[i] for i in range(N) if i % 2 == 0]
odd = [V[i] for i in range(N) if i % 2 == 1]

even_counter = defaultdict(lambda: 0)
odd_counter = defaultdict(lambda: 0)

for i in range(N // 2):
    even_counter[even[i]] += 1
    odd_counter[odd[i]] += 1

even_counter = sorted(even_counter.items(), key=lambda x: x[1], reverse=True)
odd_counter = sorted(odd_counter.items(), key=lambda x: x[1], reverse=True)

# 最頻値が even と odd で異なる場合，最頻値以外の数の和が答え
if not even_counter[0][0] == odd_counter[0][0]:
    ans = N - even_counter[0][1] - odd_counter[0][1]
    print(ans)
    exit()

# ===== 以下は最頻値が even と odd で同じ場合 =====

# ２番目の最頻値
even_second_value = even_counter[1][1] if len(even_counter) > 1 else 0
odd_second_value = odd_counter[1][1] if len(odd_counter) > 1 else 0

# ２番目の最頻値の数が多いほうが１番目を譲る
if even_second_value >= odd_second_value:
    ans = N - odd_counter[0][1] - even_second_value
else:
    ans = N - odd_second_value - even_counter[0][1]

print(ans)
