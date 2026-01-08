import sys
input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    order = input().split()
    if order[0] == "1":
        q.append(order[1])
    elif order[0] == "2":
        if len(q) == 0:
            print(-1)
        else:
            a = q.pop()
            print(a)
    elif order[0] == "3":
        print(len(q))
    elif order[0] == "4":
        print(1 if len(q)==0 else 0)
    else:
        print(-1 if len(q)==0 else q[-1])
