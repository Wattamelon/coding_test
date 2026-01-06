import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    age , name = input().split()
    age = int(age)
    heapq.heappush(q , ((age, i), name))

for _ in range(n):
    a = heapq.heappop(q)
    print(a[0][0] , a[1])