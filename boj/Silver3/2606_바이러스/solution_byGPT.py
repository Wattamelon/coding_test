# solution_byGPT.py  (BFS, 코테용 깔끔/안전)
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
q = deque([1])
visited[1] = True
cnt = 0

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            cnt += 1
            q.append(nxt)

print(cnt)
