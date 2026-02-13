import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]


a , b = map(int,input().split())
graph = []
visited = []
for _ in range(a):
    graph.append(list(map(int,input().strip())))
    visited.append([False]*b)

r , c = 0 , 0 # row , column

queue = deque([(r,c)])
visited[r][c] = True

while queue:
    r,c = queue.popleft()
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        if 0 <= x < a and 0 <= y < b:
            if graph[x][y] == 0:
                continue
            else:
                if graph[x][y] == 1 and not visited[x][y]:
                    continue
                else:
                    graph[x][y] = graph[r][c] + 1
                    queue.append((x,y))
                    visited[x][y] = True

print(graph[a-1][b-1])
print(graph)

"""
5 6
101010
111111
000001
111111
111111
"""


