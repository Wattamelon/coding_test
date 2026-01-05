import sys
input = sys.stdin.readline

# 메모리 초과뜸

m = int(input())
s = set()
out = []

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
            s.discard(x)              # 없으면 무시 (remove처럼 에러 안 남)
        elif op == "check":
            out.append("1\n" if x in s else "0\n")
        elif op == "toggle":
            s.remove(x) if x in s else s.add(x)

sys.stdout.write("".join(out))
