import sys
input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    s = input().strip()
    bal = 0
    ok = True
    for ch in s:
        if ch == '(':
            bal += 1
        else:  # ')'
            bal -= 1
            if bal < 0:
                ok = False
                break
    out.append("YES" if ok and bal == 0 else "NO")

sys.stdout.write("\n".join(out))
