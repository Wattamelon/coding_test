import sys
input = sys.stdin.readline

while True:
    tmp = input()
    bal = True
    if tmp == ".\n":
        break
    tmp = list(tmp.strip())
    stack = []
    for i in tmp:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]" or i == ")":
            if len(stack) > 0:
                cur = stack.pop()
                if i == ")":
                    if cur == "[":
                        bal = False
                        break
                elif i == "]":
                    if cur == "(":
                        bal = False
                        break
            else:
                bal = False
                break
        else:
            continue
    if bal and len(stack) == 0:
        print("yes")
    else:
        print("no")