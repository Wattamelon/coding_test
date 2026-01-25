# solution_byGPT.py (가장 코테스럽고 깔끔한 정석: deque + rotate)
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
moves = list(map(int, input().split()))

dq = deque((i + 1, moves[i]) for i in range(n))
out = []

while dq:
    idx, step = dq.popleft()
    out.append(str(idx))
    if not dq:
        break

    # 핵심:
    # step > 0 이면, 이미 한 칸은 popleft로 "현재 풍선"을 제거하며 이동 시작이므로 step-1만큼 더 오른쪽으로 가야 함
    # step < 0 이면, 왼쪽 이동은 그대로 step만큼 rotate 하면 됨
    if step > 0:
        dq.rotate(-(step - 1))
    else:
        dq.rotate(-step)  # step이 음수라 -step은 양수: 오른쪽 rotate == 왼쪽 이동 효과

sys.stdout.write(" ".join(out))
