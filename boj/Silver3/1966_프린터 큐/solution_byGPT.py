# solution_byGPT.py
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n, m = map(int, input().split())
    pr = list(map(int, input().split()))

    dq = deque((p, i) for i, p in enumerate(pr))
    printed = 0

    while True:
        p, i = dq[0]
        if p == max(x[0] for x in dq):
            dq.popleft()
            printed += 1
            if i == m:
                out.append(str(printed))
                break
        else:
            dq.rotate(-1)

sys.stdout.write("\n".join(out))
