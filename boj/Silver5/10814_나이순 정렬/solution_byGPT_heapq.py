import sys
import heapq

input = sys.stdin.readline

n = int(input())
hq = []

for idx in range(n):
    age, name = input().split()
    heapq.heappush(hq, (int(age), idx, name))  # (나이, 입력순서, 이름)

out = []
while hq:
    age, _, name = heapq.heappop(hq)
    out.append(f"{age} {name}\n")

sys.stdout.write("".join(out))
