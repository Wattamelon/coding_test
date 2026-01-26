# solution_byGPT.py
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(r, c):
    visited[r][c] = True
    if grid[r][c] == '-':
        nc = c + 1
        if nc < m and not visited[r][nc] and grid[r][nc] == '-':
            dfs(r, nc)
    else:  # '|'
        nr = r + 1
        if nr < n and not visited[nr][c] and grid[nr][c] == '|':
            dfs(nr, c)

cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)
