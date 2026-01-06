import sys

input = sys.stdin.readline

a , b = map(int,input().split())

n = int(input())
z = []
cnt = 0
for _ in range(n):
    z.append((abs(int(input()) - b)))
z.sort()
cur = abs(a-b)
if z[0] >= cur:
    print(cur)
else:
    print(z[0]+1)
"""
for i in z:
    if i < a-b:
        cnt = cnt + 1 + i
        print(cnt)
        break


"""



