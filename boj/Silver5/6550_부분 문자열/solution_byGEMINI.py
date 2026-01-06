import sys

input = sys.stdin.readline

while True:
    try:
        line = input()
        if not line: break
        s, t = line.split()

        idx = 0
        len_s = len(s)

        # t를 직접 순회 (속도 최적화)
        for char in t:
            if char == s[idx]:
                idx += 1
                # s를 다 찾았으면 조기 종료 (불필요한 순회 방지)
                if idx == len_s:
                    break

        if idx == len_s:
            print("Yes")
        else:
            print("No")

    except:
        break