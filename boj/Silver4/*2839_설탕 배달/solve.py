import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 5001
dp[0] , dp[1],dp[2],dp[3],dp[4],dp[5] = -1 , -1, -1, 1, -1, 1

for i in range(6,n+2):
    if i%5 == 0:
        dp[i] = dp[i-5] + 1
    elif i%3 == 0:
        dp[i] = dp[i-3] + 1
    else:
        if dp[i - 5] == -1 and dp[i - 3] == -1:
            dp[i] = -1
            continue
        a = dp[i-5] if dp[i-5] != -1 else 5000
        b = dp[i-3] if dp[i-3] != -1 else 5000
        dp[i] = min(a,b) + 1


print(dp[n])
"""
for i in range(1,n+1):
    print(f"dp[{i}] : {dp[i]}")
"""