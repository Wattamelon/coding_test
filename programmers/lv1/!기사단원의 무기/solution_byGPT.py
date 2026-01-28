# solution_byGPT.py
import sys

def solution(number, limit, power):
    div_cnt = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            div_cnt[j] += 1

    total = 0
    for i in range(1, number + 1):
        total += power if div_cnt[i] > limit else div_cnt[i]
    return total
