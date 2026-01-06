import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
rank = []
for i in arr:
    cnt = 1
    for j in arr:
        if i[0] >= j[0] and i[1] >= j[1]:
            continue
        elif i[0] >= j[0] or i[1] >= j[1]:
            continue
        else:
            cnt += 1
    rank.append(cnt)
print(*rank)