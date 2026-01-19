import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    ps = input().strip()  # 문자열 그대로 사용
    stack = []

    for char in ps:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                print("NO")
                break
            stack.pop()
    else:
        # break에 걸리지 않고(즉, 중간에 에러 없이) 루프가 끝난 경우
        if not stack:
            print("YES")
        else:
            print("NO")