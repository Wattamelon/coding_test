import sys

input = sys.stdin.readline

h , w = map(int,input().split())

for _ in range(h):
    grid = list(input().strip())
    tmp = []
    if "c" not in grid:
        for _ in range(w):
            tmp.append("-1")
    else:
        cnt = 0
        for i in grid:
            if i == "c":
                tmp.append("0")
                cnt = 1
            elif i == "." and cnt == 0:
                tmp.append("-1")
            else:
                tmp.append(str(cnt))
                cnt += 1
    print(" ".join(tmp))




