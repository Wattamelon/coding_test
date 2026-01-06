import sys
input = sys.stdin.readline

h, w = map(int, input().split())

for _ in range(h):
    row = input().strip()
    ans = []
    last = -1  # 마지막 'c'의 위치(인덱스)
    for j, ch in enumerate(row):
        if ch == 'c':
            last = j
            ans.append(0)
        else:  # '.'
            if last == -1:
                ans.append(-1)
            else:
                ans.append(j - last)

    print(*ans)
