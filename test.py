import sys
from collections import deque

input = sys.stdin.readline

n , m , k , x = map(int,input().split())

cities = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    idx , num = map(int,input().split())
    cities[idx].append(num)

queue = deque([x])
while queue:
    v = queue.popleft()

    for i in cities[v]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = visited[v] + 1

out = []
for idx , num in enumerate(visited):
    if num == k:
        out.append(str(idx))

if len(out) == 0:
    print(-1)
else:
    sys.stdout.write("\n".join(out))


"""
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4

"""