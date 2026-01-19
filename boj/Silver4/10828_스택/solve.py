import sys

input = sys.stdin.readline

n = int(input())
q = []
out = []
for _ in range(n):
    order = input().split()
    op = order[0]
    if op == "push":
        q.append(order[1])
    elif op == "pop":
        out.append(q.pop()) if q else out.append("-1")
    elif op == "size":
        out.append(str(len(q)))
    elif op == "empty":
        out.append("0") if q else out.append("1")
    else:
        out.append(str(q[-1])) if q else out.append("-1")

sys.stdout.write("\n".join(out))