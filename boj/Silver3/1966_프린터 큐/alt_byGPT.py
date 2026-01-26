# 다른 로직 (카운팅 배열로 "현재 최대 중요도"를 O(1)에 관리)
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n, m = map(int, input().split())
    pr = list(map(int, input().split()))

    cnt = [0] * 10
    for x in pr:
        cnt[x] += 1

    cur_max = 9
    while cur_max > 0 and cnt[cur_max] == 0:
        cur_max -= 1

    dq = deque((p, i) for i, p in enumerate(pr))
    printed = 0

    while True:
        p, i = dq[0]
        if p == cur_max:
            dq.popleft()
            printed += 1
            cnt[p] -= 1
            if i == m:
                out.append(str(printed))
                break
            while cur_max > 0 and cnt[cur_max] == 0:
                cur_max -= 1
        else:
            dq.rotate(-1)

sys.stdout.write("\n".join(out))
