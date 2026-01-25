import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
new_list = deque()
for idx, num in enumerate(nums):
    idx += 1
    new_list.append([num,idx])
# -----------------------
first = new_list.popleft()
order = [first[1]]
cnt = first[0]
while new_list:
    if cnt > 0:
        for _ in range(cnt-1):
            tmp = new_list.popleft()
            new_list.append(tmp)
    elif cnt < 0 :
        for _ in range(abs(cnt)):
            tmp = new_list.pop()
            new_list.appendleft(tmp)
    current = new_list.popleft()
    order.append(current[1])
    cnt = current[0]
print(*order)