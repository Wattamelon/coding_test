# solution_byGPT.py
# BOJ 1003 피보나치 함수
# 코테용 베스트: 0~40까지 미리 전처리해서 O(1)로 답 출력

import sys

input = sys.stdin.readline

t = int(input())

# dp[n] = (zero_count, one_count)
dp = [(0, 0)] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, 41):
    dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

out = []
for _ in range(t):
    n = int(input())
    out.append(f"{dp[n][0]} {dp[n][1]}")

sys.stdout.write("\n".join(out))
