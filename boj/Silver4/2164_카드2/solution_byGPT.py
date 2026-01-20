import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cards = deque(range(1, n + 1))

while len(cards) > 1:
    cards.popleft()               # 버리기
    cards.append(cards.popleft()) # 아래로 옮기기

print(cards[0])
