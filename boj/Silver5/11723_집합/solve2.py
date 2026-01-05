import sys
input = sys.stdin.readline

s = set()
def add(x):
    s.add(x)

def remove(x):
    if x in s:
        s.remove(x)

def check(x):
    if x in s:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in s:
        remove(x)
    else:
        add(x)
def all():
    s = set()
    for i in range(1,21):
        s.add(i)
    return s

def empty():
    s.clear()

m = int(input())

for _ in range(m):
    order = input().split()
    operator = order[0]
    if operator == "add":
        num = int(order[1])
        add(num)
    elif operator == "remove":
        num = int(order[1])
        remove(num)
    elif operator == "check":
        num = int(order[1])
        check(num)
    elif operator == "toggle":
        num = int(order[1])
        toggle(num)
    elif operator == "all":
        s = all()
    elif operator == "empty":
        empty()

