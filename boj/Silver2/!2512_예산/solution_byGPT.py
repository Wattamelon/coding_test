# solution_byGPT.py
import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
m = int(input())

req.sort()

if sum(req) <= m:
    sys.stdout.write(str(req[-1]))
else:
    left, right = 0, req[-1]
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for x in req:
            total += min(x, mid)
        if total <= m:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    sys.stdout.write(str(ans))
