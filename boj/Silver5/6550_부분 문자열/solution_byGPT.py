import sys
input = sys.stdin.readline
write = sys.stdout.write

for line in sys.stdin:          # EOF까지
    s, t = line.split()
    i = 0                       # s 포인터

    for ch in t:                # t를 한 번만 순회
        if i < len(s) and s[i] == ch:
            i += 1
            if i == len(s):     # 다 맞추면 조기 종료
                break

    write("Yes\n" if i == len(s) else "No\n")
