import sys
import heapq
input = sys.stdin.readline


n = int(input())

queue = []
out = []
for _ in range(n):
    x = int(input())
    if x == 0 and not queue:
        out.append("0")
    elif x == 0:
        out.append(str(heapq.heappop(queue)))
    else:
        heapq.heappush(queue,x)

sys.stdout.write("\n".join(out))