import sys
from collections import deque
import heapq
input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    n , m = map(int,input().split())
    tmp = list(map(int,input().split()))
    queue = deque()
    for idx , w in enumerate(tmp):
        queue.append((-w,idx))
    hq = []
    for i in range(n):
        heapq.heappush(hq,queue[i])
    for i in range(n):
        ans = heapq.heappop(hq)
        while ans[0] != queue[0][0]:
            queue.append(queue.popleft())
        a = queue.popleft()
        if a[1] == m:
            print(i+1)






"""
for _ in range(testcase):
    n , m = map(int,input().split())
    queue = list(map(int,input().split()))
    nums = deque()
    for i in range(n):
        nums.append((i+1, queue[i]))
    nums = sorted(list(nums), key = lambda x: x[1])"""