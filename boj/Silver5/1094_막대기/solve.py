import sys
input = sys.stdin.readline

x = int(input())
out = [64]

while sum(out) != x:
    tmp = out.pop()
    tmp //= 2
    out.append(tmp)
    if sum(out)<x:
        out.append(tmp)

print(len(out))