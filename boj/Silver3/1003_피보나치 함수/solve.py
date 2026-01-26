import sys
input = sys.stdin.readline

t = int(input())
dp = [(1,0),(0,1),(0,1),(1,2)]

for _ in range(t):
    n = int(input())
    if n < len(dp):
        print(dp[n])
    else:
        while len(dp) <= n:
            tmp_0,tmp_1 = 0 , 0
            for i in dp:
                tmp_0 += i[0]
                tmp_1 += i[1]
            dp.append((tmp_0,tmp_1))
    print(dp[-1])


