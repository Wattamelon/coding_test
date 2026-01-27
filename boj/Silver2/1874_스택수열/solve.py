"""import sys
input = sys.stdin.readline

t = int(input())
ex = [int(input()) for _ in range(t)]
nums = [i for i in range(t+1,1,-1)]
out = []
idx = 0
stack = [nums.pop()]
res =  []
while nums:
    while stack[-1] == ex[idx]:
        res.append(stack.pop())
        if idx<len(ex)-1:
            idx += 1
        out.append("-")
        if not nums and not stack:
            break
    if nums:
        stack.append(nums.pop())
        out.append("+")

if ex == res:
    sys.stdout.write("\n".join(out))
else:
    print("NO")
print(res)

"""
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
ex = [int(input()) for _ in range(t)]
deque = deque(ex)
nums = deque(i for i in range(1,t+1))
stack = []
out = []
while deque or nums:
    if not stack and nums:
        stack.append(nums.popleft())
        out.append("+")
        continue
    if deque[0] == stack[-1]:
        deque.popleft()
        stack.popleft()
        out.append("-")
    else:
        stack.append(nums.popleft)
        out.append("+")

