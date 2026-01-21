import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int,input().split()))
m = int(input())
x = list(map(int,input().split()))

res = []
for is_exist in x:
    if is_exist in a:
        res.append("1")
    else:
        res.append("0")

sys.stdout.write("\n".join(res))