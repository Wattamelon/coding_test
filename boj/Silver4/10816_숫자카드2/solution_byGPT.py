import sys
input = sys.stdin.readline

n = int(input())
cards = input().split()
dict_cards = {}
for i in cards:
    if i in dict_cards:
        dict_cards[i] += 1
    else:
        dict_cards[i] = 1

m = int(input())
nums = input().split()

out = []

for i in nums:
    if i in dict_cards:
        out.append(str(dict_cards[i]))
    else:
        out.append("0")

sys.stdout.write(" ".join(out))