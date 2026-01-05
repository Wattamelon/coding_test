import sys
input = sys.stdin.readline
write = sys.stdout.write

s = set()
m = int(input())

for _ in range(m):
    cmd = input().split()
    op = cmd[0]

    if op == "all":
        s = set(range(1, 21))
    elif op == "empty":
        s.clear()
    else:
        x = int(cmd[1])
        if op == "add":
            s.add(x)
        elif op == "remove":
            s.discard(x)
        elif op == "check":
            write("1\n" if x in s else "0\n")
        elif op == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)
