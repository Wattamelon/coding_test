import sys
input = sys.stdin.readline

def rnd(x):
    if x%1 >= 0.5:
        return int(x)+1
    else:
        return int(x)

n = int(input())
if n == 0:
    print(0)
else:
    op = [int(input()) for _ in range(n)]
    cut = rnd(n * 0.15)

    op.sort()
    print(rnd(sum(op[cut:n-cut])/(n-2*cut)))