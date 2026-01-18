import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n + 1))
ans = []

while q:
    q.rotate(-(k - 1))   # 왼쪽으로 k-1칸 회전
    ans.append(q.popleft())

sys.stdout.write("<" + ", ".join(map(str, ans)) + ">")
