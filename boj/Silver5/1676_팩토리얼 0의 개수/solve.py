import sys
import math

input = sys.stdin.readline

n = math.factorial(int(input()))
cnt = 0
num = str(n)
for i in range(n):
    if num[-i-1] == "0":
        cnt += 1
    else:
        print(cnt)
        break
