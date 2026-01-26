# 다른 로직 (배열로 양방향 연결리스트 흉내: next/prev)
# rotate 없이도 '터진 풍선 건너뛰기'를 O(1)로 처리 가능 (N이 커져도 견고)
import sys
input = sys.stdin.readline

n = int(input().strip())
move = [0] + list(map(int, input().split()))

# 1..n 원형 연결
nxt = [0] * (n + 1)
prv = [0] * (n + 1)
for i in range(1, n + 1):
    nxt[i] = i + 1 if i < n else 1
    prv[i] = i - 1 if i > 1 else n

cur = 1
out = []

for _ in range(n):
    out.append(str(cur))
    step = move[cur]

    # cur 제거
    a, b = prv[cur], nxt[cur]
    nxt[a] = b
    prv[b] = a

    if len(out) == n:
        break

    # 다음 시작 위치: 오른쪽으로 1칸(=b) 또는 왼쪽으로 1칸(=a)부터 이동
    if step > 0:
        cur = b
        for __ in range(step - 1):
            cur = nxt[cur]
    else:
        cur = a
        for __ in range((-step) - 1):
            cur = prv[cur]

sys.stdout.write(" ".join(out))
