import sys
input = sys.stdin.readline

n = int(input())
p = sorted(map(int, input().split()))

total = 0
acc = 0
for x in p:
    acc += x
    print(f"acc = {acc}")
    total += acc
    print(f"total = {total}")

print(total)
