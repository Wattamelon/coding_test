import sys
input = sys.stdin.readline

res = set()

def add(res, num):
    res.add(num)

def remove(res,num):
    try:
        res.remove(num)
    except:
        pass

def check(res,num):
    if num in res:
        print(1)
    else:
        print(0)

def toggle(res,num):
    if num in res:
        res.remove(num)
    else:
        res.add(num)

def all(res):
    empty(res)
    for i in range(1,21):
        res.add(i)

def empty(res):
    res = set()
    return res

n = int(input())


for i in range(n):
    order = input().split()
    if order[0] == "add":
        add(res, int(order[1]))
    if order[0] == "remove":
        remove(res, int(order[1]))
    if order[0] == "check":
        check(res, int(order[1]))
    if order[0] == "toggle":
        toggle(res, int(order[1]))
    if order[0] == "all":
        all(res)
    if order[0] == "empty":
        res = empty(res)