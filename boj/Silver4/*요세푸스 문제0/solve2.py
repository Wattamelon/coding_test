from collections import deque

n , k = map(int,input().split())
arr = deque()
res = []    #  result
for i in range(1,n+1):
    arr.append(i)

while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    res.append(arr.popleft())

print("<",end ="")
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i], end = "")
        continue
    print(res[i],end = ", ")
print(">")