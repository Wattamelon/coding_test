import sys

input = sys.stdin.readline

n = int(input())

pos = []

for _ in range(n):
    x , y = map(int, (input().split()))
    pos.append([x,y])

pos.sort(key = lambda x : (x[1] , x[0]))
for i in pos:
    print(*i)