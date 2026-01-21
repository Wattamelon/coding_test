import sys
input = sys.stdin.readline
def compare(x,y):
    x = set(x)
    y = set(y)
    res = sorted(x.intersection(y))
    print(len(res))
    sys.stdout.write("\n".join(res))

n,m = map(int,input().split())
x = [input().rstrip() for _ in range(n)]
y = [input().rstrip() for _ in range(m)]

if len(x)>=len(y):
    compare(x,y)
else:
    compare(y,x)