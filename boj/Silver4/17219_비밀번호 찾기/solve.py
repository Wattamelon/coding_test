import sys
input = sys.stdin.readline

n , m = map(int,input().split())
info = {}
for _ in range(n):
    add , pw = input().split()
    info[add] = pw
order = [input().strip() for _ in range(m)]

sys.stdout.write("\n".join(info[i] for i in order))