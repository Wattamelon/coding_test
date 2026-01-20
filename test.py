import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    queue = []
    tmp = input().strip()
    balance = True
    for i in tmp:
        if i == "(":
            queue.append(i)
        else:
            if len(queue) == 0:
                balance = False
                break
            else:
                queue.pop()
    if len(queue) == 0 and balance:
        print("YES")
    else:
        print("NO")
