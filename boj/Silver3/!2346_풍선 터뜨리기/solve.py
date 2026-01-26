import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(list(map(int,input().split())))
visited = [False] * n
out = []
idx = 0

while 1:
    if not visited[idx]:
        visited[idx] = True
        num = queue[idx]
        out.append(str(idx + 1))
        if len(out) == n:
            break
        if num > 0:
            while num>0:
                idx += 1
                if idx >= n:
                    idx = 0
                if not visited[idx]:
                    num -= 1
        elif num < 0:
            while num < 0:
                idx -= 1
                if idx < 0:
                    idx = n-1
                if not visited[idx]:
                    num +=1



sys.stdout.write(" ".join(out))


