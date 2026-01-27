# alt.py
# 다른 로직: 필요한 만큼만 dp를 "확장"해서 처리 (lazy 확장)

import sys

input = sys.stdin.readline

t = int(input())

dp = [(1, 0), (0, 1)]  # dp[0], dp[1]

out = []
for _ in range(t):
    n = int(input())
    while len(dp) <= n:
        z = dp[-1][0] + dp[-2][0]
        o = dp[-1][1] + dp[-2][1]
        dp.append((z, o))
    out.append(f"{dp[n][0]} {dp[n][1]}")

sys.stdout.write("\n".join(out))
