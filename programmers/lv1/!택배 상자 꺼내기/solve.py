from collections import deque


def solution(n, w, num):
    if n % w == 0:
        grid = [deque([]) for _ in range(n // w)]
    else:
        grid = [deque([]) for _ in range((n // w) + 1)]

    cnt = 1
    row = 0
    while cnt <= n:
        """if cnt>(num//w)*w:
            row = num//w
        else:
            if cnt%w == 0:
                row = (cnt//w)-1
            else:
                row = cnt//w"""
        if cnt % w == 0:
            row = (cnt//w) - 1
        else:
            row = cnt//w
        if row % 2 == 0:
            grid[row].append(cnt)
        else:
            grid[row].appendleft(cnt)
        cnt += 1
    return grid

print(solution(22,6,8))