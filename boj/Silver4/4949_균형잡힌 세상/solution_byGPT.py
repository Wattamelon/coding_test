import sys
input = sys.stdin.readline

pair = {')': '(', ']': '['}

while True:
    s = input().rstrip()
    if s == ".":
        break

    stack = []
    ok = True

    for ch in s:
        if ch in "([":          # 여는 괄호
            stack.append(ch)
        elif ch in ")]":        # 닫는 괄호
            if not stack or stack[-1] != pair[ch]:
                ok = False
                break
            stack.pop()

    print("yes" if ok and not stack else "no")
