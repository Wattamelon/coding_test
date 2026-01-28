
# alt_solution.py
import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
m = int(input())

req.sort()
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + req[i]

if prefix[n] <= m:
    sys.stdout.write(str(req[-1]))
else:
    remain = m
    for i in range(n):
        cap = (remain // (n - i))
        if req[i] > cap:
            sys.stdout.write(str(cap))
            break
        remain -= req[i]
