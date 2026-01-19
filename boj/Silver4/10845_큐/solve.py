import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

def push(num):
    queue.append(num)

def pop():
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()

def size():
    return len(queue)

def is_empty():
    if queue:
        return 0
    else:
        return 1

def front():
    if not queue:
        return -1
    else:
        return queue[0]

def back():
    if not queue:
        return -1
    else:
        return queue[-1]

n = int(input())

for _ in range(n):
    orders = input().split()
    if orders[0] == "push":
        push(int(orders[1]))
    elif orders[0] == "pop":
        print(pop())
    elif orders[0] == "size":
        print(size())
    elif orders[0] == "empty":
        print(is_empty())
    elif orders[0] == "front":
        print(front())
    else:
        print(back())