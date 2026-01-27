import sys
input = sys.stdin.readline

t = int(input())
dp = [(1,0),(0,1),(1,1),(1,2)]
out = []
for _ in range(t):
    n = int(input())
    if n < len(dp):
        out.append(f"{dp[n][0]} {dp[n][1]}")
    else:
        while len(dp) <= n:
            zero = dp[-1][0] + dp[-2][0]
            one = dp[-1][1] + dp[-2][1]
            dp.append((zero,one))
        out.append(f"{dp[-1][0]} {dp[-1][1]}")

sys.stdout.write("\n".join(out))


