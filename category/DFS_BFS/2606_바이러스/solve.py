import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
n_pairs = int(input())
coms = []
for _ in range(n+1):
    coms.append([])
visited = [False] * (n+1)
cnt = 0
for _ in range(n_pairs):
    a , b = map(int,input().split())
    coms[a].append(b)
    coms[b].append(a)

queue = deque(coms[1])
visited[1] = True
while queue:
    q = queue.popleft()
    if not visited[q] :
        cnt += 1
        visited[q] = True
        for i in coms[q]:
            queue.append(i)

print(cnt)