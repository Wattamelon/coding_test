import sys
input = sys.stdin.readline

n = int(input())
cows = []
for _ in range(n):
    cows.append(list(map(int,input().split())))

cows.sort(key = lambda x:x)

cnt = 0
for i in cows:
    if i[0] > cnt:
        cnt += (i[0]-cnt)
    cnt += i[1]
print(cnt)