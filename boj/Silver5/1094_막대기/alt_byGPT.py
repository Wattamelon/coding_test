# alt_solution.py
import sys
input = sys.stdin.readline

x = int(input())

sticks = [64]
while sum(sticks) > x:
    smallest = sticks.pop()
    half = smallest // 2
    sticks.append(half)
    if sum(sticks) < x:
        sticks.append(half)

sys.stdout.write(str(len(sticks)))
