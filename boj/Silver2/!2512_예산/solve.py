import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
ask = list(map(int,input().split()))
budget = int(input())
ask.sort()
visited = [False] * n
tmp = 0
budget = budget - (budget%n)
if budget >= sum(ask):
    print(ask[-1])
else:
    standard = budget//n
    tmp = 0
    cnt = 0
    for i in ask:
        if i<=standard:
            tmp += (standard - i)
        else:
            cnt+=1
    standard += tmp//cnt
    print(standard)
"""
못풀었음
"""




