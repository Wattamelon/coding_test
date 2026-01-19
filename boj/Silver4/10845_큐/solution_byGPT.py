import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
out = []

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if op == "push":
        q.append(cmd[1])  # 출력만 할 거라 문자열로 둬도 됨
    elif op == "pop":
        out.append(q.popleft() if q else "-1")
    elif op == "size":
        out.append(str(len(q)))
    elif op == "empty":
        out.append("0" if q else "1")
    elif op == "front":
        out.append(q[0] if q else "-1")
    else:  # back
        out.append(q[-1] if q else "-1")

sys.stdout.write("\n".join(out))
