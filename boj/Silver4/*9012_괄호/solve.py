import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    tmp = deque(input().strip())
    stack = []
    res = True
    while tmp:
        i = tmp.popleft()
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                res = False
                break
            else:
                stack.pop()
    if res and len(stack) == 0:
        print("YES")
    else:
        print("NO")