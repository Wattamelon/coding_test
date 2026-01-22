# solution_byGPT.py
import sys
input = sys.stdin.readline

t = int(input())
queries = [int(input()) for _ in range(t)]

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

out = [str(dp[n]) for n in queries]
sys.stdout.write("\n".join(out))
