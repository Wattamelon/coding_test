import sys
import heapq

input = sys.stdin.readline

n = int(input())
me = int(input())

if n == 1:
    print(0)
    sys.exit()

hq = []
for _ in range(n - 1):
    heapq.heappush(hq, -int(input()))

cnt = 0
while True:
    top = -heapq.heappop(hq)
    if me > top:
        print(cnt)
        break
    me += 1
    top -= 1
    cnt += 1
    heapq.heappush(hq, -top)
