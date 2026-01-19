import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
# 입력을 받을 때 바로 Counter에 넣으면 메모리와 시간을 아낄 수 있습니다.
cards = Counter(input().split())

m = int(input())
nums = input().split()

# 리스트 컴프리헨션을 사용하면 더 빠르고 간결합니다.
print(*(cards.get(i, 0) for i in nums))