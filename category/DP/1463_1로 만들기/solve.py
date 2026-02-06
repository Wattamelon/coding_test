import sys
input = sys.stdin.readline

x = int(input())

dp = [0,0,1,1]
if x<len(dp):
    print(dp[x])
    exit()
for i in range(4,x+1):
    tmp = []
    if i%3==0:
        tmp.append(dp[i//3]+1)
    if i%2 == 0 :
        tmp.append(dp[i // 2] + 1)
    tmp.append(dp[i-1] + 1)
    dp.append(min(tmp))


print(dp[-1])