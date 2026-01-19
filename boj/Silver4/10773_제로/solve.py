import sys
input = sys.stdin.readline

k = int(input())

cnt = [int(input()) for _ in range(k)]

out = []

for i in cnt:
    if i == 0:
        out.pop()
    else:
        out.append(i)

print(sum(out))