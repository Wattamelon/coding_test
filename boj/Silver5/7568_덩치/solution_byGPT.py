import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

rank = []
for i in range(n):
    r = 1
    for j in range(n):
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            r += 1
    rank.append(r)

print(*rank)
