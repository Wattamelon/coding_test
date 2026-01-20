from collections import deque

cards = deque(i for i in range(1, int(input())+1))

while 1:
    if len(cards) == 1:
        print(cards[0])
        break
    cards.popleft()
    if len(cards) == 1:
        print(cards[0])
        break
    cards.append(cards.popleft())
    if len(cards) == 1:
        print(cards[0])
        break