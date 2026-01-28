# alt_solution.py
import sys

def solution(number, limit, power):
    total = 0
    for i in range(1, number + 1):
        cnt = 0
        j = 1
        while j * j <= i:
            if i % j == 0:
                cnt += 1 if j * j == i else 2
            j += 1
        total += power if cnt > limit else cnt
    return total
