import sys

input = sys.stdin.readline

def add(x):
    s.add(x)

def remove(x):
    s.discard(x)

def check(x):
    out.append("1\n" if x in s else "0\n")

def toggle(x):
    if x in s:
        remove(x)
    else:
        add(x)

def all():
    s = set(range(1,21))
    return s

def empty():
    s.clear()


m = int(input())
s = set()
out = []
for _ in range(m):
    cmd = input().split()
    op = cmd[0]

    if op == "all":
        s = all()
    elif op == "empty":
        empty()
    else:
        x = int(cmd[1])
        if op == "add":
            add(x)
        elif op == "remove":
            remove(x)
        elif op == "check":
            check(x)
        elif op == "toggle":
            toggle(x)

sys.stdout.write("".join(out))