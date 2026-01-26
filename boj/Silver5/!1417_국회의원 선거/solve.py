import sys
import heapq

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
elif n == 2:
    cand = [int(input()) for _ in range(n)]
    if cand[0] > cand[1]:
        print(0)
    elif cand[0] == cand[1]:
        print(1)
    else:
        print((cand[1]-cand[0])//2 +1)
else:
    me = int(input())
    hq = []
    cnt = 0
    for _ in range(n-1):
        v = int(input())
        heapq.heappush(hq,-v)
    while True :
        top = -heapq.heappop(hq)
        if me > top:
            print(cnt)
            break
        else:
            cnt += 1
            me += 1
            top -= 1
            heapq.heappush(hq,-top)
