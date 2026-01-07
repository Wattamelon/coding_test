import sys
input = sys.stdin.readline

n = int(input())

words = []
for _ in range(n):
    word = input().strip()
    if word not in words:
        words.append(word)

words.sort(key = lambda x : (len(x),x))

sys.stdout.write("\n".join(words))