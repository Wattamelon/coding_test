import sys
input = sys.stdin.readline

n , k = map(int,input().split())
visited = [False] * n
result = []
idx = 0
cnt = 1
for _ in range(n):
    while 1:
        if idx >= n:
            idx -= n
        if visited[idx] == False and cnt == k :
            result.append(idx+1)
            visited[idx] = True
            idx += 1
            cnt = 1
            break
        elif visited[idx] == False and cnt != k:
            cnt += 1
            idx += 1
        elif visited[idx] == True:
            idx += 1


print("<", end ="")
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i] , end = "")
    else:
        print(result[i], end = ", ")
print(">")